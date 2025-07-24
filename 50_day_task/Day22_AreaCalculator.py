import streamlit as st
import pyttsx3
import math
from PIL import Image, ImageDraw
from datetime import datetime

# Initialize voice engine
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Draw dynamic shapes
def draw_shape(shape, dark=False):
    bg = "#333333" if dark else "white"
    color_map = {"Circle": "blue", "Rectangle": "green", "Triangle": "red"}
    img = Image.new("RGB", (200, 200), bg)
    draw = ImageDraw.Draw(img)

    if shape == "Circle":
        draw.ellipse((50, 50, 150, 150), outline=color_map[shape], width=5)
    elif shape == "Rectangle":
        draw.rectangle((40, 70, 160, 130), outline=color_map[shape], width=5)
    elif shape == "Triangle":
        draw.polygon([(100, 40), (40, 160), (160, 160)], outline=color_map[shape], width=5)

    return img

# Fun facts about each shape
def fun_fact(shape):
    facts = {
        "Circle": "🔵 A circle encloses the largest area with the shortest perimeter!",
        "Rectangle": "🟩 Rectangles form the backbone of most designs — from screens to architecture!",
        "Triangle": "🔺 Triangles are the most stable shape — used in bridges and trusses!"
    }
    return facts.get(shape, "")

# App config
st.set_page_config(page_title="Smart Area Calculator", layout="centered")

# App title
st.title("📐 Smart Area Calculator")

# Theme switch
dark_mode = st.toggle("🌗 Dark Mode")
st.markdown("---")

# Choose shape
shape = st.radio("Select a shape:", ["Circle", "Rectangle", "Triangle"], horizontal=True)

# Show shape illustration and fact
st.image(draw_shape(shape, dark=dark_mode), caption=shape)
st.info(fun_fact(shape))

# History
if "history" not in st.session_state:
    st.session_state.history = []

# Calculation Logic
def log_and_speak(shape, area):
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.history.append((shape, area, timestamp))
    speak(f"The area of the {shape.lower()} is {area:.2f} square units.")

# Form Input
with st.form(f"form_{shape}"):
    if shape == "Circle":
        radius = st.number_input("Enter radius:", min_value=0.0, step=0.1)
        submitted = st.form_submit_button("Calculate Area")
        if submitted:
            area = math.pi * radius ** 2
            st.success(f"Area of Circle: {area:.2f} sq units")
            log_and_speak("Circle", area)

    elif shape == "Rectangle":
        length = st.number_input("Enter length:", min_value=0.0, step=0.1)
        width = st.number_input("Enter width:", min_value=0.0, step=0.1)
        submitted = st.form_submit_button("Calculate Area")
        if submitted:
            area = length * width
            st.success(f"Area of Rectangle: {area:.2f} sq units")
            log_and_speak("Rectangle", area)

    elif shape == "Triangle":
        base = st.number_input("Enter base:", min_value=0.0, step=0.1)
        height = st.number_input("Enter height:", min_value=0.0, step=0.1)
        submitted = st.form_submit_button("Calculate Area")
        if submitted:
            area = 0.5 * base * height
            st.success(f"Area of Triangle: {area:.2f} sq units")
            log_and_speak("Triangle", area)

# Display recent history
if st.session_state.history:
    st.markdown("### 📊 Recent Calculations")
    for shape, area, time in reversed(st.session_state.history[-5:]):
        st.write(f"🕒 {time} — {shape}: {area:.2f} sq units")
