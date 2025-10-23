# 🌐 Multi-Language Text Translator & Speech Synthesizer

A powerful web application built with Streamlit that translates text into 20+ languages using Google's Gemini API and converts translations into natural-sounding speech.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.29.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- 🔄 **Multi-Language Translation** - Support for 20+ languages including Spanish, French, German, Japanese, Chinese, Arabic, Hindi, and more
- 🔊 **Text-to-Speech Conversion** - Generate natural-sounding audio from translated text
- 📁 **Multiple Input Formats** - Direct text input or file upload (TXT, PDF, CSV, Excel)
- ⬇️ **Audio Download** - Save generated speech as MP3 files
- 🎨 **User-Friendly Interface** - Clean, intuitive design with real-time feedback
- ⚡ **Fast Processing** - Efficient translation and audio generation
- 🛡️ **Error Handling** - Comprehensive validation and user-friendly error messages

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get it here](https://makersuite.google.com/app/apikey))
- Internet connection

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ajaysingh0021/translation_tts_app.git
   cd translation_tts_app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the app**
   - Open your browser and navigate to `http://localhost:8501`
   - Enter your Gemini API key in the sidebar
   - Start translating!

## 📋 Usage

### Basic Workflow

1. **Enter API Key** - Paste your Gemini API key in the sidebar
2. **Choose Input Method** - Type text directly or upload a file
3. **Select Language** - Choose from 20+ supported languages
4. **Translate** - Click the translate button
5. **Listen & Download** - Play the audio and download as MP3

### Supported Languages

| Language | Code | Language | Code |
|----------|------|----------|------|
| Spanish | es | Japanese | ja |
| French | fr | Korean | ko |
| German | de | Chinese | zh-CN |
| Italian | it | Arabic | ar |
| Portuguese | pt | Hindi | hi |
| Russian | ru | Bengali | bn |
| Turkish | tr | Thai | th |
| Dutch | nl | Vietnamese | vi |
| Polish | pl | Indonesian | id |
| Swedish | sv | Greek | el |

### Supported File Formats

- **TXT** - Plain text files
- **PDF** - Portable Document Format
- **CSV** - Comma-separated values
- **Excel** - .xlsx and .xls files

## 🛠️ Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web application framework
- **[Google Gemini API](https://ai.google.dev/)** - AI-powered translation
- **[gTTS](https://gtts.readthedocs.io/)** - Google Text-to-Speech
- **[PyPDF2](https://pypdf2.readthedocs.io/)** - PDF text extraction
- **[Pandas](https://pandas.pydata.org/)** - Data processing for CSV/Excel

## 📦 Project Structure

```
translation_tts_app/
│
├── translation_tts_app.py     # Main application file
├── docs/		       # Folder with documents
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── DOCUMENTATION.md           # Detailed technical documentation
├── .gitignore                 # Git ignore file
└── test_translation_upload_feature.txt     # Test file to check upload feature

```

## 🔧 Configuration

### API Key Setup

1. Visit [Google AI Studio](https://aistudio.google.com/app/api-keys)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy and paste the key into the app's sidebar

### Environment Variables (Optional)

For production deployment, you can set the API key as an environment variable:

```bash
export GEMINI_API_KEY="your_api_key_here"
```

## 📝 Example Usage

### Example 1: Translate a Document
```python
1. Upload a PDF document
2. Select "Spanish" as target language
3. Click translate
4. Download audio for pronunciation practice
```

### Example 2: Quick Translation
```python
1. Type: "Hello, how are you today?"
2. Select "French"
3. Get: "Bonjour, comment allez-vous aujourd'hui?"
4. Listen to the pronunciation
```

## ⚠️ Limitations

- Maximum 10,000 characters per translation
- Requires active internet connection
- Subject to Gemini API rate limits
- Audio quality depends on gTTS service
- Large PDF files (>10MB) may take longer to process

## 🐛 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Invalid API Key | Verify key is correct, check for extra spaces |
| Translation not working | Check internet connection and API quota |
| Audio not playing | Check browser audio settings |
| File upload failing | Verify file format and size |

For more detailed troubleshooting, see [DOCUMENTATION.md](DOCUMENTATION.md)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Gemini API for powerful translation capabilities
- gTTS for text-to-speech conversion
- Streamlit for the amazing web framework
- All contributors and users of this project

## 📧 Contact

Ajay - ajaysingh002@gmail.com

Project Link: [https://github.com/ajaysingh0021/translation_tts_app](https://github.com/ajaysingh0021/translation_tts_app)

