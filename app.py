import streamlit as st
import joblib

# Load the model
model = joblib.load("model.pkl")

# Streamlit App Title
st.title("Fake Job Prediction App")

# Input Box for Job Description
job_description = st.text_area("Enter Job Description:", height=200)

# Button to Trigger Prediction
if st.button("Predict"):
    # Run prediction
    prediction = model.predict([job_description])
    # Display Result
    st.success(
        "This job posting is: **{}**".format("Fake" if prediction[0] == 1 else "Real")
    )
