import plotly.express as px
import streamlit as st
from utils.data_loader import load_data
from utils.sidebar import sidebar
from utils.footer import footer

sidebar()

st.title("📊 Dataset Explorer")

df = load_data()

st.subheader("Dataset Preview")

st.dataframe(df.head(10), use_container_width=True)

st.subheader("Dataset Shape")

col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])


st.subheader("Sentiment Distribution")

st.write(df["sentiment"].value_counts())    

fig = px.pie(
    df,
    names="sentiment",
    title="Sentiment Distribution"
)

st.plotly_chart(fig, use_container_width=True)


df["review_length"] = df["review"].apply(len)

st.subheader("Review Length Distribution")

fig = px.histogram(
    df,
    x="review_length",
    nbins=50,
    title="Distribution of Review Length"
)

st.plotly_chart(fig, use_container_width=True)

footer()