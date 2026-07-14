import streamlit as st


def risk_analysis(df):

    st.markdown("## 🔥 Attrition Risk Analysis")


    # Convert Attrition
    temp = df.copy()

    temp["Attrition_Value"] = (
        temp["Attrition"]
        .map({
            "Yes": 1,
            "No": 0
        })
    )


    # -----------------------------
    # Overtime Risk
    # -----------------------------

    overtime_rate = (
        temp.groupby("OverTime")["Attrition_Value"]
        .mean()
        * 100
    )


    if "Yes" in overtime_rate.index:

        st.warning(
            f"⏰ Overtime employees attrition rate: "
            f"**{overtime_rate['Yes']:.1f}%**"
        )


    # -----------------------------
    # Department Risk
    # -----------------------------

    dept = (
        temp.groupby("Department")["Attrition_Value"]
        .mean()
        .sort_values(
            ascending=False
        )
    )


    st.error(
        f"🏢 Highest Risk Department: "
        f"**{dept.index[0]} "
        f"({dept.iloc[0]*100:.1f}%)**"
    )


    # -----------------------------
    # Job Satisfaction
    # -----------------------------

    satisfaction = (
        temp.groupby("JobSatisfaction")["Attrition_Value"]
        .mean()
        .sort_values(
            ascending=False
        )
    )


    st.info(
        f"😟 Highest Risk Satisfaction Level: "
        f"Level {satisfaction.index[0]}"
    )