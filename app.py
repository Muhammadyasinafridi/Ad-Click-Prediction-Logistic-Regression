import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load assets
model = joblib.load('ad_click_model.pkl')
scaler = joblib.load('ad_click_scaler.pkl')
feature_names = joblib.load('feature_names.pkl')

# Page Styling
st.set_page_config(
    page_title="Ad Click Prediction",
    page_icon="📈",
    layout="centered"
)


st.title("📊 E-Commerce Ad Click Predictor")
st.markdown("Predict Ad Click Probability ")
st.markdown("---")

# Input Form
st.subheader("📊 Session Information")
time_spent = st.slider("Time Spent on Site (Seconds)", 0, 1200, 200)
pages_visited = st.number_input("Pages Visited during session", min_value=0, max_value=50, value=10)

st.subheader("🏷️ Advertisement Category")
ad_type_selected = st.selectbox("Select Ad Type", ["Adult", "Commercial", "Educational", "Recruitment"])

if st.button("Predict", type="primary"):
 
    input_dict = {
        'TimeSpentSeconds': time_spent,
        'PagesVisited': pages_visited
    }
    
   
    for col in feature_names:
        if col.startswith('AdType_'):
            category_name = col.replace('AdType_', '')
            input_dict[col] = 1 if ad_type_selected == category_name else 0
            
    # Format to DataFrame
    input_df = pd.DataFrame([input_dict])[feature_names]
    
    # Predict
    scaled_data = scaler.transform(input_df)
    prediction = model.predict(scaled_data)[0]
    probability = model.predict_proba(scaled_data)[0][1] * 100
    
    # Show  UI
    st.markdown("---")
    if prediction == 1:
        st.error(f" **High Click Potential!** Probable click conversion detected ({probability:.2f}% confidence).")
    else:
        st.success(f" **Low Click Potential.** High likelihood user will skip this advertisement ({100 - probability:.2f}% confidence).")
