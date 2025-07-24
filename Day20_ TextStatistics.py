import streamlit as st
import string
import re
from collections import Counter
from textblob import TextBlob

# Helper Functions
def count_words(text):
    return len(text.split())

def count_sentences(text):
    return len(re.findall(r'[.!?]+', text))

def count_characters(text):
    return len(text)

def avg_word_length(text):
    words = text.split()
    return round(sum(len(word) for word in words) / len(words), 2) if words else 0

def reading_time(text, wpm=200):
    words = count_words(text)
    return round(words / wpm, 2)

def most_common_words(text, n=5):
    words = [w.strip(string.punctuation).lower() for w in text.split()]
    freq = Counter(words)
    return freq.most_common(n)

def highlight_sentences(text):
    sentences = re.split(r'(?<=[.!?]) +', text)
    colors = ["#f4cccc", "#d9ead3", "#d0e0e3", "#fff2cc", "#cfe2f3", "#ead1dc"]
    html = ""
    for i, sentence in enumerate(sentences):
        color = colors[i % len(colors)]
        html += f"<div style='background-color:{color}; padding:5px; margin:5px; border-radius:5px'>{sentence}</div>"
    return html

def letter_frequency(text):
    letters = [char.lower() for char in text if char.isalpha()]
    return Counter(letters)

def sentiment_analysis(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "😊 Positive"
    elif polarity < -0.1:
        return "😠 Negative"
    else:
        return "😐 Neutral"

# App Config
st.set_page_config(page_title="TextScope Analyzer 📊", layout="centered")
st.title("📊 TextScope Analyzer")
st.markdown("Analyze your paragraph with live insights, color-coded sentences, and fun stats!")

# Input
text = st.text_area("✍️ Paste or type your paragraph below:", height=200)

if text:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📝 Words", count_words(text))

    with col2:
        st.metric("📌 Sentences", count_sentences(text))

    with col3:
        st.metric("🔡 Characters", count_characters(text))

    st.subheader("🎯 Text Summary Insights")
    st.write(f"• **Average Word Length:** {avg_word_length(text)} characters")
    st.write(f"• **Estimated Reading Time:** {reading_time(text)} mins")
    st.write(f"• **Sentiment:** {sentiment_analysis(text)}")

    st.subheader("🔁 Most Frequent Words")
    common_words = most_common_words(text)
    for word, count in common_words:
        st.write(f"🔹 `{word}` — {count} times")

    st.subheader("🌈 Color-coded Sentences")
    st.markdown(highlight_sentences(text), unsafe_allow_html=True)

    st.subheader("🔤 Letter Frequency")
    letters = letter_frequency(text)
    letter_col1, letter_col2 = st.columns(2)
    half = len(letters) // 2 + 1
    with letter_col1:
        for letter, count in list(letters.items())[:half]:
            st.write(f"`{letter.upper()}`: {count}")
    with letter_col2:
        for letter, count in list(letters.items())[half:]:
            st.write(f"`{letter.upper()}`: {count}")

else:
    st.info("Start typing a paragraph above to see live insights.")

st.markdown("---")
st.caption("🔍 Created with ❤️ using Streamlit — for writers, thinkers, and curious minds.")
