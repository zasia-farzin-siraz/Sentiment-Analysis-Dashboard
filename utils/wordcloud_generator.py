import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

@st.cache_data
def generate_wordcloud(text):

    wc = WordCloud(
        width=1400,
        height=700,
        background_color="black",
        colormap="viridis",
        max_words=200,
        contour_width=1,
        contour_color="white"
    ).generate(text)

    fig, ax = plt.subplots(figsize=(16, 8))

    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")

    return fig