import streamlit as st

def show_homepage():
    st.markdown('<h1 class="title">Welkom bij NTP AI Bot</h1>', unsafe_allow_html=True)
    left_col, right_col = st.columns(2)
    
    with left_col:
        st.write("""
        Dit is de homepage van de NTP AI Bot. Gebruik het menu aan de linkerkant om door de functies te navigeren.
        Deze applicatie helpt je bij verschillende taken zoals tekstcorrectie, voorbereidingen van inhoudelijke sessies en meer.
        """)
    
    with right_col:
        st.image("https://example.com/path_to_ai_image.jpg", use_column_width=True)
