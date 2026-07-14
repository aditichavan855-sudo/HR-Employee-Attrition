import streamlit as st


def apply_theme():
    st.set_page_config(
        page_title="HR Employee Attrition Dashboard",
        page_icon="👨‍💼",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.markdown(
        """
        <style>

        /* ==========================================
           PAGE SPACING
        ========================================== */

        .block-container{
            padding-top:2rem;
            padding-bottom:2rem;
            padding-left:2rem;
            padding-right:2rem;
        }

        /* ==========================================
           DASHBOARD TITLE
        ========================================== */

        .dashboard-title{
            font-size:42px;
            font-weight:700;
            color:#2563EB;
            margin-bottom:0;
        }

        .dashboard-subtitle{
            font-size:18px;
            color:#64748B;
            margin-top:0;
            margin-bottom:20px;
        }

        /* ==========================================
           DATAFRAME
        ========================================== */

        div[data-testid="stDataFrame"]{
            border-radius:15px;
            overflow:hidden;
            border:1px solid rgba(0,0,0,0.08);
        }

        /* ==========================================
           BUTTONS
        ========================================== */

        .stButton > button{
            width:100%;
            border-radius:10px;
            font-weight:600;
        }

        /* ==========================================
           DOWNLOAD BUTTON
        ========================================== */

        .stDownloadButton > button{
            width:100%;
            border-radius:10px;
            font-weight:600;
        }

        /* ==========================================
           FILE UPLOADER
        ========================================== */

        div[data-testid="stFileUploader"]{
            border-radius:12px;
        }

        /* ==========================================
           SIDEBAR
        ========================================== */

        section[data-testid="stSidebar"]{
            border-right:1px solid rgba(128,128,128,.15);
        }

        /* ==========================================
           HR
        ========================================== */

        hr{
            margin-top:20px;
            margin-bottom:20px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )