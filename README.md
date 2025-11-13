# Phishing URL Detector (ML) 🕵️‍♀️

A Python machine learning project that classifies URLs as **safe** or **phishing** using feature extraction and supervised ML models.  
Designed for educational purposes, cybersecurity research, and learning about phishing detection techniques.

---

## 🔍 Overview

The **Phishing URL Detector** system works by:

- Extracting meaningful features from URLs:
  - URL length and structure
  - Special characters like `@` and `-`
  - HTTPS presence
  - Number of subdirectories and digits
  - Common phishing keywords or suspicious patterns
- Using a **machine learning model** (Random Forest by default) trained on labeled URL datasets to predict phishing or safe URLs.
- Providing a **CLI interface** for single URL or batch file predictions.
- Saving and loading models for repeated use.

> ⚠️ **Important:** This tool is intended for educational and authorized testing only. Unauthorized scanning or classification may be illegal.

---

## 🛠 Features

- URL feature extraction for ML classification
- Train and save ML models
- Predict phishing/safe status for single or multiple URLs
- Save predictions in CSV or JSON format
- CLI interface with intuitive commands
- Modular design for easy extension

---

## 📁 Repository Structure

phishing-url-detector/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── examples/
│ └── sample_urls.txt
├── src/
│ └── pud/
│ ├── init.py
│ ├── cli.py
│ ├── feature_extraction.py
│ ├── model.py
│ ├── train.py
│ └── utils.py
└── tests/
├── test_feature_extraction.py
├── test_model.py
└── test_utils.py

yaml
Copy code

---

## ⚡ Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/phishing-url-detector.git
cd phishing-url-detector
Create a virtual environment and install dependencies:

bash
Copy code
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

🚀 Usage
Train a Model
bash
Copy code
python -m src.pud.train --input examples/sample_urls.txt --model-output models/phishing_model.joblib
Predict Single URL
bash
Copy code
python -m src.pud.cli --url "http://example.com" --model models/phishing_model.joblib
Predict Batch of URLs
bash
Copy code
python -m src.pud.cli --input examples/sample_urls.txt --model models/phishing_model.joblib --output predictions.csv

🧪 Testing
Run tests using pytest:

bash
Copy code
pytest -q
Lint code using ruff:

bash
Copy code
ruff check src tests

🤝 Contributing

Fork the repository and create a feature branch: feature/<name>.
Write tests for your changes.
Follow conventional commits:
feat: New feature
fix: Bug fix
docs: Documentation
chore: Non-functional changes
Open a Pull Request (PR) with a detailed description of your changes.
See CONTRIBUTING.md for more details.

📜 License
This project is licensed under the MIT License. See the LICENSE file for full details.

📞 Contact
Created by Mahad Zulfiqar.
Open a GitHub issue for questions, feedback, or support.
