import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Heart Risk Predictor", page_icon="❤️", layout="wide")

st.caption("Model Accuracy: 85.25% | Trained on 303 patients - Cleveland Clinic Foundation")
st.title("❤️ Heart Disease Risk Predictor")
st.markdown("**Clinical Decision Support Prototype | Accuracy: 85.25% | Model: Random Forest**")
st.divider()

# Load model
with open('heart_model.pkl', 'rb') as f:
    model = pickle.load(f)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Patient Demographics")
    age = st.slider("Age", 20, 90, 50, help="Patient age in years")
    sex = st.selectbox("Sex", ["Female", "Male"])
    sex_val = 0 if sex == "Female" else 1

    st.subheader("Vitals")
    trestbps = st.slider("Resting BP (mm Hg)", 90, 200, 120)
    chol = st.slider("Cholesterol (mg/dl)", 100, 600, 200)
    fbs = st.selectbox("Fasting Blood Sugar >120 mg/dl?", ["No", "Yes"])
    fbs_val = 1 if fbs == "Yes" else 0

with col2:
    st.subheader("Cardiac Symptoms")
    cp_options = {0:"Typical Angina", 1:"Atypical Angina", 2:"Non-Anginal Pain", 3:"Asymptomatic"}
    cp = st.selectbox("Chest Pain Type", options=list(cp_options.keys()), format_func=lambda x: f"{x} - {cp_options[x]}")

    exang = st.selectbox("Exercise Induced Angina?", ["No", "Yes"])
    exang_val = 1 if exang == "Yes" else 0
    oldpeak = st.slider("ST Depression (oldpeak)", 0.0, 6.0, 1.0, 0.1, help="Exercise induced ST depression")

with col3:
    st.subheader("ECG & Imaging")
    restecg_options = {0:"Normal", 1:"ST-T Abnormality", 2:"LV Hypertrophy"}
    restecg = st.selectbox("Rest ECG", options=list(restecg_options.keys()), format_func=lambda x: f"{x} - {restecg_options[x]}")

    thalach = st.slider("Max Heart Rate Achieved", 60, 220, 150)

    slope_options = {0:"Upsloping", 1:"Flat", 2:"Downsloping"}
    slope = st.selectbox("ST Slope", options=list(slope_options.keys()), format_func=lambda x: slope_options[x])

    ca = st.selectbox("Major Vessels (0-4) colored by fluoroscopy", [0,1,2,3,4])
    thal_options = {0:"Unknown", 1:"Normal", 2:"Fixed Defect", 3:"Reversible Defect"}
    thal = st.selectbox("Thalassemia", options=list(thal_options.keys()), format_func=lambda x: thal_options[x])

st.divider()

if st.button("🔍 Predict Heart Disease Risk", use_container_width=True, type="primary"):
    input_data = pd.DataFrame([[age, sex_val, cp, trestbps, chol, fbs_val, restecg, thalach, exang_val, oldpeak, slope, ca, thal]],
                              columns=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal'])
    pred = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1] * 100

    st.subheader(f"Predicted Risk: {prob:.1f}%")
    st.progress(int(prob))

    if pred == 1:
        st.error(f"### 🔴 HIGH RISK: {prob:.1f}%")
        st.write("**Recommendation:** Urgent cardiology consultation. Suggested: 12-lead ECG, 2D Echo, Troponin, lipid profile. Lifestyle: Low sodium, exercise as advised.")
    else:
        st.success(f"### 🟢 LOW RISK: {prob:.1f}%")
        st.write("**Recommendation:** Routine follow-up. Maintain healthy diet, regular exercise, annual cardiac screening. Recheck BP and lipids in 6 months.")

st.sidebar.info("This is a prototype for educational purposes only. Not for actual medical diagnosis. Consult a doctor.")