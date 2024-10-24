import streamlit as st
from PyPDF2 import PdfReader
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No OpenAI API key found. Please set it in the .env file.")
openai.api_key = api_key

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    pdf_reader = PdfReader(uploaded_file)
    extracted_text = ""
    for page in pdf_reader.pages:
        extracted_text += page.extract_text()
    return extracted_text

# Function to show the mindmap generation page
def show_mindmap_page():
    st.markdown('<h1 class="title">Mindmap Generator</h1>', unsafe_allow_html=True)
    st.write("He NTP'r! Goed om te zien dat je gebruik maakt van de Mindmap generator. Upload de selectieleidraad zodat ik de mindmap kan maken terwijl je voor jezelf een kopje koffie ophaalt.")

    # Temperature slider for creativity
    temperature = st.slider('Creativiteit van het model (temperature)', 0.0, 1.0, 0.5)

    # File uploader for PDF
    uploaded_file = st.file_uploader("Upload de Selectieleidraad", type=['pdf'])

    if uploaded_file:
        st.info("Bestand geüpload. Analyse en verwerking gestart...")

        # Extract text from the uploaded PDF
        pdf_content = extract_text_from_pdf(uploaded_file)

        if not pdf_content:
            st.error("Kon geen tekst uit het PDF-bestand extraheren. Probeer een ander bestand.")
            return

        # Define the prompt with instructions for GPT
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
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Je bent een expert in het genereren van mindmaps uit tenderdocumenten."},
                {"role": "user", "content": prompt + "\n\n" + pdf_content}
            ],
            temperature=temperature,
            max_tokens=3000
        )
        
        # Extract the content from the response
        mindmap_content = response['choices'][0]['message']['content']

        # Display the mindmap content as Markdown
        st.markdown("### Mindmap Output")
        st.code(mindmap_content, language='markdown')

        # Provide a message for copying and saving as a .MD file
        st.info("De informatie in het codeblok kun je kopiëren in kladblok en vervolgens opslaan als .MD-bestand. Dit bestand kun je tenslotte importeren in xMind.")

        # Option to download the content as a markdown file
        st.download_button(
            label="📥 Download Mindmap als .MD-bestand",
            data=mindmap_content.encode(),
            file_name="mindmap.md",
            mime="text/markdown"
        )
