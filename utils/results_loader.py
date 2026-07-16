import pandas as pd
import streamlit as st


@st.cache_data
def load_accuracy():
    return pd.read_csv("results/accuracy.csv")


@st.cache_data
def load_report():
    return pd.read_csv("results/classification_report.csv", index_col=0)


@st.cache_data
def load_confusion():
    return pd.read_csv("results/confusion_matrix.csv", index_col=0)