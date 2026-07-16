import pandas as pd
import streamlit as st
from collections import Counter
import plotly.express as px
from utils.wordcloud_generator import generate_wordcloud
from utils.footer import footer

from utils.sidebar import sidebar

sidebar()

st.title("☁️ Word Cloud")

df = pd.read_csv("data/clean_imdb_dataset.csv")

# 3000 reviews for faster loading
positive_df = df[df["sentiment"] == "positive"].sample(
    n=3000,
    random_state=42
)

negative_df = df[df["sentiment"] == "negative"].sample(
    n=3000,
    random_state=42
)

positive = " ".join(positive_df["clean_review"])
negative = " ".join(negative_df["clean_review"])

st.subheader("Positive Reviews")

st.pyplot(generate_wordcloud(positive))

st.divider()

st.subheader("Negative Reviews")

st.pyplot(generate_wordcloud(negative))



def top_words(text, n=20):

    words = text.split()

    counter = Counter(words)

    return counter.most_common(n)


positive_words = top_words(positive)

positive_df = pd.DataFrame(
    positive_words,
    columns=["Word","Count"]
)

fig = px.bar(
    positive_df,
    x="Word",
    y="Count",
    title="Top 20 Positive Words"
)

st.plotly_chart(fig, use_container_width=True)



negative_words = top_words(negative)

negative_df = pd.DataFrame(
    negative_words,
    columns=["Word","Count"]
)

fig = px.bar(
    negative_df,
    x="Word",
    y="Count",
    title="Top 20 Negative Words"
)

st.plotly_chart(fig, use_container_width=True)


footer()