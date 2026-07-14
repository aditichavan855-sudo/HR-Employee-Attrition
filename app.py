import streamlit as st

from utils.theme import apply_theme
from utils.data_loader import load_default_data, load_uploaded_data
from utils.metrics import calculate_metrics, kpi_card

from utils.charts import (
    attrition_pie,
    department_chart,
    gender_chart,
    overtime_chart,
    age_distribution,
    income_distribution,
)

from utils.filters import sidebar_filters
from utils.insights import generate_insights
from utils.risk_analysis import risk_analysis
from utils.segmentation import employee_segmentation
from utils.prediction import prediction_section
from utils.model_metrics import model_performance

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="HR Employee Attrition Dashboard",
    page_icon="👨‍💼",
    layout="wide"
)


# =====================================================
# APPLY THEME
# =====================================================

apply_theme()
PLOTLY_CONFIG = {
    "displaylogo": False,
    "toImageButtonOptions": {
        "format": "png"
    }
}

# =====================================================
# HEADER
# =====================================================

st.markdown(
    """
    <div class="dashboard-title">
        👨‍💼 HR Employee Attrition Dashboard
    </div>

    <div class="dashboard-subtitle">
        AI Powered Workforce Analytics
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


# =====================================================
# SIDEBAR DATA UPLOAD
# =====================================================

st.sidebar.header("📂 Dataset")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV",
    type=["csv"]
)



# =====================================================
# LOAD DATA
# =====================================================

if uploaded_file is not None:

    df = load_uploaded_data(uploaded_file)

    st.sidebar.success(
        "Custom dataset loaded."
    )

else:

    df = load_default_data()

    st.sidebar.info(
        "Using default HR dataset."
    )


# =====================================================
# SIDEBAR FILTERS
# =====================================================

filtered_df = sidebar_filters(df)

if filtered_df.empty:
    st.warning("⚠️ No employees match the selected filters.")

    st.stop()

st.sidebar.divider()

st.sidebar.markdown("### 📊 Dashboard Summary")

st.sidebar.metric(
    "Employees",
    len(filtered_df)
)

st.sidebar.metric(
    "Departments",
    filtered_df["Department"].nunique()
)

st.sidebar.metric(
    "Job Roles",
    filtered_df["JobRole"].nunique()
)

# =====================================================
# CALCULATE METRICS
# =====================================================

metrics = calculate_metrics(filtered_df)

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📊 Overview",
        "🔥 Risk Analysis",
        "🤖 Prediction",
        "📄 Data Explorer"
    ]
)
with tab1:

    # =====================================================
    # KPI SECTION
    # =====================================================
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"🏢 Departments: {filtered_df['Department'].nunique()}")
    with col2:
        st.info(f"💼 Job Roles: {filtered_df['JobRole'].nunique()}")
    with col3:
        st.info(f"👥 Current Records: {len(filtered_df)}")
    col1, col2, col3, col4 = st.columns(4)


    with col1:
        kpi_card(
            "👥 Total Employees",
            metrics["total_employees"]
        )


    with col2:
        kpi_card(
            "🚪 Attrition Rate",
            f"{metrics['attrition_rate']}%"
        )


    with col3:
        kpi_card(
            "🎂 Average Age",
            metrics["average_age"]
        )


    with col4:
        kpi_card(
            "💰 Avg Income",
            f"₹{metrics['average_income']:,.0f}"
        )


    # =====================================================
    # INSIGHTS
    # =====================================================

    st.divider()
    with st.expander(
        "📌 Key Insights",
        expanded=True
        ):
        generate_insights(filtered_df)


    # =====================================================
    # ATTRITION ANALYSIS
    # =====================================================

    st.markdown(
        "## 📈 Attrition Analysis"
    )


    col1, col2 = st.columns(2)


    with col1:
        st.plotly_chart(
            attrition_pie(filtered_df),
            use_container_width=True,
            config=PLOTLY_CONFIG
        )


    with col2:
        st.plotly_chart(
            department_chart(filtered_df),
            use_container_width=True,
            config=PLOTLY_CONFIG
        )


    # =====================================================
    # EMPLOYEE ANALYSIS
    # =====================================================

    st.markdown(
        "## 👥 Employee Analysis"
    )


    col1, col2 = st.columns(2)


    with col1:
        st.plotly_chart(
            gender_chart(filtered_df),
            use_container_width=True,
            config=PLOTLY_CONFIG
        )


    with col2:
        st.plotly_chart(
            overtime_chart(filtered_df),
            use_container_width=True,
            config=PLOTLY_CONFIG
        )


    # =====================================================
    # DISTRIBUTION ANALYSIS
    # =====================================================

    st.markdown(
        "## 📊 Distribution Analysis"
    )


    col1, col2 = st.columns(2)


    with col1:
        st.plotly_chart(
            age_distribution(filtered_df),
            use_container_width=True,
            config=PLOTLY_CONFIG
        )


    with col2:
        st.plotly_chart(
            income_distribution(filtered_df),
            use_container_width=True,
            config=PLOTLY_CONFIG
        )



# =====================================================
# RISK ANALYSIS TAB
# =====================================================

with tab2:

    risk_analysis(filtered_df)

    employee_segmentation(filtered_df)



# =====================================================
# PREDICTION TAB
# =====================================================

with tab3:

    model_performance()

    st.divider()

    prediction_section()


# =====================================================
# DATA EXPLORER TAB
# =====================================================

with tab4:

    st.markdown("## 📄 Dataset Preview")

    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Filtered Dataset",
        data=csv,
        file_name="filtered_hr_data.csv",
        mime="text/csv",
        use_container_width=True,
    )

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

    st.success(
        f"Showing {len(filtered_df)} employees after applying filters."
    )

st.divider()

st.markdown(
    """
    <div style='text-align:center;
                color:#9CA3AF;
                font-size:14px;
                padding:10px;'>

    👨‍💼 HR Employee Attrition Dashboard <br>
    Developed by <b>Aditi Chavan</b> | Data Science Portfolio Project

    </div>
    """,
    unsafe_allow_html=True
)
