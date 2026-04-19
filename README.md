# 🛡️ AI vs AI Cyber Defense System

## 📌 Overview
This project simulates an adversarial cybersecurity environment where:

- An **Attacker module** generates mutated XSS and SQL Injection payloads  
- A **Defender AI model** detects malicious inputs using Machine Learning  
- The system logs attacks and supports retraining  

---

## ⚔️ AI vs AI Concept
- Attacker continuously evolves payloads using obfuscation techniques  
- Defender tries to classify them as malicious or benign  
- Some attacks are blocked, some bypass the model  

---

## 🚀 Features
- Multi-layer payload mutation engine  
- Machine learning-based detection (TF-IDF + SVM)  
- Attack simulation system  
- Logging of attack attempts  
- Retraining pipeline  
- Interactive Streamlit dashboard  

---

## 🛠️ Tech Stack
- Python  
- Scikit-learn  
- Streamlit  
- Pandas  

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt