# AI-Phishing Email Detector

An AI-powered web application that detects phishing emails and provides a risk score. Users can scan emails, view scan history, and monitor results in a user-friendly dashboard. Admins can see all user scans and statistics.

---

## Features

### User Features
- **Scan Emails:** Users can paste email content and get a phishing/safe prediction with a risk score.
- **Scan History:** View the history of all scanned emails.
- **Profile Panel:** Check total scans, phishing and safe counts, and logout.
- **Authentication:** Secure login and registration with password hashing.

### Admin Features
- **Dashboard:** View total scans, phishing, and safe counts across all users.
- **History:** See scan history for all users.

---

## Technologies Used
- **Backend:** Python, Flask, MySQL
- **Machine Learning:** Scikit-learn (model and vectorizer for email classification)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** MySQL

---

## Project Structure
AI-Phishing_Email_Detector/
│
├── app.py # Main Flask application
├── db.py # Database connection
├── model.pkl # Trained ML model
├── vectorizer.pkl # TF-IDF vectorizer
├── requirements.txt # Python dependencies
├── templates/ # HTML templates
│ ├── dashboard.html
│ ├── history.html
│ ├── home.html
│ ├── login.html
│ ├── navbar.html
│ ├── scan.html
│ └── register.html
├── static/ # CSS, JS, images
│ ├── css/
│ └── javascript/
├── dataset.csv/ # Sample emails(from kaggle)
├── phishing.db # MySQL database
└── README.md

## How It Works

1. User submits email content
2. Text is processed using TF-IDF
3. Machine Learning model predicts phishing or safe
4. Result and risk score are displayed
5. Scan details are stored for history tracking

## Note
This project is intended for educational and demonstration purposes.
