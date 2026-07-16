import streamlit as st
from utils.sidebar import sidebar
from utils.footer import footer

sidebar()

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About This Project")

st.markdown("""
## 🎬 Movie Review Sentiment Analysis Dashboard

This project uses **Natural Language Processing (NLP)** and **Machine Learning**
to classify IMDb movie reviews as **Positive** or **Negative**.

The dashboard demonstrates the complete machine learning workflow, from
data preprocessing and feature engineering to model evaluation and deployment
using Streamlit.
""")

st.divider()

# Dataset
st.header("📂 Dataset")

st.info("""
IMDb Movie Review Dataset

• 50,000 Movie Reviews

• Balanced Dataset

• Binary Sentiment Classification

• Source: Kaggle
""")

# Models
st.divider()

st.header("🧠 Machine Learning Models")

col1, col2 = st.columns(2)

with col1:
    st.success("✅ Logistic Regression")
    st.success("✅ Linear SVM")

with col2:
    st.success("✅ Naive Bayes")
    st.success("✅ Random Forest")

# Tech Stack
st.divider()

st.header("🛠 Tech Stack")

st.code("""
Python
Pandas
NumPy
Scikit-Learn
NLTK
Plotly
Matplotlib
WordCloud
Streamlit
""")

# Workflow
st.divider()

st.header("📈 Project Workflow")

st.markdown("""
Dataset

⬇

Text Cleaning

⬇

Tokenization

⬇

Stopword Removal

⬇

Lemmatization

⬇

TF-IDF Vectorization

⬇

Machine Learning Models

⬇

Prediction

⬇

Interactive Dashboard
""")

st.divider()

st.header("👩‍💻 Developer")

st.markdown("""
**Name:** Zasia Farzin Siraz

**University:** BRAC University

**Department:** Computer Science and Engineering

This project was developed as part of my Machine Learning portfolio.
""")

st.divider()

st.caption("Made with ❤️ using Streamlit and Scikit-Learn")


footer()



st.subheader("👩‍💻 Developer")

st.info("""
**Zasia Farzin Siraz**

🎓 B.Sc. in Computer Science & Engineering

🏫 BRAC University

💡 Interested in Machine Learning, Data Science, and AI

🌐 GitHub: https://github.com/zasia-farzin-siraz
""")