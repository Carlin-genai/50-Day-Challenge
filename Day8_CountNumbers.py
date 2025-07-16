import streamlit as st
from PIL import Image

# ---- Page Configuration ----
st.set_page_config(
    page_title="🧮 Number Counter | Carlin's Math Zone",
    page_icon="🔢",
    layout="centered"
)

# ---- Header Image ----
st.image("https://cdn.pixabay.com/photo/2015/12/03/14/53/mathematics-1076329_1280.jpg", use_column_width=True)

# ---- Title and Introduction ----
st.title("🔢 Count Positive, Negative & Zero Numbers")
st.markdown("""
Welcome to **Carlin's Math Zone**!  
Enter a list of numbers and let's explore how many are:
- 🟢 Positive  
- 🔴 Negative  
- ⚫ Zero  

Plus, we’ll tell you **which numbers** belong where — and **why**!
""")

# ---- Input Field ----
input_numbers = st.text_input("✍️ Enter numbers separated by commas (e.g. `4, -2, 0, 7, -5`)")

# ---- Logic and Result ----
if input_numbers:
    try:
        # Convert the input into a list of numbers
        number_list = [float(num.strip()) for num in input_numbers.split(',')]

        # Categorize numbers
        positives = [n for n in number_list if n > 0]
        negatives = [n for n in number_list if n < 0]
        zeros = [n for n in number_list if n == 0]

        # Count each type
        positive_count = len(positives)
        negative_count = len(negatives)
        zero_count = len(zeros)

        # ---- Display Results Summary ----
        st.success("🎉 Count complete!")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("https://cdn-icons-png.flaticon.com/512/190/190411.png", width=80)
            st.metric(label="Positive", value=positive_count)

        with col2:
            st.image("https://cdn-icons-png.flaticon.com/512/753/753345.png", width=80)
            st.metric(label="Negative", value=negative_count)

        with col3:
            st.image("https://cdn-icons-png.flaticon.com/512/565/565491.png", width=80)
            st.metric(label="Zeros", value=zero_count)

        # ---- Detailed Explanations ----
        st.markdown("### 📋 Breakdown of Results:")

        st.markdown("#### 🟢 Positive Numbers")
        if positives:
            st.write(f"{positives}")
            st.info("These numbers are greater than zero — typically representing **gain, quantity, or upward values**.")
        else:
            st.warning("No positive numbers found.")

        st.markdown("#### 🔴 Negative Numbers")
        if negatives:
            st.write(f"{negatives}")
            st.info("These are less than zero — often used to show **loss, decrease, or reverse direction**.")
        else:
            st.warning("No negative numbers found.")

        st.markdown("#### ⚫ Zeroes")
        if zeros:
            st.write(f"{zeros}")
            st.info("Zero represents **neutrality** — not positive or negative, just the balance point.")
        else:
            st.warning("No zeros found.")

    except ValueError:
        st.error("⚠️ Please enter only numbers separated by commas.")

# ---- Footer ----
st.markdown("---")
st.caption("✨ Created with ❤️ by **Carlin** • Exploring numbers the creative way!")
