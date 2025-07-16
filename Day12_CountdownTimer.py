import streamlit as st
import time

# --- Page Setup ---
st.set_page_config(page_title="⏳ Countdown Timer", page_icon="🕒", layout="centered")
st.title("⏱️ 10-Second Countdown Challenge!")
st.subheader("Watch as we count down to something exciting...")

st.markdown("---")

# Button to start countdown
if st.button("🚀 Start Countdown"):
    countdown_placeholder = st.empty()

    for i in range(10, -1, -1):
        countdown_placeholder.markdown(f"<h1 style='text-align: center; color: #FF4B4B;'>{i}</h1>", unsafe_allow_html=True)
        time.sleep(1)

    # After countdown ends
    st.success("🎉 Time's up! You did it!")
    st.balloons()

else:
    st.info("Press the button above to begin the countdown ⬆️")

st.markdown("---")
st.caption("Made with ❤️ by Carlin • Powered by Streamlit")
