
import streamlit as st
import pickle
import numpy as np

# Load the model
with open("best_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Life Expectancy Predictor")

# Input features (example set, adjust based on actual model input)
bmi = st.number_input("BMI")
gdp = st.number_input("GDP per capita")
schooling = st.number_input("Schooling (Years)")
hiv = st.number_input("HIV/AIDS prevalence")
alcohol = st.number_input("Alcohol Consumption")
percentage_expenditure = st.number_input("Health Expenditure (% of GDP)")
infant_deaths = st.number_input("Infant Deaths per 1000 births")
measles = st.number_input("Measles cases")
adult_mortality = st.number_input("Adult Mortality")
polio = st.number_input("Polio Immunization (%)")

# Ensure order matches training input
input_data = np.array([[
    adult_mortality, infant_deaths, alcohol, percentage_expenditure,
    bmi, hiv, measles, gdp, schooling, polio
]])

# Prediction
if st.button("Predict Life Expectancy"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Life Expectancy: {prediction[0]:.2f} years")
