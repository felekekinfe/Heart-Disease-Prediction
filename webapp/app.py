import streamlit as st
import pandas as pd
import pickle

# Title and description
st.title("Heart Disease Prediction App")
st.write("Enter the patient details below to predict the likelihood of heart disease.")

# User input fields
age = st.number_input("Age (years)", min_value=1, max_value=120, value=30)
sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.selectbox("Chest Pain Type", options=[0, 1, 2, 3], format_func=lambda x: [
    "Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"][x])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=200, value=120)
chol = st.number_input("Serum Cholesterol (mg/dL)", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", options=[0, 1], format_func=lambda x: "False" if x == 0 else "True")
restecg = st.selectbox("Resting Electrocardiographic Results", options=[0, 1, 2], format_func=lambda x: [
    "Normal", "ST-T wave abnormality", "Left Ventricular Hypertrophy"][x])
thalach = st.number_input("Maximum Heart Rate Achieved (bpm)", min_value=60, max_value=220, value=150)
exang = st.selectbox("Exercise-Induced Angina", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
oldpeak = st.number_input("ST Depression (oldpeak)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
slope = st.selectbox("Slope of Peak Exercise ST Segment", options=[0, 1, 2], format_func=lambda x: [
    "Upsloping", "Flat", "Downsloping"][x])
ca = st.number_input("Number of Major Vessels (0-3)", min_value=0, max_value=3, value=0)
thal = st.selectbox("Thalassemia", options=[0, 1, 2], format_func=lambda x: [
    "Normal", "Fixed Defect", "Reversible Defect"][x])


if st.button("Predict"):

    try:
        with open('/home/cs/Desktop/heart-disease-project/heart-disease-project/heart-disease-classification/model/_model.pkl', 'rb') as file:
            model = pickle.load(file)
        

        input_data = pd.DataFrame({
            "age": [age],
            "sex": [sex],
            "cp": [cp],
            "trestbps": [trestbps],
            "chol": [chol],
            "fbs": [fbs],
            "restecg": [restecg],
            "thalach": [thalach],
            "exang": [exang],
            "oldpeak": [oldpeak],
            "slope": [slope],
            "ca": [ca],
            "thal": [thal]
        })

        
        prediction = model.predict(input_data)[0]  

        
        if prediction == 1:
            st.error("The model predicts that the patient has heart disease.")
        else:
            st.success("The model predicts that the patient does not have heart disease.")

    except FileNotFoundError:
        st.error("Model file not found. Please ensure 'heart_disease_model.pkl' is in the same directory.")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
