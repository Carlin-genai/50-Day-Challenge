import streamlit as st
import random

# 🎨 Abbreviation ideas for each alphabet
ABBREVIATIONS = {
    'A': ['Amazing', 'Adventurous', 'Authentic'],
    'B': ['Brilliant', 'Bold', 'Balanced'],
    'C': ['Creative', 'Confident', 'Calm'],
    'D': ['Dynamic', 'Dazzling', 'Determined'],
    'E': ['Elegant', 'Energetic', 'Empathetic'],
    'F': ['Fabulous', 'Fearless', 'Friendly'],
    'G': ['Generous', 'Genuine', 'Graceful'],
    'H': ['Honest', 'Humble', 'Hopeful'],
    'I': ['Innovative', 'Intelligent', 'Inspiring'],
    'J': ['Joyful', 'Just', 'Jovial'],
    'K': ['Kind', 'Keen', 'Knowledgeable'],
    'L': ['Loyal', 'Lively', 'Lovely'],
    'M': ['Magical', 'Motivated', 'Mindful'],
    'N': ['Noble', 'Neat', 'Nurturing'],
    'O': ['Optimistic', 'Outstanding', 'Organized'],
    'P': ['Powerful', 'Peaceful', 'Passionate'],
    'Q': ['Quick-witted', 'Quiet', 'Quirky'],
    'R': ['Radiant', 'Reliable', 'Resilient'],
    'S': ['Strong', 'Smart', 'Sincere'],
    'T': ['Talented', 'Thoughtful', 'Trustworthy'],
    'U': ['Unique', 'Upbeat', 'Understanding'],
    'V': ['Valiant', 'Vibrant', 'Visionary'],
    'W': ['Wise', 'Warm-hearted', 'Witty'],
    'X': ['Xtraordinary', 'Xenial', 'Xpressive'],
    'Y': ['Youthful', 'Yes-minded', 'Yielding'],
    'Z': ['Zesty', 'Zealous', 'Zany'],
}

# ✨ Sweet meanings
NAME_MEANINGS = [
    "You light up the world with your presence.",
    "A rare gem in a sea of ordinary.",
    "A soul full of magic and meaning.",
    "Born to inspire and uplift.",
    "Charming, courageous, and kind-hearted.",
]

# 🌈 Emoji styling
def name_to_emojis(name):
    emoji_map = {
        'A': '🅰️', 'B': '🅱️', 'C': '🌊', 'D': '🐬', 'E': '🦅', 'F': '🎆',
        'G': '🌟', 'H': '🏠', 'I': '🍦', 'J': '🕹️', 'K': '🎋', 'L': '🦁',
        'M': '🌙', 'N': '🎶', 'O': '🌈', 'P': '🥞', 'Q': '👑', 'R': '🌹',
        'S': '⭐', 'T': '🌴', 'U': '☂️', 'V': '🎻', 'W': '🌊', 'X': '❌',
        'Y': '🌱', 'Z': '⚡'
    }
    return ''.join(emoji_map.get(ch.upper(), ch) for ch in name if ch.isalpha())

# ⚙️ Abbreviation logic
def generate_abbreviation(name):
    words = name.strip().split()
    initials = [word[0].upper() for word in words if word]
    abbreviation = {ch: random.choice(ABBREVIATIONS.get(ch.upper(), [ch])) for ch in initials}
    return initials, abbreviation

# 🚀 App UI
st.set_page_config(page_title="NameSpark ✨", layout="centered")
st.title("✨ NameSpark - Let Your Name Shine!")
st.markdown("Uncover the magic behind your name with initials, emojis, and sweet meanings.")

name_input = st.text_input("🔤 Enter your full name")

if name_input:
    initials, abbreviation = generate_abbreviation(name_input)

    st.subheader("🔠 Your Initials")
    st.success(" ".join(initials))

    st.subheader("💡 Abbreviation Style Meaning")
    for letter in initials:
        st.markdown(f"**{letter}** — {abbreviation[letter]}")

    st.subheader("🌈 Emoji Style")
    st.markdown(f"**{name_to_emojis(name_input)}**")

    st.subheader("💫 A Sweet Meaning")
    meaning = random.choice(NAME_MEANINGS)
    st.info(meaning)

    st.subheader("🎨 Creative Options")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔁 Refresh Abbreviation"):
            st.rerun()  # Correct Streamlit rerun

    with col2:
        abbr_lines = "\n".join([f"{k} - {v}" for k, v in abbreviation.items()])
        report_content = (
            f"Name: {name_input}\n"
            f"Initials: {' '.join(initials)}\n"
            f"Abbreviations:\n{abbr_lines}\n"
            f"Sweet Meaning: {meaning}"
        )
        st.download_button("⬇️ Download Name Report", data=report_content, file_name=f"{name_input}_meaning.txt")

else:
    st.warning("Please enter your full name to begin the magic!")

st.markdown("---")
st.caption("🚀 Created with ❤️ using Streamlit")
