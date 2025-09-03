#pip install streamlit torch transformers

import streamlit as st
from transformers import pipeline

# Load the sentiment analysis pipeline
nlp_pipeline = pipeline("text-generation")

def main():
    st.title("Mental Health Bot")

    st.markdown("""
    Welcome to the Mental Health Bot! This application aims to provide you with support and insights regarding your mental well-being.
    Please answer the following questions honestly to receive personalized feedback.
    """)

    questions = [
        "How often do you feel stressed?",
        "Do you have trouble sleeping?",
        "How would you rate your overall mood?",
        "Do you feel overwhelmed by your daily tasks?",
        "How often do you engage in physical activity?",
        "Do you have a support system to talk to when you're feeling down?",
        "How often do you take breaks during work or study?",
        "Are you satisfied with your work-life balance?"
    ]

    answers = {}

    for question in questions:
        answer = st.selectbox(question, options=["Rarely", "Sometimes", "Often", "Almost always"])
        answers[question] = answer

    # Generate mental health report
    report = generate_report(answers)

    # Display mental health report
    st.subheader("Mental Health Report")
    st.write(report)

def generate_report(answers):
    response = nlp_pipeline(" ".join(answers.values()), max_length=150, do_sample=False)
    return response[0]['generated_text']

if __name__ == "__main__":
    main()
