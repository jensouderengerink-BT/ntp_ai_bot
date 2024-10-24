import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv  # Make sure to import this line

# Load environment variables
load_dotenv()

# Initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Function to show the mindmap generation page
def show_mindmap_page():
    st.markdown('<h1 class="title">Mindmap Generator</h1>', unsafe_allow_html=True)
    st.write("He NTP'r! Goed om te zien dat je gebruik maakt van de Mindmap generator. Upload de selectieleidraad zodat ik de mindmap kan maken terwijl je voor jezelf een kopje koffie ophaalt.")

    # Temperature slider
    temperature = st.slider('Creativiteit van het model (temperature)', 0.0, 1.0, 0.5)

    # File uploader
    uploaded_file = st.file_uploader("Upload de Selectieleidraad", type=['pdf'])

    if uploaded_file:
        st.info("Bestand geüpload. Analyse en verwerking gestart...")

        # Reading the PDF content (placeholder for actual processing)
        # Here you can add a PDF extraction logic, e.g., PyPDF2
        pdf_content = "Hier komt de inhoud van de PDF"  # Placeholder
        
        # Prompt for GPT to analyze the PDF
        prompt = f"""
        Analyseer de selectieleidraad en vul de volgende secties in met informatie uit het document.
        - '## Beoordeling: fictieve korting': geef per EMVI aspect de fictieve korting of punten.
        - '## Beoordeling: Beoordeling': geef per EMVI aspect de beoordelingscijfers met bijbehorende korting of punten.
        - '## EMVI aspecten': geef een beknopte samenvatting per aspect.
        - '## Tenderteam': laat leeg.
        - '# Central topic': vervang met de titel van de opdracht.
        - '## Onderscheidend vermogen': geef een bulletpoint lijst.
        - '## EMVI planning': neem onderdelen uit de planning en vermeld de datum.

        Te analyseren structuur:
        ```markdown
        # Central topic:
        ## EMVI planning
        ## Opdrachtgever
        ## Tenderteam
        - Directie:
        - Projectleider:
        - Uitvoerder:
        - Calculator:
        - Duurzaamheidscoördinator:
        - Planning en fasering:
        - Engineer:
        - Tenderleider:
        ## Eisen PVA / indiening
        - Opmaak:
        ## EMVI aspecten
        - Onderdelen:
        ## Beoordeling:
        - Fictieve korting:
        - Beoordeling:
        ## Vragen voor nota:
        ## Strategie plan:
        ## Bijzonderheden:
        ## Projectdoelstellingen:
        ## Activiteiten:
        ## Triggertermen:
        ## Onderscheidend vermogen:
        ## Concurrentie:
        ```
        Gebruik markdown om de secties op te maken. Als een sectie geen informatie bevat, vul dan in 'Geen informatie beschikbaar'.
        """
        
        # Call the OpenAI API to generate the mindmap content
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Je bent een expert in het genereren van mindmaps uit tenderdocumenten."},
                {"role": "user", "content": prompt + "\n\n" + pdf_content}
            ],
            temperature=temperature,
            max_tokens=3000
        )
        
        # Extract the content from the response
        mindmap_content = response.choices[0].message.content

        # Display the mindmap content as Markdown
        st.markdown("### Mindmap Output")
        st.code(mindmap_content)

        # Provide a message for copying and saving as a .MD file
        st.info("De informatie in het codeblok kun je kopiëren in kladblok en vervolgens opslaan als .MD-bestand. Dit bestand kun je tenslotte importeren in xMind.")

        # Option to download the content as a markdown file
        st.download_button(
            label="📥 Download Mindmap als .MD-bestand",
            data=mindmap_content.encode(),
            file_name="mindmap.md",
            mime="text/markdown"
        )
