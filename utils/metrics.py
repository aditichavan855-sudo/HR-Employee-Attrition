import streamlit as st


def calculate_metrics(df):

    # Convert Attrition text to numeric
    if df["Attrition"].dtype == "object":

        attrition_numeric = (
            df["Attrition"]
            .map({
                "Yes": 1,
                "No": 0
            })
        )

    else:
        attrition_numeric = df["Attrition"]


    total_employees = len(df)


    attrition_rate = (
        attrition_numeric.mean() * 100
    )


    average_age = (
        df["Age"].mean()
    )


    average_income = (
        df["MonthlyIncome"].mean()
    )


    return {

        "total_employees": total_employees,

        "attrition_rate": round(
            attrition_rate, 2
        ),

        "average_age": round(
            average_age, 1
        ),

        "average_income": round(
            average_income, 0
        )

    }



def kpi_card(title, value):

    st.metric(
        title,
        value
    )