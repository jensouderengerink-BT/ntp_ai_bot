import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def show_toetsing_page():
    st.markdown('<h1 class="title">75% en 90% Toetsing</h1>', unsafe_allow_html=True)
    st.write("Deze functie helpt je om documenten te vergelijken met inschrijfleidraad of vragen te verwerken.")

    # Step 1: User selects a conversational opening
    option = st.radio(
        "Kies een optie om verder te gaan:",
        ["Kun je het plan vergelijken met de inschrijfleidraad?", 
         "Zijn de gestelde vragen goed verwerkt?"]
    )

    if option == "Kun je het plan vergelijken met de inschrijfleidraad?":
        # Step 2: Ask the user to upload both documents
        st.write("Upload zowel de inschrijfleidraad als het concept document dat je wilt laten controleren.")
        inschrijfleidraad = st.file_uploader("Upload inschrijfleidraad (PDF)", type=['pdf'])
        plan_van_aanpak = st.file_uploader("Upload plan van aanpak (PDF)", type=['pdf'])

        if inschrijfleidraad and plan_van_aanpak:
            st.write("Inschrijfleidraad en plan van aanpak geüpload.")
            
            # Step 3: Compare the documents and estimate success rate
            st.info("Vergelijken van documenten...")
            # Here, you will process both files and call OpenAI's GPT for comparison
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Vergelijk het plan van aanpak met de inschrijfleidraad."},
                    {"role": "user", "content": f"Plan van aanpak en inschrijfleidraad zijn beide geüpload. Doe een analyse."}
                ],
                max_tokens=3000,
                temperature=0.5
            )
            success_rate = 70  # This is a placeholder value, replace it with actual calculation
            st.write(f"Geschatte slagingskans: {success_rate}%")

            # Step 4: Provide feedback on recognized criteria and goals, with suggestions
            st.write("Gunningscriteria en doelstellingen worden gecontroleerd...")
            feedback_response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Controleer of de gunningscriteria en doelstellingen zijn herkend en geef verbeteringen."},
                    {"role": "user", "content": f"Hier zijn de documenten: {inschrijfleidraad.name}, {plan_van_aanpak.name}"}
                ],
                max_tokens=3000,
                temperature=0.5
            )
            st.write(feedback_response.choices[0].message.content)

    elif option == "Zijn de gestelde vragen goed verwerkt?":
        # Step 2: Ask the user to upload the Plan van Aanpak, inschrijfleidraad, and the questions
        st.write("Upload zowel het Plan van aanpak, de inschrijfleidraad als de vragen.")
        plan_van_aanpak = st.file_uploader("Upload plan van aanpak (PDF)", type=['pdf'])
        inschrijfleidraad = st.file_uploader("Upload inschrijfleidraad (PDF)", type=['pdf'])
        vragen_document = st.file_uploader("Upload vragen (PDF)", type=['pdf'])

        if plan_van_aanpak and inschrijfleidraad and vragen_document:
            st.write("Alle documenten zijn geüpload.")
            
            # Step 3: Check if the questions are properly processed and estimate success rate
            st.info("Beantwoorde vragen worden vergeleken...")
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Controleer of de vragen goed zijn verwerkt in het plan van aanpak."},
                    {"role": "user", "content": f"Hier zijn de documenten: {vragen_document.name}, {inschrijfleidraad.name}, {plan_van_aanpak.name}"}
                ],
                max_tokens=3000,
                temperature=0.5
            )
            success_rate = 85  # This is a placeholder value, replace it with actual calculation
            st.write(f"Geschatte slagingskans: {success_rate}%")
