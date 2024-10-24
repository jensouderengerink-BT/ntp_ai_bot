import streamlit as st

def apply_custom_styling():
    st.markdown(
        """
        <style>
        /* Global settings */
        body {
            background-color: #F4F4F4;
        }

        /* Sidebar customization */
        .css-1lcbmhc { 
            background-color: #F5C401 !important; /* Yellow sidebar */
        }

        /* Button styling */
        .stButton>button {
            background-color: #018A98 !important;
            color: white !important;
            font-size: 18px !important;
            border-radius: 8px !important;
            width: 100%;
            height: 50px !important;
            margin-bottom: 10px !important;
        }

        .stButton>button:hover {
            background-color: #016E78 !important;
            border: 2px solid #F5C401 !important; /* Active button border */
        }

        .stButton:focus>button {
            border: 2px solid #F5C401 !important; /* Active button border */
        }

        /* Header text */
        .title {
            font-family: 'Heebo', sans-serif;
            font-size: 42px;
            text-transform: uppercase;
            color: #018A98;
            text-align: left;
            margin-bottom: 20px;
        }

        /* Footer customization */
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f5f5f5;
            text-align: center;
            padding: 10px;
            font-size: 12px;
            color: #666;
        }
        </style>
        """, unsafe_allow_html=True
    )
