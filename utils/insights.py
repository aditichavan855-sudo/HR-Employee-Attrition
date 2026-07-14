import streamlit as st
import pandas as pd


def generate_insights(df):

    st.markdown("## 📌 Key Insights")

    # Create a copy
    insight_df = df.copy()

    # Always convert Attrition to numeric
    insight_df["Attrition_Value"] = (
        insight_df["Attrition"]
        .eq("Yes")
        .astype(int)
    )

    # =====================================================
    # Highest Attrition Department
    # =====================================================

    dept_attrition = (
        insight_df
        .groupby("Department")["Attrition_Value"]
        .mean()
        .sort_values(ascending=False)
    )

    highest_department = dept_attrition.index[0]
    highest_rate = dept_attrition.iloc[0] * 100

    st.info(
        f"🔥 Highest Attrition Department: "
        f"**{highest_department} ({highest_rate:.1f}%)**"
    )

    # =====================================================
    # Overtime Insight
    # =====================================================

    overtime_attrition = (
        insight_df
        .groupby("OverTime")["Attrition_Value"]
        .mean()
    )

    if "Yes" in overtime_attrition.index:

        overtime_rate = overtime_attrition["Yes"] * 100

        st.warning(
            f"⏰ Overtime Attrition Rate: "
            f"**{overtime_rate:.1f}%**"
        )

    # =====================================================
    # Salary Insight
    # =====================================================

    avg_income = pd.to_numeric(
        insight_df["MonthlyIncome"],
        errors="coerce"
    ).mean()

    st.success(
        f"💰 Average Monthly Income: "
        f"**₹{avg_income:,.0f}**"
    )

    # =====================================================
    # Workforce Insight
    # =====================================================

    largest_department = (
        insight_df["Department"]
        .value_counts()
        .idxmax()
    )

    employee_count = (
        insight_df["Department"]
        .value_counts()
        .max()
    )

    st.write(
        f"👥 Largest Workforce: "
        f"**{largest_department} "
        f"({employee_count} employees)**"
    )
