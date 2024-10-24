import streamlit as st
from OpenAI.openai_client import client  # Import OpenAI client

def show_session_preparation_page():
    st.markdown('<h1 class="title">Voorbereiding inhoudelijke sessies</h1>', unsafe_allow_html=True)
    st.write("Analyseer een aanbestedingsdocument en genereer vragen op basis van gunningscriteria.")

    # Temperature slider (directly on the page)
    temperature = st.slider('Creativiteit van het model (temperature)', 0.0, 1.0, 0.5)

    # File uploader for session preparation
    uploaded_file = st.file_uploader("Upload je PDF-bestand", type=['pdf'])

    if uploaded_file:
        st.info("Document is succesvol geüpload en wordt geanalyseerd...")
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Analyseer het document en genereer discussievragen."},
                {"role": "user", "content": "Here is the PDF content..."}  # Add document processing logic here
            ],
            temperature=temperature
        )
        # Handle the response and display generated questions (logic continues here)
        st.write(response.choices[0].message.content)
