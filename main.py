import streamlit as st

# Page configuration (must be first)
st.set_page_config(
    page_title="NTP AI Bot",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

from dotenv import load_dotenv
from openai import OpenAI
from Components.text_correction import show_text_correction_page
from Components.session_preparation import show_session_preparation_page
from Components.homepage import show_homepage
from Components.mindmap import show_mindmap_page
from Components.toetsing import show_toetsing_page
from Styling.styling import apply_custom_styling
from Authentication.auth import login_form
import os

# Get the port dynamically from Heroku
port = int(os.environ.get('PORT', 8501))  # Default to 8501 for local testing

# Run Streamlit
st._config.set_option('server.port', port)

# Load environment variables
load_dotenv()

# Initialize the OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No OpenAI API key found. Please set it as an environment variable.")

client = openai.OpenAI(api_key=api_key)

# Apply custom styling from the separate module
apply_custom_styling()

# Authentication handling
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_form()  # Show login form
else:
    # Sidebar button-based navigation
    with st.sidebar:
        st.image("https://ntp.nl/wp-content/uploads/2021/06/logo-3.svg", width=150)
        st.title("Overzicht functies")
        st.write("Gebruik de knoppen om verschillende functies te ontdekken.")

        if st.button("🏠 Home"):
            st.session_state.page = 'Home'
        if st.button("🔍 Voorbereiding inhoudelijke sessies"):
            st.session_state.page = 'Voorbereiding'
        if st.button("📊 75% en 90% toetsing"):
            st.session_state.page = 'Toetsing'
        if st.button("🧠 Mindmap maken"):
            st.session_state.page = 'Mindmap'

    # Navigation logic based on button click
    if 'page' not in st.session_state or st.session_state.page == 'Home':
        show_homepage()
    elif st.session_state.page == 'Voorbereiding':
        show_session_preparation_page()
    elif st.session_state.page == 'Toetsing':
        show_toetsing_page()
    elif st.session_state.page == 'Mindmap':
        show_mindmap_page()

# Footer
st.markdown(
    """
    <div class="footer">
        Gerealiseerd door <a href="https://bluetree.nl" target="_blank">BlueTree</a>
    </div>
    """, unsafe_allow_html=True
)
