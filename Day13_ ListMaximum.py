import streamlit as st
import time
import random

# ---------- Streamlit Page Setup ----------
st.set_page_config(page_title="Mega Max Finder", page_icon="📈", layout="centered")

# ---------- Custom CSS Styling ----------
st.markdown("""
    <style>
    .main-title {
        font-size: 2.5em;
        text-align: center;
        color: #4CAF50;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .highlight {
        background-color: #E8F5E9;
        padding: 12px;
        border-radius: 10px;
        font-size: 1.1em;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown('<div class="main-title">📈 Mega Max Finder 🚀</div>', unsafe_allow_html=True)

# ---------- Instructions ----------
st.info("Enter a list of numbers separated by commas (e.g. `12, 45, -3, 99, 7`)")

# ---------- User Input ----------
user_input = st.text_input("🔢 Enter your list of numbers:")

# ---------- Helper: Find Max Without Using max() ----------
def find_max_number(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

# ---------- Main Logic ----------
if user_input:
    try:
        number_list = [int(num.strip()) for num in user_input.split(',')]
        st.success("✅ Numbers received!")

        with st.expander("📋 Your Entered Numbers"):
            st.markdown(f"<div class='highlight'>{number_list}</div>", unsafe_allow_html=True)

        st.markdown("🔍 **Finding the largest number...**")
        with st.spinner("Crunching numbers 🔄"):
            time.sleep(1.5)  # Simulate loading
            largest_number = find_max_number(number_list)

        st.balloons()
        st.markdown(f"""
            <div style='text-align:center; font-size: 1.8em; color:#FF5722; font-weight:bold; margin-top:20px;'>
                🎉 The Largest Number is: <span style='color:#2196F3'>{largest_number}</span> 🎉
            </div>
        """, unsafe_allow_html=True)

    except ValueError:
        st.error("❌ Please enter valid integers separated by commas.")
else:
    st.warning("📥 Waiting for your input above...")

# ---------- Footer ----------
st.markdown("---")
st.markdown("Made with ❤️ using Python & Streamlit")
