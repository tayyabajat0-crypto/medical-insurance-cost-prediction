import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

st.title("Medical Insurance Cost Predictor")
st.write("Enter your details to get an estimated yearly insurance cost.")

age = st.slider("Age", 18, 64, 30)
bmi = st.slider("BMI", 15.0, 50.0, 25.0)
children = st.selectbox("Children", [0, 1, 2, 3, 4, 5])
smoker = st.selectbox("Smoker", ["no", "yes"])
sex = st.selectbox("Gender", ["male", "female"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

if st.button("Predict Cost"):
    row = {c: 0 for c in columns}
    row["age"] = age
    row["bmi"] = bmi
    row["children"] = children
    row["smoker"] = 1 if smoker == "yes" else 0
    row["sex"] = 1 if sex == "female" else 0
    if "region_" + region in row:
        row["region_" + region] = 1
    pred = model.predict(pd.DataFrame([row])[columns])[0]
    st.success(f"Estimated insurance cost: ${max(pred, 0):,.2f}")
