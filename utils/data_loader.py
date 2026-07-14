import pandas as pd
import streamlit as st
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


@st.cache_data
def load_default_data():
    """Load the first CSV file found in the data folder."""
    try:
        csv_files = list(DATA_DIR.glob("*.csv"))

        if not csv_files:
            st.error("❌ No CSV file found in the data folder.")
            return None

        return pd.read_csv(csv_files[0])

    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return None


@st.cache_data
def load_uploaded_data(uploaded_file):
    """Load an uploaded CSV file."""
    try:
        return pd.read_csv(uploaded_file)

    except Exception as e:
        st.error(f"Error reading uploaded file: {e}")
        return None