import streamlit as st


def sidebar_filters(df):
    """
    Creates interactive sidebar filters and returns filtered dataframe.
    """

    st.sidebar.header("🎛 Dashboard Filters")

    department = st.sidebar.multiselect(
        "Department",
        options=sorted(df["Department"].unique()),
        default=sorted(df["Department"].unique())
    )

    gender = st.sidebar.multiselect(
        "Gender",
        options=sorted(df["Gender"].unique()),
        default=sorted(df["Gender"].unique())
    )

    job_role = st.sidebar.multiselect(
        "Job Role",
        options=sorted(df["JobRole"].unique()),
        default=sorted(df["JobRole"].unique())
    )

    overtime = st.sidebar.multiselect(
        "OverTime",
        options=sorted(df["OverTime"].unique()),
        default=sorted(df["OverTime"].unique())
    )

    marital = st.sidebar.multiselect(
        "Marital Status",
        options=sorted(df["MaritalStatus"].unique()),
        default=sorted(df["MaritalStatus"].unique())
    )

    travel = st.sidebar.multiselect(
        "Business Travel",
        options=sorted(df["BusinessTravel"].unique()),
        default=sorted(df["BusinessTravel"].unique())
    )


    # Apply filters
    filtered_df = df[
        (df["Department"].isin(department)) &
        (df["Gender"].isin(gender)) &
        (df["JobRole"].isin(job_role)) &
        (df["OverTime"].isin(overtime)) &
        (df["MaritalStatus"].isin(marital)) &
        (df["BusinessTravel"].isin(travel))
    ]


    # Employee count display
    st.sidebar.write(
        f"👥 Employees Selected: {len(filtered_df)}"
    )


    return filtered_df