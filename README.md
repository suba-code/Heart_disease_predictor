# ❤️ Heart Disease Risk Predictor - 85.25% Accuracy

**Clinical Decision Support Prototype | Live Demo:** https://heartdiseasepredictor-suba8055.streamlit.app/

A machine learning web app that predicts heart disease risk from 13 clinical parameters. Built for portfolio and clinical learning.

### 🚀 Live Demo
👉 **https://heartdiseasepredictor-suba8055.streamlit.app/**

### 📊 Model Performance
- **Accuracy: 85.25%**
- **Dataset:** 303 patients - Cleveland Clinic Foundation (UCI)
- **Algorithm:** Random Forest Classifier
- **Features:** 13 (age, sex, chest pain, BP, cholesterol, ECG, etc.)

### 🛠️ Tech Stack
- Python, Scikit-learn, Pandas
- Streamlit (UI)
- Trained model: `heart_model.pkl`

### 💡 Features
- 3-column clinical UI with medical terminology (Typical Angina vs 0,1,2)
- Real-time risk % with progress bar
- Color-coded triage: 🔴 HIGH RISK / 🟢 LOW RISK
- Actionable recommendations

### 📁 Project Structure
- app.py - Streamlit app (main UI)
- train.py - Model training script
- heart.csv - Cleveland Clinic dataset (303 patients)
- heart_model.pkl - Trained RandomForest model (85.25%)
- requirements.txt - Dependencies
- README.md - Documentation
