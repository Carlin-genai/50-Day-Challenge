import streamlit as st
from googletrans import Translator

# Initialize translator
translator = Translator()

# Supported languages (you can expand this list)
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Tamil": "ta",
    "Telugu": "te",
    "Arabic": "ar",
    "Chinese (Simplified)": "zh-cn",
    "Japanese": "ja"
}

# Streamlit UI
st.title("🌍 Reverse Words & Translate Sentences")
st.markdown("Enter a sentence, reverse the words, and translate to different languages!")

# Input language
input_lang = st.selectbox("Select Input Language", list(languages.keys()))

# Output language
output_lang = st.selectbox("Select Output Language for Translation", list(languages.keys()))

# Input sentence
sentence = st.text_input("Enter your sentence:")

if sentence:
    # Translate input to English for processing (if not already English)
    translated_input = translator.translate(sentence, src=languages[input_lang], dest='en').text

    # Reverse each word individually
    reversed_words = ' '.join([word[::-1] for word in translated_input.split()])

    # Translate both original and reversed sentence to selected output language
    translated_original = translator.translate(translated_input, src='en', dest=languages[output_lang]).text
    translated_reversed = translator.translate(reversed_words, src='en', dest=languages[output_lang]).text

    st.markdown("### 🔁 Reversed Words:")
    st.write(reversed_words)

    st.markdown("### 🌐 Translations")
    st.write(f"**Original in {output_lang}**: {translated_original}")
    st.write(f"**Reversed in {output_lang}**: {translated_reversed}")
