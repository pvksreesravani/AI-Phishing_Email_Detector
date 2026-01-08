# 🛡️ AI Phishing Email Detector

## 📌 Overview
AI Phishing Email Detector is a machine learning–based web application that helps users identify whether an email is **Phishing** or **Safe**. The system analyzes email content using **Natural Language Processing (NLP)** and provides a **risk score** along with the prediction.

This project focuses on improving cybersecurity awareness and protecting users from phishing attacks.

---

## ❗ Problem Statement
Phishing emails are one of the most common cyber threats today. Many users unknowingly fall victim to fake emails that steal sensitive information such as passwords, bank details, and personal data.

Existing solutions are often complex, non-transparent, or not user-friendly for common users.

---

## 💡 Proposed Solution
This project provides a simple and user-friendly **AI-powered web platform** where users can:
- Paste email content
- Instantly detect phishing emails
- View risk scores
- Track scan history securely

The system uses **machine learning classification** to identify suspicious patterns in email text.

---

## 🧠 Technologies Used
- Python
- Flask
- Machine Learning (Scikit-learn)
- TF-IDF Vectorization
- MySQL
- HTML, CSS, JavaScript

---

## ⚙️ Features
- User Registration & Login
- AI-based Email Scanning
- Phishing / Safe Prediction
- Risk Score Generation
- Scan History Tracking
- Admin & User Dashboards
- Secure Session Management

---

## 📁 Project Structure
```AI-Phishing_Email_Detector/
├──app.py
├──db.py
├── ml_model.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
│
├── dataset/
│ └── dataset.csv
│
├── templates/
│ ├── home.html
│ ├── login.html
│ ├── register.html
│ ├── dashboard.html
│ ├── scan.html
│ ├── history.html
│ └── navbar.html
│
├── static/
│ ├── css/
│ │ ├── style.css
│ │ └── logo.png
│ ├── js/
│ │ ├── dashboard.js
│ │ └── scan.js
│
└── .gitignore

```

## 🚀 How It Works
1. User registers and logs in
2. Email content is submitted for scanning
3. Text is vectorized using TF-IDF
4. Machine learning model predicts **Phishing** or **Safe**
5. Results and risk score are stored in the database
6. User can view scan history

---

## 🎯 Use Cases
- Email security awareness
- Educational demonstrations
- Cybersecurity projects
- Student and academic use
- Imagine Cup submissions

---

## 🔮 Future Enhancements
- Real-time email integration
- Advanced deep learning models
- Browser extension support
- Multi-language support
- Cloud deployment

---

## 📝 Note
This project is developed for educational and demonstration purposes.
