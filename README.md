# 🛡️ AI vs AI Cyber Defense System

## 📌 Overview

This project simulates an adversarial cybersecurity environment where artificial intelligence systems compete in a cyber defense scenario. An attacker AI generates sophisticated mutated payloads for XSS (Cross-Site Scripting) and SQL Injection attacks, while a defender AI model, trained on machine learning techniques, attempts to detect and block these malicious inputs. The system includes logging, retraining capabilities, and an interactive dashboard for monitoring and analysis.

## ⚔️ AI vs AI Concept

In this adversarial setup:
- The **Attacker** continuously evolves attack payloads using advanced obfuscation and mutation techniques to bypass detection.
- The **Defender** employs machine learning models (TF-IDF vectorization with SVM classification) to classify inputs as malicious or benign.
- The system demonstrates real-world cyber defense dynamics where attackers adapt, and defenders must retrain to maintain effectiveness.

---

## 🚀 Features

- **Multi-layer Payload Mutation Engine**: Generates complex, obfuscated XSS and SQL injection payloads.
- **Machine Learning-Based Detection**: Utilizes TF-IDF feature extraction and Support Vector Machine (SVM) for classification.
- **Attack Simulation System**: Simulates real-time attacks and defenses.
- **Comprehensive Logging**: Tracks all attack attempts and outcomes in CSV format.
- **Retraining Pipeline**: Allows the defender model to be retrained with new data.
- **Interactive Streamlit Dashboard**: Web-based interface for visualization and control.

---

## 🛠️ Tech Stack

- **Python**: Core programming language.
- **Scikit-learn**: For machine learning models and preprocessing.
- **Streamlit**: For building the interactive web dashboard.
- **Pandas**: For data manipulation and analysis.
- **Joblib**: For model serialization.

---

## 📁 Project Structure

```
ai_vs_ai_cyber_defense/
├── main.py                 # Main entry point for the simulation
├── app/
│   └── app.py              # Streamlit dashboard application
├── attacker/
│   └── mutator.py          # Payload mutation and attack generation
├── defender/
│   ├── train_model.py      # Model training script
│   └── retrain_model.py    # Model retraining script
├── data/
│   └── dataset.csv         # Training and testing dataset
├── logs/
│   └── attack_log.csv      # Log of attack attempts
├── models/
│   └── defender_model.joblib # Trained defender model
└── README.md               # Project documentation
```

---

## ▶️ Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai_vs_ai_cyber_defense.git
cd ai_vs_ai_cyber_defense
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Prepare the Dataset
Ensure `data/dataset.csv` contains labeled data for training the defender model.

### 4. Train the Initial Model (if needed)
```bash
python defender/train_model.py
```

---

## 🚀 Usage

### Running the Simulation
Execute the main simulation script:
```bash
python main.py
```

### Launching the Dashboard
Start the Streamlit web interface:
```bash
streamlit run app/app.py
```

### Retraining the Model
To retrain the defender with new data:
```bash
python defender/retrain_model.py
```

### Viewing Logs
Check `logs/attack_log.csv` for detailed attack logs.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

For questions or suggestions, please open an issue on GitHub or contact the maintainers.