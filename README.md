# AI Model for Phishing Detection System

## 🚀 Overview
This project is an AI-powered **Phishing Detection System** that helps identify malicious URLs and phishing emails using machine learning. It analyzes various URL features, detects suspicious patterns, and classifies them as safe or phishing attempts.

## 🔥 Features
- ✅ URL-based phishing detection
- ✅ Email phishing detection
- ✅ Machine learning model for classification
- ✅ Web interface built with Flask
- ✅ CSV-based dataset handling
- ✅ Easy-to-use API for phishing detection

## 🛠️ Tech Stack
- **Backend:** Flask (Python)
- **Machine Learning:** Scikit-learn, Pandas, NumPy
- **Frontend:** HTML, CSS, JavaScript
- **Storage:** CSV for datasets

## 📁 Project Structure
```
📦 Phishing Detector
 ┣ 📂 archive
 ┣ 📂 static
 ┣ 📂 templates
 ┣ 📜 .gitignore
 ┣ 📜 email.ipynb
 ┣ 📜 main_model.pkl
 ┣ 📜 main.ipynb
 ┣ 📜 Phishing_Email_model.pkl
 ┣ 📜 phishing_features.csv
 ┣ 📜 phishing_site_urls.csv
 ┣ 📜 predictionmain.ipynb
 ┣ 📜 server.py
```

## 🚀 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/NilanshuGarhewal/code-crushers-kurukshetra-2k25.git
cd code-crushers-kurukshetra-2k25
```
### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run the Flask Server
```bash
python server.py
```
The application should now be running at **http://127.0.0.1:5000** 🚀

## 🛠️ Usage
- Enter a URL in the input field to check if it's safe or phishing.
- Upload a suspicious email for phishing detection.

## 🤖 Model Training
To retrain the machine learning model, use the Jupyter notebooks provided (`main.ipynb`, `email.ipynb`). Modify and experiment with different algorithms to improve accuracy.

## 💡 Future Enhancements
- 🔹 Improve model accuracy with deep learning
- 🔹 Add real-time URL scanning
- 🔹 Implement a browser extension for detection

## ❤️ Contributing
Pull requests are welcome! Feel free to **fork** the repo and submit improvements.

---
**Developed by Code Crushers** 🎵💻
Team Members:
Team Leader - Khushi Gupta
Teammates - Nilanshu Garhewal, Khush Paliwal, Harshit Sharma.
