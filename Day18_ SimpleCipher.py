import streamlit as st
import random

# Caesar cipher shift function
def shift_letter(char, shift):
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - base + shift) % 26 + base)
    return char

def shift_text(text, shift):
    return ''.join(shift_letter(char, shift) for char in text)

# Mapping original to shifted
def generate_letter_mapping(text, shift):
    mapping = []
    for char in text:
        if char.isalpha():
            mapping.append((char, shift_letter(char, shift)))
    return mapping

# Word puzzle challenge logic
WORDS = ['apple', 'banana', 'stream', 'python', 'bright', 'dream', 'magic', 'brave', 'truth', 'zebra']
selected_word = random.choice(WORDS)
encrypted_challenge = shift_text(selected_word, 1)

# App UI
st.set_page_config(page_title="AlphaMorph Live 🔠", layout="centered")
st.title("🔠 AlphaMorph Live")
st.markdown("Transform, decode, and play with letters in real-time!")

tab1, tab2, tab3 = st.tabs(["🔤 Live Letter Shift", "🔓 Decrypt Mode", "🧩 Word Puzzle Challenge"])

# Tab 1 - Live Shift
with tab1:
    st.header("🔤 Real-Time Typing + Shift +1")
    input_text = st.text_input("Type a word or sentence:")
    shift = 1

    if input_text:
        shifted = shift_text(input_text, shift)
        st.subheader("✨ Shifted Output")
        st.success(shifted)

        st.subheader("🔍 Visual Letter Mapping")
        mapping = generate_letter_mapping(input_text, shift)
        for orig, new in mapping:
            st.write(f"**{orig.upper()} → {new.upper()}**")
    else:
        st.info("Start typing above to see real-time shifts.")

# Tab 2 - Decrypt Mode
with tab2:
    st.header("🔓 Decrypt Encrypted Text")
    encrypted_input = st.text_input("Paste encrypted text to decode:")
    reverse_shift = -1

    if encrypted_input:
        decrypted = shift_text(encrypted_input, reverse_shift)
        st.subheader("✅ Decrypted Output")
        st.code(decrypted, language='text')

        st.subheader("🧩 Decryption Letter Map")
        mapping = generate_letter_mapping(encrypted_input, reverse_shift)
        for orig, new in mapping:
            st.write(f"**{orig.upper()} → {new.upper()}**")
    else:
        st.info("Paste a Caesar-shifted message above to decode.")

# Tab 3 - Word Puzzle Challenge
with tab3:
    st.header("🧩 Guess the Original Word!")
    st.markdown("We’ve encrypted a random 5-6 letter word. Try guessing the original!")

    st.info(f"🔐 Encrypted Word: **{encrypted_challenge.upper()}**")

    user_guess = st.text_input("Your guess:")
    if user_guess:
        if user_guess.lower() == selected_word:
            st.success("🎉 Correct! You cracked the word!")
        else:
            st.error("❌ Try again!")

    if st.button("🔁 New Word"):
        st.experimental_rerun()

st.markdown("---")
st.caption("🚀 Built with ❤️ using Streamlit — AlphaMorph makes letters fun!")
