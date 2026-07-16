import streamlit as st

st.set_page_config(
    page_title="Movie Review Sentiment Analysis",
    page_icon="🎬",
    layout="wide"
)


st.title("🎬 Movie Review Sentiment Analysis Dashboard")

st.markdown("""
Welcome to the **Movie Review Sentiment Analysis Dashboard**.

This application demonstrates an end-to-end Natural Language Processing (NLP)
pipeline for classifying IMDb movie reviews as **Positive** or **Negative**.

### Dashboard Features

- 📝 Predict movie review sentiment
- 📊 Explore the IMDb dataset
- 📈 Compare machine learning models
- ☁️ Visualize word clouds
- ℹ️ Learn about the project
""")


col1, col2, col3, col4 = st.columns(4)

col1.metric("Dataset", "50,000")
col2.metric("Models", "4")
col3.metric("Best Accuracy", "88.58%")
col4.metric("Deployment", "Streamlit")
st.divider()



st.subheader("✨ Dashboard Features")

c1, c2 = st.columns(2)

with c1:
    st.info("""
📝 **Sentiment Prediction**

Predict whether a movie review is Positive or Negative.
""")

    st.info("""
📊 **Dataset Explorer**

Explore the IMDb movie review dataset.
""")

with c2:
    st.info("""
📈 **Model Performance**

Compare multiple ML models and evaluation metrics.
""")

    st.info("""
☁️ **Word Cloud**

Visualize frequently occurring words in positive and negative reviews.
""")
    

st.divider()
st.caption("Developed by Zasia Farzin Siraz • BRAC University • Streamlit • Scikit-learn")