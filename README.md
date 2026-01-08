🛡️ AI Phishing Email Detector
📌 Overview

AI Phishing Email Detector is a machine learning–based web application that helps users identify whether an email is Phishing or Safe.
The system analyzes email content using Natural Language Processing (NLP) and provides a risk score along with the prediction.

This project aims to improve cybersecurity awareness and protect users from online scams.

❗ Problem Statement

Phishing emails are one of the most common cyber threats today.
Many users unknowingly fall victim to fake emails that steal sensitive information such as passwords, bank details, and personal data.

Existing solutions are either:

Too complex for normal users

Not transparent about risk

Limited in real-time interaction

💡 Proposed Solution

This project provides a user-friendly AI-powered web platform where users can:

Paste email content

Instantly detect phishing emails

View risk scores

Track scan history securely

The system uses machine learning classification to identify suspicious patterns in email text.

🧠 Technologies Used

Python

Flask (Backend Web Framework)

Machine Learning (Scikit-learn)

TF-IDF Vectorization

MySQL (Database)

HTML, CSS, JavaScript

⚙️ Features

User Registration & Login

AI-based Email Scanning

Phishing / Safe Prediction

Risk Score Generation

Scan History Tracking

Admin & User Dashboards

Secure Session Management

📁 Project Structure
AI-Phishing_Email_Detector/
│
├── app.py
├── db.py
├── ml_model.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── scan.html
│   ├── history.html
│   └── navbar.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── dataset/

🚀 How It Works

User registers and logs in

Email content is submitted for scanning

Text is vectorized using TF-IDF

ML model predicts Phishing or Safe

Results and risk score are stored

User can view scan history

🎯 Use Cases

Students & professionals

Email security awareness

Educational demonstrations

Cybersecurity projects

Imagine Cup submissions

🔮 Future Enhancements

Real-time email integration

Deep learning models

Browser extension

Multi-language support

Cloud deployment

📝 Note

This project is developed for educational and demonstration purposes.
