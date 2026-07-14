import streamlit as st
import pandas as pd


def calculate_metrics(df):

    # Always convert Attrition to numeric
    attrition_numeric = (
        df["Attrition"]
        .replace({
            "Yes": 1,
            "No": 0
        })
        .astype(float)
    )

    total_employees = len(df)

    attrition_rate = attrition_numeric.mean() * 100

    average_age = pd.to_numeric(
        df["Age"],
        errors="coerce"
    ).mean()

    average_income = pd.to_numeric(
        df["MonthlyIncome"],
        errors="coerce"
    ).mean()

    return {

        "total_employees": total_employees,

        "attrition_rate": round(attrition_rate, 2),

        "average_age": round(average_age, 1),

        "average_income": round(average_income, 0)

    }


def kpi_card(title, value):

    st.metric(title, value)
