import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    BASE_DIR /
    "model" /
    "attrition_model.pkl"
)

ENCODER_PATH = (
    BASE_DIR /
    "model" /
    "label_encoders.pkl"
)


def prediction_section():

    st.markdown("## 🤖 Attrition Prediction")


    model = joblib.load(MODEL_PATH)

    encoders = joblib.load(ENCODER_PATH)


    st.write(
        "Enter employee details to predict attrition risk."
    )


    col1, col2 = st.columns(2)


    with col1:

        age = st.number_input(
            "Age",
            18,
            60,
            30
        )


        department = st.selectbox(
            "Department",
            encoders["Department"].classes_
        )


        gender = st.selectbox(
            "Gender",
            encoders["Gender"].classes_
        )


        overtime = st.selectbox(
            "OverTime",
            encoders["OverTime"].classes_
        )


        job_level = st.number_input(
            "Job Level",
            1,
            5,
            2
        )


        income = st.number_input(
            "Monthly Income",
            1000,
            50000,
            5000
        )


    with col2:

        job_satisfaction = st.slider(
            "Job Satisfaction",
            1,
            4,
            3
        )


        environment = st.slider(
            "Environment Satisfaction",
            1,
            4,
            3
        )


        years = st.number_input(
            "Years At Company",
            0,
            40,
            5
        )


        job_role = st.selectbox(
            "Job Role",
            encoders["JobRole"].classes_
        )


        worklife = st.slider(
            "Work Life Balance",
            1,
            4,
            3
        )


        total_years = st.number_input(
            "Total Working Years",
            0,
            50,
            8
        )


    if st.button("Predict Attrition"):


        input_data = pd.DataFrame(
            {
                "Age":[age],
                "Department":[department],
                "Gender":[gender],
                "OverTime":[overtime],
                "JobLevel":[job_level],
                "MonthlyIncome":[income],
                "JobSatisfaction":[job_satisfaction],
                "EnvironmentSatisfaction":[environment],
                "YearsAtCompany":[years],
                "JobRole":[job_role],
                "WorkLifeBalance":[worklife],
                "TotalWorkingYears":[total_years]
            }
        )


        # Apply same encoding as training

        for column, encoder in encoders.items():

            if column in input_data.columns:

                input_data[column] = encoder.transform(
                    input_data[column]
                )


        prediction = model.predict(
            input_data
        )


        probability = model.predict_proba(
            input_data
        )[0][1]


        if prediction[0] == 1:
            st.error("🔴 High Attrition Risk")
            st.progress(float(probability))
            st.metric(
        "Risk Score",
        f"{probability*100:.1f}%"
    )

        else:

         st.success("🟢 Low Attrition Risk")

         st.progress(float(probability))

         st.metric(
             "Risk Score",
             f"{probability*100:.1f}%"
        )
         