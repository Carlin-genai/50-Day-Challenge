# save as test_score_app.py
import streamlit as st

# --- Page setup ---
st.set_page_config(page_title="🎓 Test‑Score Checker", page_icon="📊", layout="centered")

st.title("🎓 Test‑Score Average & Pass/Fail")
st.caption("Enter five scores and see whether you pass! (Pass mark = 60 %)")

st.markdown("---")

# --- Score inputs ---
st.subheader("✍️ Enter your five test scores")
scores = []
for i in range(1, 6):
    score = st.number_input(f"Score {i}", min_value=0.0, max_value=100.0, value=0.0, key=f"score_{i}")
    scores.append(score)

# --- Compute average ---
average = sum(scores) / 5
st.markdown("### 📈 Your average:")
st.metric(label="Average (%)", value=f"{average:.2f}")

# --- Pass / Fail logic ---
PASS_MARK = 60  # change this if needed

if all(s == 0 for s in scores):
    st.info("Enter scores above to see your result!")
else:
    if average >= PASS_MARK:
        st.success("🎉 Congrats, you **PASS**!")
        st.balloons()
    else:
        st.error("🚫 Sorry, you **FAIL**. Keep studying and try again!")

st.markdown("---")
st.caption("App by *Your‑Name‑Here* • Powered by Streamlit")
