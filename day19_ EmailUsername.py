import streamlit as st
import re
import random

# Helper functions
def extract_username(email):
    if '@' in email:
        return email.split('@')[0]
    return None

def beautify_username(username):
    parts = re.split(r'[._-]', username)
    return ' '.join([p.capitalize() for p in parts if p])

def suggest_usernames(username):
    base = username.replace('.', '').replace('_', '')
    return [
        f"{base}{random.randint(10,99)}",
        f"the_{base}",
        f"{base}_official",
        f"{base}123",
        f"{base}_xoxo"
    ]

def analyze_username(username):
    return {
        "Length": len(username),
        "Contains Digits": any(char.isdigit() for char in username),
        "Contains Special Characters": any(not char.isalnum() for char in username),
        "Is Alphanumeric": username.isalnum()
    }

def generate_meaning(username):
    # Just for fun - not real meanings
    adjectives = ["Brilliant", "Creative", "Loyal", "Bold", "Curious", "Kind", "Witty", "Mighty"]
    traits = ["Explorer", "Thinker", "Dreamer", "Leader", "Coder", "Designer"]
    return f"{random.choice(adjectives)} {random.choice(traits)}"

def emoji_decorator(username):
    return f"✨ {username} ✨"

def get_anagrams(word):
    from itertools import permutations
    unique = set([''.join(p) for p in permutations(word) if len(p) > 2])
    return list(unique)[:5]

# App UI
st.set_page_config(page_title="Username Wizard ✉️", layout="centered")
st.title("📧 Email Username Extractor & Enhancer")

email = st.text_input("Enter your email address:")

if email:
    if '@' in email:
        username = extract_username(email)
        st.success(f"✅ Username extracted: `{username}`")

        beautified = beautify_username(username)
        st.subheader("🎨 Beautified Username")
        st.write(f"🧑‍🎨 {beautified}")

        st.subheader("💡 Creative Meaning")
        st.write(f"🔮 You are a **{generate_meaning(username)}**")

        st.subheader("📊 Username Analyzer")
        analysis = analyze_username(username)
        st.json(analysis)

        st.subheader("🪄 Suggested Social Usernames")
        for s in suggest_usernames(username):
            st.markdown(f"- `{s}`")

        st.subheader("🎉 Emoji Decorated")
        st.markdown(f"`{emoji_decorator(username)}`")

        st.subheader("🔀 Anagram Generator")
        anagrams = get_anagrams(username)
        if anagrams:
            st.markdown(", ".join(anagrams))
        else:
            st.info("Not enough letters to generate anagrams.")

    else:
        st.error("❌ Please enter a valid email address.")

st.markdown("---")
st.caption("🚀 Powered by Streamlit — turning emails into creativity 💫")
