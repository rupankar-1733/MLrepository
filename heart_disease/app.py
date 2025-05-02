import streamlit as st
import joblib
import numpy as np

# Set page configuration
st.set_page_config(page_title="Heart Disease Predictor", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #dbeafe, #f0f9ff);
        background-attachment: fixed;
        font-family: 'Segoe UI', sans-serif;
    }

    .block-container {
        backdrop-filter: blur(8px);
        background-color: rgba(255, 255, 255, 0.65);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }

    h1, h2, h3 {
        color: #0f172a;
    }

    .stButton>button {
        background-color: #2563eb;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 1.5em;
    }

    .stButton>button:hover {
        background-color: #1e40af;
        color: white;
    }

    .stSelectbox label, .stSlider label {
        font-weight: bold;
    }

    .stSidebar {
        background-color: #f0f9ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load trained model
model = joblib.load("heart_disease/best_rf_model.pkl")


# Title
st.markdown("<h1 style='text-align: center;'>❤️ Heart Disease Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>An interactive ML app to assess heart disease risk</p>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("ℹ️ About")
    st.write("""
        This app uses a trained Random Forest model to predict the likelihood of heart disease.
        Enter patient health data and click Predict to see the result.
    """)
    st.write("Developed with 🧠 Machine Learning & Streamlit.")

# Input form layout
st.subheader("📝 Enter Patient Information:")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider("Age", 29, 77, 54)
    sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
    cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3], help="0: Typical Angina, 1: Atypical, 2: Non-anginal, 3: Asymptomatic")
    trestbps = st.slider("Resting Blood Pressure (mm Hg)", 90, 200, 130)
    chol = st.slider("Cholesterol (mg/dl)", 100, 600, 245)

with col2:
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
    restecg = st.selectbox("Resting ECG", [0, 1, 2], help="0: Normal, 1: ST-T abnormality, 2: Probable/Definite LVH")
    thalach = st.slider("Max Heart Rate Achieved", 70, 210, 150)
    exang = st.selectbox("Exercise Induced Angina", [0, 1])
    oldpeak = st.slider("ST Depression", 0.0, 6.2, 1.0, step=0.1)

with col3:
    slope = st.selectbox("Slope of ST Segment", [0, 1, 2], help="0: Upsloping, 1: Flat, 2: Downsloping")
    ca = st.selectbox("Number of Major Vessels Colored (ca)", [0, 1, 2, 3, 4])
    thal = st.selectbox("Thalassemia", [0, 1, 2, 3], help="1: Fixed Defect, 2: Normal, 3: Reversible Defect")

# Collect input into numpy array
features = np.array([[
    age, sex, cp, trestbps, chol, fbs, restecg,
    thalach, exang, oldpeak, slope, ca, thal
]])

# Prediction
st.markdown("---")
if st.button("🔍 Predict Heart Disease Risk"):
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    st.markdown("### 🧪 Prediction Result:")
    if prediction == 1:
        st.error(f"🚨 High Risk Detected! (Probability: {probability:.2%})")
        st.markdown("💡 Please consult a medical professional for further evaluation.")
    else:
        st.success(f"✅ Low Risk Detected (Probability: {probability:.2%})")
        st.markdown("🎉 Keep up the great heart health!")

# Footer
st.markdown("---")
st.markdown("<small style='text-align: center; display: block;'>Built with ❤️ by Your Name</small>", unsafe_allow_html=True)
