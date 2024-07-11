import streamlit as st

def calculate_bmr(gender, weight, height, age):
    if gender == "Male":
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

def calculate_calories(bmr, activity_level):
    if activity_level == "Sedentary (little or no exercise)":
        return bmr * 1.2
    elif activity_level == "Lightly active (light exercise/sports 1-3 days/week)":
        return bmr * 1.375
    elif activity_level == "Moderately active (moderate exercise/sports 3-5 days/week)":
        return bmr * 1.55
    elif activity_level == "Very active (hard exercise/sports 6-7 days a week)":
        return bmr * 1.725
    else:
        return bmr * 1.9

# Streamlit app
st.title("Calorie Calculator")

# User input
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=0, max_value=120, value=25)
weight = st.number_input("Weight (kg)", min_value=0.0, max_value=200.0, value=70.0)
height = st.number_input("Height (cm)", min_value=0.0, max_value=250.0, value=170.0)
activity_level = st.selectbox("Activity Level", [
    "Sedentary (little or no exercise)",
    "Lightly active (light exercise/sports 1-3 days/week)",
    "Moderately active (moderate exercise/sports 3-5 days/week)",
    "Very active (hard exercise/sports 6-7 days a week)",
    "Super active (very hard exercise/sports & physical job)"
])

if st.button("Calculate"):
    bmr = calculate_bmr(gender, weight, height, age)
    calories_needed = calculate_calories(bmr, activity_level)
    st.write(f"Your BMR is: {bmr:.2f} calories/day")
    st.write(f"To maintain your current weight, you need: {calories_needed:.2f} calories/day")

# To run the app, save this code in a file (e.g., calorie_calculator.py) and run `streamlit run calorie_calculator.py` in the terminal
