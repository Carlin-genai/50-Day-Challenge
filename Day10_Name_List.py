# streamlit_app.py

import streamlit as st

# Page title
st.title("🔠 Name Length Analyzer")
st.subheader("Let’s see how long your names are!")

# Step 1: Store 5 names in a list
names = ["Carlin", "Ava", "Jonathan", "Zara", "Michael"]

# Step 2: Display each name with its length
st.write("Here are the names and their lengths:")

# Step 3: Loop through and display
for i, name in enumerate(names, start=1):
    st.markdown(f"**{i}. {name}** ➡️ `{len(name)} characters`")

# Step 4: Add a little fun visual
st.success("✨ All names processed successfully!")
st.balloons()
