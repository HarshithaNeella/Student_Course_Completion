import streamlit as st
import pickle
import numpy as np
import pandas as pd
import base64

with open("best_students_dtree.pkl","rb") as f:
    best_dt=pickle.load(f)


#st.bg_image("asstes\Students image.jpg.jpg")

def set_bg_image(img_path):
    with open(img_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# CALL background function
set_bg_image(r"Stdunt img2.jpg")

st.title("Students Course Complete Prediction")

fee=st.selectbox("Fee_Paid",["Yes","No"])
time_spent=int(st.number_input("Time_Spent_Hours",value=0.00))
video=int(st.number_input("Video_Completion_Rate",value=0.00))
quiz=int(st.number_input("Quiz_Score_Avg",value=0.00))
payment=int(st.number_input("Payment_Amount",value=0))


if st.button("Completed (Yes/No)"):

    # RULE 1: Fee not paid
    if fee == "No" or payment == 0:
        st.markdown(
            "<h2 style='color:#8B0000; background:#FFCCCC; padding:12px; border-radius:10px;'>"
            "Prediction: NOT Completed</h2>",
            unsafe_allow_html=True
        )

    # RULE 2: Engagement thresholds
    elif video < 70 or quiz < 70:
        st.markdown(
            "<h2 style='color:#8B0000; background:#FFCCCC; padding:12px; border-radius:10px;'>"
            "Prediction: NOT Completed</h2>",
            unsafe_allow_html=True
        )

    else:
        # ML MODEL PREDICTION (only if rules pass)
        input_df = pd.DataFrame([{
            "Fee_Paid": fee,
            "Time_Spent_Hours": time_spent,
            "Video_Completion_Rate": video,
            "Quiz_Score_Avg": quiz,
            "Payment_Amount": payment
        }])

        result = best_dt.predict(input_df)[0]

        if result in [1, "Yes", "Completed"]:
            st.markdown(
                "<h2 style='color:#006400; background:#90EE90; padding:12px; border-radius:10px;'>"
                "Prediction: Completed</h2>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<h2 style='color:#8B0000; background:#FFCCCC; padding:12px; border-radius:10px;'>"
                "Prediction: NOT Completed</h2>",
                unsafe_allow_html=True
            )

    



