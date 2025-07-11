import streamlit as st
import time

# Title with emoji
st.title("🧮 Sum Calculator")
st.markdown("Enter a number *n*, and we'll calculate the sum from **1 to *n*** using a loop!")

# Sidebar for extra info
st.sidebar.header("About")
st.sidebar.info(
    "This app calculates the sum of numbers from 1 to n using a simple for-loop. "
    "You can see the progress step-by-step and even visualize the cumulative sum!"
)

# Input using slider
n = st.slider("Choose a number (n):", min_value=1, max_value=100, value=10)

# Button to trigger calculation
if st.button("🚀 Calculate Sum"):
    total = 0
    progress_bar = st.progress(0)
    status_text = st.empty()
    sum_list = []

    # Loop with visual feedback
    for i in range(1, n + 1):
        total += i
        sum_list.append(total)
        percent_complete = int((i / n) * 100)
        progress_bar.progress(percent_complete)
        status_text.text(f"Calculating: {percent_complete}% complete")
        time.sleep(0.05)  # Add delay to visualize progress

    status_text.success("✅ Calculation Complete!")
    
    # Display result
    st.balloons()
    st.markdown(f"### The sum of all numbers from **1 to {n}** is: `{total}`")

    # Show chart of cumulative sum
    st.subheader("📈 Cumulative Sum Progress")
    st.line_chart(sum_list)
else:
    st.info("Click the button above to calculate the sum.")