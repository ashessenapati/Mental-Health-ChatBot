import streamlit as st
import pandas as pd

# Function to calculate the mental health score
def calculate_score(answers):
    score = sum(answers.values())
    return score

# Function to generate a report based on the mental health score
def generate_report(score):
    if score <= 10:
        report = "You seem to be doing well mentally. Keep up the good work!"
    elif 10 < score <= 20:
        report = "You might be experiencing some mild stress. Consider some relaxation techniques."
    else:
        report = "It seems like you're under significant stress. Please consider seeking professional help."
    return report

# Main function to run the Streamlit app
def main():
    st.title("Mental Health Bot")

    # Questions to ask the user
    questions = {
        "Q1. How often do you feel stressed? (1 - Rarely, 2 - Sometimes, 3 - Often)": 0,
        "Q2. Do you have trouble sleeping? (1 - No, 2 - Sometimes, 3 - Often)": 0,
        "Q3. How would you rate your overall mood? (1 - Good, 2 - Neutral, 3 - Bad)": 0,
        "Q4. Do you feel overwhelmed by your daily tasks? (1 - No, 2 - Sometimes, 3 - Often)": 0
    }

    answers = {}

    # Display questions and get user responses
    for question, _ in questions.items():
        answer = st.radio(question, options=[1, 2, 3])
        answers[question] = answer

    # Calculate mental health score and generate report
    score = calculate_score(answers)
    report = generate_report(score)

    # Display the mental health score and report
    st.subheader("Mental Health Report")
    st.write("Your mental health score is:", score)
    st.write(report)

if __name__ == "__main__":
    main()
