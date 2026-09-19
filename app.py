import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Heart Risk Predictor", page_icon="❤️")

st.title("❤️ Heart Disease Risk Predictor")
st.write("Clinical Decision Support Prototype | Accuracy: 83.61%")

# Load model
with open('heart_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.header("Enter Patient Details:")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 20, 90, 50)
    sex = st.selectbox("Gender", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type", [0,1,2,3], help="0=Typical, 1=Atypical, 2=Non-anginal, 3=Asymptomatic")
    trestbps = st.number_input("Resting Blood Pressure", 90, 200, 120)
    chol = st.number_input("Cholesterol mg/dl", 100, 600, 200)
    fbs = st.selectbox("Fasting Blood Sugar >120 mg/dl", [0,1])

with col2:
    restecg = st.selectbox("Rest ECG", [0,1,2])
    thalach = st.number_input("Max Heart Rate Achieved", 70, 220, 150)
    exang = st.selectbox("Exercise Induced Angina", [0,1])
    oldpeak = st.number_input("Oldpeak - ST depression", 0.0, 6.0, 1.0)
    slope = st.selectbox("Slope of ST segment", [0,1,2])
    ca = st.selectbox("No. of Major Vessels (0-3)", [0,1,2,3])
    thal = st.selectbox("Thalassemia", [0,1,2,3])

sex_val = 1 if sex == "Male" else 0

if st.button("🔍 PREDICT RISK"):
    columns = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']
    input_data = pd.DataFrame([[age, sex_val, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]], columns=columns)

    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1] * 100

    st.divider()
    if prediction == 1:
        st.error(f"🔴 HIGH RISK: {prob:.1f}% probability of Heart Disease")
        st.write("**Clinical Action:** Recommend ECG, 2D Echo, Lipid Profile, Immediate cardiology referral.")
        st.progress(int(prob))
    else:
        st.success(f"🟢 LOW RISK: {prob:.1f}% probability")
        st.write("**Clinical Action:** Routine follow-up, diet control, regular exercise.")
        st.progress(int(prob))

st.caption("Disclaimer: For educational/research only. Not a replacement for doctor diagnosis. Trained on 303 Cleveland Clinic patients.")