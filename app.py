import streamlit as st
import pandas as pd
import joblib

# Load the model (Ensure churn_model.pkl is in the same folder)
model = joblib.load('churn_model.pkl')

st.title("📊 Customer Churn Prediction")
st.write("Adjust the inputs below to match the customer's profile.")

# 1. Create Input Widgets
col1, col2 = st.columns(2)

with col1:
    satisfaction = st.slider("Satisfaction Score (1-5)", 1, 5, 3)
    months = st.number_input("Tenure (Months)", min_value=1, value=12)
    monthly = st.number_input("Monthly Charges ($)", min_value=0.0, value=70.0)
    total_revenue = st.number_input("Total Revenue ($)", min_value=0.0, value=1000.0)
    gb_mon = st.number_input("Monthly Data Usage (GB)", min_value=0, value=20)

with col2:
    cltv = st.number_input("CLTV", min_value=0, value=4000)
    contract = st.selectbox("Contract Type", ["Month-to-Month", "One Year", "Two Year"])
    internet = st.selectbox("Internet Type", ["Fiber Optic", "DSL", "Cable", "None"])
    security = st.selectbox("Online Security", ["Yes", "No"])

# 2. Prediction Logic
if st.button("Predict"):
    data = {
        'satisfaction': [satisfaction],
        'total_revenue': [total_revenue],
        'months': [months],
        'cltv': [cltv],
        'monthly': [monthly],
        'gb_mon': [gb_mon],
        'contract_Two Year': [1 if contract == "Two Year" else 0],
        'contract_One Year': [1 if contract == "One Year" else 0],
        'internet_type_Fiber Optic': [1 if internet == "Fiber Optic" else 0],
        'security_Yes': [1 if security == "Yes" else 0]
    }
    
    features = pd.DataFrame(data)
    
    # Must match the list in the Colab cell above
    column_order = [
        'satisfaction', 'total_revenue', 'months', 'cltv', 'monthly', 
        'gb_mon', 'contract_Two Year', 'contract_One Year', 
        'internet_type_Fiber Optic', 'security_Yes'
    ]
    features = features[column_order]
    
    prediction = model.predict(features)
    prob = model.predict_proba(features)[0][1]

    if prediction[0] == 1:
        st.error(f"Prediction: Likely to CHURN (Risk: {prob:.2f})")
    else:
        st.success(f"Prediction: Likely to STAY (Risk: {prob:.2f})")
