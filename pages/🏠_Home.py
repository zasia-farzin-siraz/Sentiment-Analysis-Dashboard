import streamlit as st
from utils.sidebar import sidebar
from utils.footer import footer

sidebar()

st.set_page_config(page_title="Movie Sentiment Dashboard", layout="wide")

st.title("🎬 Movie Review Sentiment Analysis")

st.markdown("""
### Welcome!

This project predicts whether a movie review is **Positive** or **Negative**
using Natural Language Processing (NLP) and Machine Learning.

---

### Technologies

- Python
- Scikit-Learn
- NLTK
- TF-IDF Vectorization
- Streamlit

---

### Machine Learning Models

- Logistic Regression
- Naive Bayes
- Linear SVM
- Random Forest
""")

st.divider()

col1, col2, col3 = st.columns(3)

col1.metric("Dataset", "50,000 Reviews")
col2.metric("Models", "4")
col3.metric("Best Accuracy", "90%")

footer()