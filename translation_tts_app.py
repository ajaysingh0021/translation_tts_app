import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import PyPDF2
import pandas as pd
import io
import os
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Text Translator & TTS",
    page_icon="🌐",
    layout="wide"
)

# Title and description
st.title("🌐 Multi-Language Text Translator & Speech Synthesizer")
st.markdown("""
Translate text into multiple languages and convert it to speech. 
Upload files or enter text directly to get started!
""")

# Sidebar for API key and settings
with st.sidebar:
    st.header("⚙️ Settings")
    
    # API Key input
    api_key = st.text_input(
        "Enter Gemini API Key",
        type="password",
        help="Get your API key from https://aistudio.google.com/api-keys"
    )
    
    if api_key:
        try:
            genai.configure(api_key=api_key)
            st.success("✅ API Key configured successfully!")
        except Exception as e:
            st.error(f"❌ Error configuring API: {str(e)}")
    
    st.markdown("---")
    st.markdown("### 📚 Instructions")
    st.markdown("""
    1. Enter your Gemini API key
    2. Choose input method (text or file)
    3. Select target language
    4. Click 'Translate' button
    5. Listen and download audio
    """)

# Language options
LANGUAGES = {
    "Hindi": "hi",
    "Bengali": "bn",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese (Simplified)": "zh-CN",
    "Arabic": "ar",
    "Turkish": "tr",
    "Dutch": "nl",
    "Polish": "pl",
    "Swedish": "sv",
    "Thai": "th",
    "Vietnamese": "vi",
    "Indonesian": "id",
    "Greek": "el"
}

def extract_text_from_pdf(pdf_file):
    """Extract text from PDF file"""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        raise Exception(f"Error reading PDF: {str(e)}")

def extract_text_from_excel(excel_file):
    """Extract text from Excel file"""
    try:
        df = pd.read_excel(excel_file)
        text = df.to_string(index=False)
        return text
    except Exception as e:
        raise Exception(f"Error reading Excel file: {str(e)}")

def extract_text_from_csv(csv_file):
    """Extract text from CSV file"""
    try:
        df = pd.read_csv(csv_file)
        text = df.to_string(index=False)
        return text
    except Exception as e:
        raise Exception(f"Error reading CSV file: {str(e)}")

def translate_text(text, target_language):
    """Translate text using Gemini API"""
    try:
        model = genai.GenerativeModel('gemini-flash-latest')        # working on 22-10-2025
        
        prompt = f"""Translate the following text to {target_language}. 
        Provide ONLY the translation without any explanations or additional text.
        
        Text to translate:
        {text}
        """
        
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        raise Exception(f"Translation error: {str(e)}")

def text_to_speech(text, language_code):
    """Convert text to speech using gTTS"""
    try:
        tts = gTTS(text=text, lang=language_code, slow=False)
        
        # Save to bytes buffer
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        
        return audio_buffer
    except Exception as e:
        raise Exception(f"Text-to-speech error: {str(e)}")

# Main application
if not api_key:
    st.warning("⚠️ Please enter your Gemini API key in the sidebar to continue.")
    st.stop()

# Input method selection
input_method = st.radio(
    "Choose input method:",
    ["Enter Text", "Upload File"],
    horizontal=True
)

input_text = ""

if input_method == "Enter Text":
    input_text = st.text_area(
        "Enter text to translate:",
        height=200,
        placeholder="Type or paste your text here..."
    )
else:
    uploaded_file = st.file_uploader(
        "Upload a file",
        type=["txt", "pdf", "csv", "xlsx", "xls"],
        help="Supported formats: TXT, PDF, CSV, Excel"
    )
    
    if uploaded_file:
        try:
            file_type = uploaded_file.name.split('.')[-1].lower()
            
            with st.spinner("📄 Reading file..."):
                if file_type == "txt":
                    input_text = uploaded_file.read().decode("utf-8")
                elif file_type == "pdf":
                    input_text = extract_text_from_pdf(uploaded_file)
                elif file_type == "csv":
                    input_text = extract_text_from_csv(uploaded_file)
                elif file_type in ["xlsx", "xls"]:
                    input_text = extract_text_from_excel(uploaded_file)
                
                st.success(f"✅ File loaded successfully! ({len(input_text)} characters)")
                
                # Show preview
                with st.expander("📝 Preview extracted text"):
                    st.text(input_text[:500] + ("..." if len(input_text) > 500 else ""))
                    
        except Exception as e:
            st.error(f"❌ Error reading file: {str(e)}")
            st.stop()

# Language selection
col1, col2 = st.columns([2, 1])

with col1:
    target_language = st.selectbox(
        "Select target language:",
        options=list(LANGUAGES.keys()),
        index=0
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    translate_button = st.button("🔄 Translate", type="primary", use_container_width=True)

# Translation and TTS processing
if translate_button:
    if not input_text:
        st.error("❌ Please enter text or upload a file before translating.")
    elif len(input_text.strip()) < 3:
        st.error("❌ Text is too short. Please enter at least 3 characters.")
    elif len(input_text) > 10000:
        st.error("❌ Text is too long. Please limit to 10,000 characters.")
    else:
        try:
            # Translation
            with st.spinner(f"🔄 Translating to {target_language}..."):
                translated_text = translate_text(input_text, target_language)
            
            st.success("✅ Translation completed!")
            
            # Display results
            st.markdown("---")
            st.subheader("📝 Translation Result")
            
            # Show original and translated text side by side
            col_orig, col_trans = st.columns(2)
            
            with col_orig:
                st.markdown("**Original Text:**")
                st.info(input_text[:500] + ("..." if len(input_text) > 500 else ""))
            
            with col_trans:
                st.markdown(f"**Translated Text ({target_language}):**")
                st.success(translated_text)
            
            # Copy button for translated text
            st.text_area(
                "Copy translated text:",
                value=translated_text,
                height=100,
                key="translated_output"
            )
            
            # Text-to-Speech
            st.markdown("---")
            st.subheader("🔊 Audio Output")
            
            with st.spinner("🎵 Generating audio..."):
                language_code = LANGUAGES[target_language]
                audio_buffer = text_to_speech(translated_text, language_code)
            
            # Audio player
            st.audio(audio_buffer, format="audio/mp3")
            
            # Download button
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"translation_{target_language}_{timestamp}.mp3"
            
            st.download_button(
                label="⬇️ Download Audio File",
                data=audio_buffer,
                file_name=filename,
                mime="audio/mp3",
                use_container_width=True
            )
            
            st.success("✅ Audio generated successfully!")
            
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.info("💡 Please check your API key and internet connection, then try again.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>Built with Streamlit | Powered by Google Gemini & gTTS | Contact: ajaysingh002@gmail.com</p>
</div>
""", unsafe_allow_html=True)