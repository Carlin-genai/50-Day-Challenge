import streamlit as st
import pyttsx3
import re
from PIL import Image, ImageDraw, ImageFont

# Mapping of area codes to emoji and location
area_code_info = {
    "212": ("🗽", "New York"),
    "415": ("🌉", "San Francisco"),
    "213": ("🎬", "Los Angeles"),
    "305": ("🌴", "Miami"),
    "312": ("🏙️", "Chicago"),
    "512": ("🤠", "Austin"),
    "617": ("📚", "Boston"),
    "702": ("🎰", "Las Vegas"),
    "206": ("☕", "Seattle")
}

# Text-to-speech engine setup
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Format phone number to (XXX) XXX-XXXX
def format_number(num):
    return f"({num[:3]}) {num[3:6]}-{num[6:]}" if len(num) == 10 else None

# Detect area code and assign emoji and location
def get_area_info(num):
    area_code = num[:3]
    emoji, loc = area_code_info.get(area_code, ("📞", "Unknown"))
    return emoji, loc

# Create initials avatar
def create_avatar(phone_number):
    initials = phone_number[:3]
    img = Image.new("RGB", (100, 100), color="#4b4b4b")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 40)
    draw.text((10, 25), initials, font=font, fill="white")
    return img

# App UI
st.set_page_config(page_title="📱 Phone Number Beautifier", layout="centered")

st.title("📱 Phone Number Beautifier")
dark_mode = st.toggle("🌙 Dark Mode")

st.markdown("---")

mode = st.radio("Choose Mode", ["Single Format", "Bulk Format"])

if mode == "Single Format":
    phone = st.text_input("Enter 10-digit number:")

    if phone:
        digits = re.sub(r"\D", "", phone)
        if len(digits) == 10:
            formatted = format_number(digits)
            emoji, loc = get_area_info(digits)

            st.success(f"{emoji} {formatted} - Likely from **{loc}**")

            # Avatar
            avatar = create_avatar(digits)
            st.image(avatar, caption="Caller Avatar", use_column_width=False)

            # Voice
            if st.button("🔊 Read Aloud"):
                speak(f"The number is {formatted}. From {loc}.")

        else:
            st.error("Please enter exactly 10 digits.")
else:
    input_data = st.text_area("Paste numbers (1 per line):")
    if input_data:
        nums = input_data.strip().splitlines()
        results = []
        for n in nums:
            digits = re.sub(r"\D", "", n)
            if len(digits) == 10:
                formatted = format_number(digits)
                emoji, loc = get_area_info(digits)
                results.append(f"{emoji} {formatted} - {loc}")
            else:
                results.append(f"❌ Invalid: {n}")
        st.markdown("### ✅ Results:")
        st.code("\n".join(results))

st.markdown("---")
st.info("Thank you for beautifying your calls with us! 🎨📞")
