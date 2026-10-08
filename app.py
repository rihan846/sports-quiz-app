import streamlit as st

# -----------------------------
# SPORTS QUIZ
# -----------------------------

st.set_page_config(
    page_title="Sports Quiz",
    page_icon="🏆"
)

st.title("🏆 Sports Quiz")
st.write("Test your sports knowledge!")

# Questions
questions = [
    {
        "question": "Who has won the most FIFA World Cups as a player?",
        "options": ["Lionel Messi", "Pelé", "Cristiano Ronaldo", "Diego Maradona"],
        "answer": "Pelé"
    },
    {
        "question": "Which country won the 2022 FIFA World Cup?",
        "options": ["France", "Brazil", "Argentina", "Germany"],
        "answer": "Argentina"
    },
    {
        "question": "How many players are there in a football team on the field?",
        "options": ["9", "10", "11", "12"],
        "answer": "11"
    },
    {
        "question": "Which sport is played at Wimbledon?",
        "options": ["Football", "Tennis", "Cricket", "Basketball"],
        "answer": "Tennis"
    },
    {
        "question": "How many rings are on the Olympic logo?",
        "options": ["4", "5", "6", "7"],
        "answer": "5"
    },
    {
        "question": "Which country is famous for the sport of cricket?",
        "options": ["India", "Brazil", "Spain", "Argentina"],
        "answer": "India"
    },
    {
        "question": "How many players are on a basketball team on the court?",
        "options": ["4", "5", "6", "7"],
        "answer": "5"
    },
    {
        "question": "Which sport uses a shuttlecock?",
        "options": ["Tennis", "Badminton", "Football", "Hockey"],
        "answer": "Badminton"
    },
    {
        "question": "Which country hosted the 2016 Summer Olympics?",
        "options": ["China", "Brazil", "Japan", "UK"],
        "answer": "Brazil"
    },
    {
        "question": "What is the highest score possible with one dart?",
        "options": ["50", "60", "100", "120"],
        "answer": "60"
    }
]

# -----------------------------
# Store quiz state
# -----------------------------

if "question_number" not in st.session_state:
    st.session_state.question_number = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "finished" not in st.session_state:
    st.session_state.finished = False

# -----------------------------
# Quiz
# -----------------------------

if not st.session_state.finished:

    current = st.session_state.question_number
    question = questions[current]

    # Progress
    st.progress(current / len(questions))

    st.write(
        f"### Question {current + 1} of {len(questions)}"
    )

    st.subheader(question["question"])

    answer = st.radio(
        "Choose your answer:",
        question["options"],
        key=f"question_{current}"
    )

    if st.button("Next ➡️"):

        if answer == question["answer"]:
            st.session_state.score += 1
            st.success("Correct! 🎉")
        else:
            st.error(
                f"Wrong! The correct answer is {question['answer']}."
            )

        if current + 1 < len(questions):
            st.session_state.question_number += 1
            st.rerun()
        else:
            st.session_state.finished = True
            st.rerun()

# -----------------------------
# Final Result
# -----------------------------

else:

    st.balloons()

    st.header("🎉 Quiz Completed!")

    score = st.session_state.score

    st.metric(
        "Your Score",
        f"{score} / {len(questions)}"
    )

    percentage = (score / len(questions)) * 100

    st.write(f"### Percentage: {percentage:.0f}%")

    if percentage >= 80:
        st.success("🏆 Excellent! You are a Sports Master!")
    elif percentage >= 50:
        st.info("👏 Good job! Keep improving!")
    else:
        st.warning("📚 Keep practicing and try again!")

    if st.button("🔄 Play Again"):

        st.session_state.question_number = 0
        st.session_state.score = 0
        st.session_state.finished = False

        st.rerun()