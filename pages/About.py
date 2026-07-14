import streamlit as st
from utils.theme import apply_theme

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

apply_theme()

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="dashboard-title">
    ℹ️ About This Project
</div>

<div class="dashboard-subtitle">
    HR Employee Attrition Analytics & Machine Learning Dashboard
</div>
""", unsafe_allow_html=True)

st.divider()

# =====================================================
# PROJECT OVERVIEW
# =====================================================

st.markdown("## 🎯 Project Overview")

st.info("""
This dashboard helps HR professionals analyze employee attrition using
interactive visualizations, business insights, and machine learning.

It enables organizations to identify high-risk employees, understand
attrition trends, and make data-driven workforce decisions.
""")

# =====================================================
# PROJECT HIGHLIGHTS
# =====================================================

st.markdown("## ✨ Key Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
### 📊 Analytics

- Interactive KPI Cards
- Dynamic Filters
- Attrition Dashboard
- Distribution Charts
- Employee Analysis
""")

with col2:
    st.success("""
### 🤖 Machine Learning

- Attrition Prediction
- Risk Probability
- Feature Importance
- Model Performance
- Employee Risk Detection
""")

with col3:
    st.success("""
### 💡 Business Insights

- Automated Insights
- Risk Analysis
- Employee Segmentation
- Data Explorer
- Download Filtered Data
""")

st.divider()

# =====================================================
# DATASET
# =====================================================

st.markdown("## 📂 Dataset Information")

col1, col2 = st.columns(2)

with col1:

    st.metric("Employees", "1,470")
    st.metric("Features", "35")
    st.metric("Target Variable", "Attrition")

with col2:

    st.write("""
The project uses the **IBM HR Employee Attrition Dataset**, a widely
used dataset for HR analytics and employee turnover prediction.

The dataset includes demographic information, employee satisfaction,
income, overtime, work-life balance, department details, and much more.
""")

st.divider()

# =====================================================
# TECH STACK
# =====================================================

st.markdown("## 🛠 Tech Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:
    st.info("""
### 🐍 Python

- Pandas
- NumPy
""")

with tech2:
    st.info("""
### 📈 Visualization

- Plotly
- Streamlit
""")

with tech3:
    st.info("""
### 🤖 Machine Learning

- Scikit-Learn
- Joblib
""")

with tech4:
    st.info("""
### ⚙️ Development

- VS Code
- GitHub
""")

st.divider()

# =====================================================
# PROJECT WORKFLOW
# =====================================================

st.markdown("## 🚀 Workflow")

st.markdown("""
1️⃣ Load HR Dataset

⬇️

2️⃣ Clean & Prepare Data

⬇️

3️⃣ Interactive Dashboard & Filtering

⬇️

4️⃣ Generate Business Insights

⬇️

5️⃣ Predict Employee Attrition

⬇️

6️⃣ Support HR Decision Making
""")

st.divider()

# =====================================================
# DEVELOPER
# =====================================================

st.markdown("## 👩‍💻 Developer")

dev1, dev2 = st.columns([1, 2])

with dev1:
    st.markdown("# 👩")

with dev2:

    st.markdown("### Aditi Chavan")

    st.write("""
**B.Sc. Data Science Graduate**

Passionate about Data Analytics, Machine Learning,
Business Intelligence, and Interactive Dashboard Development.

This project demonstrates practical applications of:

- Data Analysis
- Data Visualization
- Predictive Analytics
- HR Analytics
- Machine Learning
""")

st.divider()

# =====================================================
# FUTURE IMPROVEMENTS
# =====================================================

st.markdown("## 🔮 Future Enhancements")

future1, future2 = st.columns(2)

with future1:
    st.success("""
- User Authentication
- SQL Database Integration
- Live HR Dashboard
- Cloud Deployment
- Explainable AI
""")

with future2:
    st.success("""
- Employee Recommendation System
- Deep Learning Model
- Automated Reports
- Email Alerts
- Mobile Responsive Dashboard
""")

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.markdown(
    """
    <div style="text-align:center; padding:25px;">
        <h4>HR Employee Attrition Analytics Dashboard</h4>
        <p>Built with ❤️ using Streamlit, Plotly & Scikit-Learn</p>
        <p>© 2026 Aditi Chavan</p>
    </div>
    """,
    unsafe_allow_html=True
)