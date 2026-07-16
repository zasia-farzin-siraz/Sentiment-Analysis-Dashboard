import streamlit as st
import time

from utils.footer import footer
from utils.predict import predict
from utils.sidebar import sidebar

sidebar()

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Prediction",
    page_icon="📝",
    layout="wide"
)

# -----------------------------
# Page Title
# -----------------------------

st.title("📝 Movie Review Sentiment Prediction")

st.markdown("""
Enter a movie review below and the trained Machine Learning model will predict
whether the review is **Positive** or **Negative**.
""")

# -----------------------------
# Example
# -----------------------------

with st.expander("💡 Example Review"):
    st.write(
        """
        This movie was absolutely fantastic.
        The acting was brilliant, the story was engaging,
        and I enjoyed every minute of it.
        """
    )

# -----------------------------
# Text Area
# -----------------------------

col1, col2 = st.columns(2)

with col1:
    if st.button("😊 Positive Example"):
        st.session_state.review = (
            "This movie was absolutely amazing. "
            "The acting was fantastic and I loved every minute."
        )

with col2:
    if st.button("😞 Negative Example"):
        st.session_state.review = (
            "Terrible movie. It was boring, poorly acted, "
            "and a complete waste of time."
        )
review = st.text_area(
    "Movie Review",
    key="review",
    height=220
)

# -----------------------------
# Predict Button
# -----------------------------

if st.button("🔍 Analyze Review", use_container_width=True):

    if review.strip() == "":
        st.warning("⚠️ Please enter a movie review.")
    else:

        with st.spinner("Analyzing review..."):
            time.sleep(1)

            prediction, confidence = predict(review)
            if prediction == 1:
                st.success("😊 Positive Review")
            else:
                st.error("😞 Negative Review")

            if confidence is not None:
                 st.progress(float(confidence))
                 st.write(f"**Confidence:** {confidence*100:.2f}%")


# -----------------------------
# Footer
# -----------------------------

st.divider()

st.caption("Built with Streamlit • Scikit-Learn • NLTK")


footer()