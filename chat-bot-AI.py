import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# GPT prompt to generate personalized mental health report
gpt_prompt = """
### Mental Health Report

Based on your responses, here is your personalized mental health report:

1. **Stress Level**: {stress_level}
2. **Sleep Quality**: {sleep_quality}
3. **Overall Mood**: {mood}
4. **Feeling of Overwhelm**: {overwhelm}
5. **Physical Activity Level**: {physical_activity}
6. **Support System**: {support_system}
7. **Breaks During Work or Study**: {breaks}
8. **Work-Life Balance Satisfaction**: {work_life_balance}

Based on this assessment, it seems like you're {assessment}.

If you're experiencing any significant distress or need further support, please consider seeking help from a mental health professional.
"""

# Function to generate personalized mental health report using GPT
def generate_report(answers):
    # Construct GPT prompt
    prompt = gpt_prompt.format(**answers)
    
    # Generate report using GPT
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5
    )
    
    # Extract generated report from GPT response
    generated_report = response.choices[0].text.strip()
    
    return generated_report

# Main function to run the Streamlit app
def main():
    st.title("Mental Health Bot")
    st.markdown(
        """
        Welcome to the Mental Health Bot! This application aims to provide you with insights into your mental well-being.
        Please answer the following questions honestly to receive your personalized mental health report.
        """
    )

    questions = {
        "Stress Level": ["Rarely", "Sometimes", "Often", "Almost always"],
        "Sleep Quality": ["Never", "Sometimes", "Often", "Almost always"],
        "Overall Mood": ["Very good", "Good", "Neutral", "Bad", "Very bad"],
        "Feeling of Overwhelm": ["Never", "Rarely", "Sometimes", "Often", "Almost always"],
        "Physical Activity Level": ["Daily", "A few times a week", "Rarely", "Never"],
        "Support System": ["Yes", "No", "Sometimes"],
        "Breaks During Work or Study": ["Regularly", "Sometimes", "Rarely", "Never"],
        "Work-Life Balance Satisfaction": ["Very satisfied", "Satisfied", "Neutral", "Unsatisfied", "Very unsatisfied"]
    }

    answers = {}

    for question, options in questions.items():
        answer = st.selectbox(question, options, key=question)
        answers[question] = answer

    # Generate personalized mental health report
    generated_report = generate_report(answers)

    st.subheader("Mental Health Report")
    st.write(generated_report)

if __name__ == "__main__":
    main()
