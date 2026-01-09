from flask import Flask, render_template, request, redirect, url_for, session
from db import get_db_connection
import pickle
import hashlib

app = Flask(__name__)
app.secret_key = "secret123"

# Load ML model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("home.html")

# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        email = request.form.get("email").strip().lower()
        password = request.form.get("password")

        if not email or not password:
            error = "Email and password are required"
            return render_template("login.html", error=error)

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        db = get_db_connection()
        cur = db.cursor()

        cur.execute(
            "SELECT id, name, email, password FROM users WHERE email = %s",
            (email,)
        )
        user = cur.fetchone()

        cur.close()
        db.close()

        if not user or hashed_password != user[3]:
            error = "Invalid email or password"
            return render_template("login.html", error=error)

        # ✅ SUCCESS
        session["user_id"] = user[0]
        session["name"] = user[1]
        session["email_id"] = user[2]

        return redirect(url_for("dashboard"))

    return render_template("login.html", error=error)

# ---------------- DASHBOARD ----------------
# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    # Get user info from session
    user_id = session.get("user_id")
    user_email = session.get("email_id")
    user_name = session.get("name", "User")  # fallback

    if not user_email:
        return redirect(url_for("login"))

    db = get_db_connection()
    cur = db.cursor()

    # Check if admin
    is_admin = (user_email == "admin@gmail.com")

    if is_admin:
        # Admin sees total counts of all scans
        cur.execute("SELECT COUNT(*) FROM scans")
        total = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM scans WHERE result='PHISHING'")
        phishing = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM scans WHERE result='SAFE'")
        safe = cur.fetchone()[0]

    else:
        # Regular user sees only their scans
        cur.execute("SELECT COUNT(*) FROM scans WHERE email_id=%s", (user_email,))
        total = cur.fetchone()[0]

        cur.execute(
            "SELECT COUNT(*) FROM scans WHERE result='PHISHING' AND email_id=%s",
            (user_email,)
        )
        phishing = cur.fetchone()[0]

        cur.execute(
            "SELECT COUNT(*) FROM scans WHERE result='SAFE' AND email_id=%s",
            (user_email,)
        )
        safe = cur.fetchone()[0]

    cur.close()
    db.close()

    return render_template(
        "dashboard.html",
        name=user_name,
        email_id=user_email,
        total=total,
        phishing=phishing,
        safe=safe
    )


# ---------------- SCAN EMAIL ----------------
@app.route("/scan", methods=["GET", "POST"])
def scan():
    result = None
    score = 0

    if request.method == "POST":
        email_text = request.form.get("email", "").strip()
        email_id = session.get("email_id", "unknown")
        user_name = session.get("name", "unknown")  # ✅ ADDED

        # ---------------- LOW-CONTENT FILTER ----------------
        if len(email_text.split()) <= 2:
            result = "NEUTRAL"
            score = 0
            return render_template("scan.html", result=result, score=score)

        # ---------------- ML PREDICTION ----------------
        vector = vectorizer.transform([email_text])
        prediction = model.predict(vector)[0]
        probability = model.predict_proba(vector)[0]

        score = int(max(probability) * 100)
        result = "PHISHING" if prediction == "phishing" else "SAFE"

        # ---------------- STORE RESULT ----------------
        db = get_db_connection()
        cur = db.cursor()
        cur.execute(
            """
            INSERT INTO scans 
            (email_id, user_name, email_content, result, risk_score)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (email_id, user_name, email_text, result, score)
        )
        db.commit()
        cur.close()
        db.close()

    return render_template("scan.html", result=result, score=score)


# ---------------- HISTORY ----------------
@app.route("/history")
def history():
    user_email = session.get("email_id")
    if not user_email:
        return redirect(url_for("login"))

    query = request.args.get("query", "").strip()
    filter_option = request.args.get("filter", "").strip()
    order = request.args.get("order", "desc")

    db = get_db_connection()
    cur = db.cursor()

    is_admin = (user_email == "admin@gmail.com")

    if is_admin:
        sql = """
        SELECT id, email_id, email_content, result, risk_score, scanned_at
        FROM scans WHERE 1=1
        """
        params = []
    else:
        sql = """
        SELECT id, email_content, result, risk_score, scanned_at
        FROM scans WHERE email_id=%s
        """
        params = [user_email]

    if query:
        sql += " AND email_content LIKE %s"
        params.append(f"%{query}%")

    if filter_option in ["SAFE", "PHISHING", "NEUTRAL"]:
        sql += " AND result=%s"
        params.append(filter_option)

    sql += " ORDER BY id ASC" if order == "asc" else " ORDER BY id DESC"

    cur.execute(sql, tuple(params))
    data = cur.fetchall()

    cur.close()
    db.close()

    return render_template(
        "history.html",
        data=data,
        is_admin=is_admin,
        order=order
    )


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


#register
@app.route("/register", methods=["GET", "POST"])
def register():
    error = None

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email").strip().lower()
        password = request.form.get("password")
        confirm = request.form.get("confirm_password")

        if not name or not email or not password or not confirm:
            error = "All fields are required"
            return render_template("register.html", error=error)

        if password != confirm:
            error = "Passwords do not match"
            return render_template("register.html", error=error)

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            db = get_db_connection()
            cur = db.cursor()

            cur.execute(
                "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                (name, email, hashed_password)
            )

            db.commit()
            cur.close()
            db.close()

            return redirect(url_for("login"))

        except Exception:
            error = "Email already exists"
            return render_template("register.html", error=error)

    return render_template("register.html", error=error)
#delete 
@app.route("/delete_history/<int:history_id>", methods=["POST"])
def delete_history(history_id):
    if "email_id" not in session:
        return redirect(url_for("login"))

    user_email = session["email_id"]
    is_admin = (user_email == "admin@gmail.com")

    db = get_db_connection()
    cur = db.cursor()

    if is_admin:
        # 🔥 Admin can delete ANY record
        cur.execute(
            "DELETE FROM scans WHERE id=%s",
            (history_id,)
        )
    else:
        # 🔐 User can delete ONLY their records
        cur.execute(
            "DELETE FROM scans WHERE id=%s AND email_id=%s",
            (history_id, user_email)
        )
    cur.execute(
        "DELETE FROM scans WHERE id=%s AND email_id=%s",
        (history_id, session["email_id"])
    )

    db.commit()
    cur.close()
    db.close()

    return redirect(url_for("history"))





# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
