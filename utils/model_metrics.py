import streamlit as st
import joblib
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_RESULTS_PATH = (
    BASE_DIR /
    "model" /
    "model_results.pkl"
)


def model_performance():

    st.markdown("## 🤖 Model Performance")


    try:

        results = joblib.load(
            MODEL_RESULTS_PATH
        )


        col1, col2, col3, col4 = st.columns(4)


        with col1:
            st.metric(
                "🎯 Accuracy",
                f"{results['accuracy']}%"
            )


        with col2:
            st.metric(
                "Precision",
                f"{results['precision']}%"
            )


        with col3:
            st.metric(
                "Recall",
                f"{results['recall']}%"
            )


        with col4:
            st.metric(
                "F1 Score",
                f"{results['f1']}%"
            )


    except:

        st.warning(
            "Model performance file not found."
        )