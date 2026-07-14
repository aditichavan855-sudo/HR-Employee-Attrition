# 👨‍💼 HR Employee Attrition Analytics Dashboard

An interactive **HR Analytics Dashboard** built using **Streamlit, Plotly, and Machine Learning** to analyze employee attrition, identify high-risk employees, and provide actionable workforce insights.

This project combines **data visualization, predictive analytics, and business intelligence** into a single application for HR professionals and data analysts.

---

## 📸 Dashboard Preview

> *(Add screenshots here after uploading to GitHub)*

| Dashboard | Prediction | Insights |
|-----------|------------|----------|
| Dashboard Screenshot | Prediction Screenshot | Insights Screenshot |

---

# 🚀 Features

### 📊 Interactive Dashboard
- KPI Cards
- Employee Count
- Attrition Rate
- Average Age
- Average Monthly Income

### 🎛 Dynamic Filters
- Department
- Gender
- Job Role
- Business Travel
- Marital Status
- OverTime

All charts and KPIs update automatically based on selected filters.

---

### 📈 Interactive Visualizations

- Attrition Distribution
- Department Attrition
- Gender Analysis
- Overtime Analysis
- Age Distribution
- Monthly Income Distribution

Built using **Plotly** for fully interactive charts.

---

### 💡 Automated Business Insights

The dashboard automatically generates insights such as:

- Highest attrition department
- Overtime impact
- Average employee income
- Workforce distribution
- Employee turnover trends

---

### 🔥 Risk Analysis

Identify employee groups with higher attrition risk using:

- Department Analysis
- Overtime Analysis
- Satisfaction Levels
- Experience Analysis

---

### 👥 Employee Segmentation

Employees are segmented based on:

- Age
- Income
- Experience
- Job Level
- Work-Life Balance

---

### 🤖 Machine Learning Prediction

Predict whether an employee is likely to leave the organization using a trained classification model.

Input Features include:

- Age
- Department
- Gender
- Job Role
- Monthly Income
- Job Satisfaction
- Environment Satisfaction
- Job Level
- Years at Company
- Work-Life Balance
- Total Working Years
- Overtime

The application displays:

- Prediction Result
- Attrition Risk Probability

---

### 📄 Data Explorer

- View filtered dataset
- Explore employee records
- Download filtered data as CSV

---

# 🧠 Machine Learning

The project evaluates multiple machine learning models:

- Logistic Regression
- Decision Tree
- Random Forest

The best-performing model is automatically selected and saved for deployment.

Performance Metrics include:

- Accuracy
- Precision
- Recall
- F1 Score

---

# 📂 Dataset

**IBM HR Analytics Employee Attrition Dataset**

Dataset contains:

- **1470 Employees**
- **35 Features**
- Target Variable:
  - Attrition (Yes / No)

Features include:

- Age
- Gender
- Department
- Job Role
- Monthly Income
- Job Satisfaction
- Environment Satisfaction
- Work-Life Balance
- Overtime
- Years at Company
- Total Working Years

---

# 🛠 Tech Stack

### Programming

- Python

### Data Processing

- Pandas
- NumPy

### Data Visualization

- Plotly
- Streamlit

### Machine Learning

- Scikit-Learn
- Joblib

### Development

- VS Code
- Git
- GitHub

---

# 📁 Project Structure

```
HR-Employee-Attrition/
│
├── app.py
│
├── data/
│   ├── HR-Employee-Attrition.csv
│   └── clean_hr_data.csv
│
├── model/
│   ├── attrition_model.pkl
│   ├── features.pkl
│   └── label_encoders.pkl
│
├── pages/
│   ├── About.py
│
├── utils/
│   ├── charts.py
│   ├── data_loader.py
│   ├── feature_importance.py
│   ├── filters.py
│   ├── insights.py
│   ├── metrics.py
│   ├── model_performance.py
│   ├── prediction.py
│   ├── risk_analysis.py
│   ├── segmentation.py
│   └── theme.py
│
├── train.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/HR-Employee-Attrition.git
```

Go to the project directory

```bash
cd HR-Employee-Attrition
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🎯 Project Objectives

- Analyze employee attrition patterns
- Identify high-risk employee groups
- Provide HR insights through visualization
- Predict employee attrition using machine learning
- Support data-driven HR decision-making

---

# 🔮 Future Improvements

- Authentication System
- SQL Database Integration
- Explainable AI (SHAP)
- Deep Learning Models
- Email Alerts
- Cloud Deployment
- Live HR Database
- REST API Integration

---

# 👩‍💻 Developer

**Aditi Chavan**

🎓 B.Sc. Data Science Graduate

Passionate about:

- Data Analytics
- Machine Learning
- Business Intelligence
- Data Visualization
- AI Applications

---

# 📜 License

This project is developed for educational and portfolio purposes.

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

It helps support the project and motivates future improvements.