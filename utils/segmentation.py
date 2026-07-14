import streamlit as st


def employee_segmentation(df):

    st.markdown("## 👥 Employee Risk Segmentation")


    temp = df.copy()


    # -----------------------------
    # Risk Score
    # -----------------------------

    temp["Risk Score"] = 0


    # Overtime impact
    temp.loc[
        temp["OverTime"] == "Yes",
        "Risk Score"
    ] += 2


    # Low satisfaction
    temp.loc[
        temp["JobSatisfaction"] <= 2,
        "Risk Score"
    ] += 1


    temp.loc[
        temp["EnvironmentSatisfaction"] <= 2,
        "Risk Score"
    ] += 1


    # Low income
    income_limit = temp["MonthlyIncome"].median()

    temp.loc[
        temp["MonthlyIncome"] < income_limit,
        "Risk Score"
    ] += 1


    # New employees
    temp.loc[
        temp["YearsAtCompany"] <= 2,
        "Risk Score"
    ] += 1



    # -----------------------------
    # Risk Category
    # -----------------------------

    def classify(score):

        if score >= 4:
            return "🔴 High Risk"

        elif score >= 2:
            return "🟡 Medium Risk"

        else:
            return "🟢 Low Risk"



    temp["Risk Category"] = (
        temp["Risk Score"]
        .apply(classify)
    )


    # -----------------------------
    # Display Counts
    # -----------------------------

    col1, col2, col3 = st.columns(3)


    high = (
        temp["Risk Category"]
        .value_counts()
        .get("🔴 High Risk",0)
    )

    medium = (
        temp["Risk Category"]
        .value_counts()
        .get("🟡 Medium Risk",0)
    )

    low = (
        temp["Risk Category"]
        .value_counts()
        .get("🟢 Low Risk",0)
    )


    with col1:
        st.error(
            f"🔴 High Risk\n\n{high} Employees"
        )


    with col2:
        st.warning(
            f"🟡 Medium Risk\n\n{medium} Employees"
        )


    with col3:
        st.success(
            f"🟢 Low Risk\n\n{low} Employees"
        )


    # -----------------------------
    # Preview Table
    # -----------------------------

    st.dataframe(
        temp[
            [
                "EmployeeNumber",
                "JobRole",
                "Department",
                "OverTime",
                "Risk Category"
            ]
        ],
        use_container_width=True
    )