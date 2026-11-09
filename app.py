import streamlit as st

# Coefficients exported from the trained Multiple Linear Regression model
INTERCEPT = -11194.194349936239
COEF = {
    "age": 248.2107202247045,
    "sex": 101.54205399029436,      # 1 = female
    "bmi": 318.70144095235065,
    "children": 533.0099887986984,
    "smoker": 23077.7645928681,     # 1 = yes
}
REGION = {
    "northeast": 0.0,
    "northwest": -391.7614547836083,
    "southeast": -838.9196157269689,
    "southwest": -659.1397515529709,
}

st.title("Medical Insurance Cost Predictor")
st.write("Enter your details to get an estimated yearly insurance cost.")

age = st.slider("Age", 18, 64, 30)
bmi = st.slider("BMI", 15.0, 50.0, 25.0)
children = st.selectbox("Children", [0, 1, 2, 3, 4, 5])
smoker = st.selectbox("Smoker", ["no", "yes"])
sex = st.selectbox("Gender", ["male", "female"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

if st.button("Predict Cost"):
    pred = (
        INTERCEPT
        + COEF["age"] * age
        + COEF["bmi"] * bmi
        + COEF["children"] * children
        + (COEF["smoker"] if smoker == "yes" else 0)
        + (COEF["sex"] if sex == "female" else 0)
        + REGION[region]
    )
    st.success(f"Estimated insurance cost: ${max(pred, 0):,.2f}")
    st.caption("Educational estimate from a Linear Regression model, not a real insurance quote.")
