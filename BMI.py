import streamlit as st

# Define the webpage title
st.title("BMI Calculator")

# Define the input controls for the user
name = st.text_input("Name")
gender = st.radio("Gender", ["Male", "Female", "Other"])
age = st.number_input("Age", min_value=0, max_value=150, step=1)
address = st.text_area("Address")
hobbies = st.multiselect("Hobbies", ["Reading", "Sports", "Music", "Traveling", "Cooking"])
weight = st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, step=0.1)
height = st.number_input("Height (cm)", min_value=0, max_value=300, step=1)

# Define a function to calculate the BMI
def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

# Define a button to calculate the BMI
if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    st.write("Your BMI is:", bmi)

# Define a button to reset the input controls
if st.button("Reset"):
    name = ""
    gender = ""
    age = 0
    address = ""
    hobbies = []
    weight = 0.0
    height = 0
