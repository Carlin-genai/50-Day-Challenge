import streamlit as st
import time
import matplotlib.pyplot as plt
from collections import Counter
import random

# ---------------------- Styling ----------------------
st.set_page_config(page_title="Vowel Vision", page_icon="🔤", layout="centered")
st.markdown("""
    <style>
    .stApp {
        background-color: #fdf6e3;
        color: #333333;
        font-family: 'Segoe UI', sans-serif;
    }
    .big-title {
        font-size: 2.5em;
        text-align: center;
        color: #ff6347;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .highlight {
        background-color: #fffbcc;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------- Title ----------------------
st.markdown('<div class="big-title">🔍 Vowel Vision: The Magical Counter 🔠</div>', unsafe_allow_html=True)

# ---------------------- Input ----------------------
word = st.text_input("✨ Enter a word to count its vowels:", "").strip()

vowels = 'aeiouAEIOU'

# Fun emoji mapping
vowel_emojis = {
    'a': '🍎', 'e': '🐘', 'i': '🍦', 'o': '🐙', 'u': '🦄',
    'A': '🍎', 'E': '🐘', 'I': '🍦', 'O': '🐙', 'U': '🦄'
}

if word:
    st.markdown("🧠 **Processing your word...**")
    time.sleep(0.5)

    # Count vowels
    vowel_counts = Counter([char for char in word if char in vowels])
    total = sum(vowel_counts.values())

    # 🎉 Result message
    st.success(f"✅ The word **`{word}`** contains **{total} vowel{'s' if total != 1 else ''}**!")

    # 🧩 Detailed breakdown
    if total > 0:
        st.markdown("### 🔡 Vowel Breakdown:")
        for v in vowels:
            if v in vowel_counts:
                emoji = vowel_emojis.get(v.lower(), '🔠')
                st.markdown(f"- **{v.upper()}** {emoji}: `{vowel_counts[v]}`")

        # 📊 Bar chart
        st.markdown("### 📊 Vowel Frequency Chart")
        fig, ax = plt.subplots()
        ax.bar(vowel_counts.keys(), vowel_counts.values(), color=['#FF5733', '#33C3FF', '#DAF7A6', '#F39C12', '#AF7AC5'])
        ax.set_title("Vowel Count Visualization", fontsize=14)
        ax.set_ylabel("Count")
        ax.set_xlabel("Vowels")
        st.pyplot(fig)
    else:
        st.warning("😢 No vowels found! Try another word.")

else:
    st.info("🔠 Enter a word above to reveal its hidden vowels!")

# ---------------------- Footer ----------------------
st.markdown("---")
st.markdown("Made with ❤️ using Python + Streamlit")

