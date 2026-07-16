import streamlit as st
import plotly.express as px

from utils.results_loader import (
    load_accuracy,
    load_report,
    load_confusion
)
from utils.sidebar import sidebar
from utils.footer import footer

sidebar()

st.title("📈 Model Performance")

st.markdown("""
Compare the performance of different Machine Learning models
trained on the IMDB Movie Review dataset.
""")

accuracy = load_accuracy()
report = load_report()
cm = load_confusion()

st.divider()

st.subheader("🏆 Model Accuracy Comparison")

st.dataframe(
    accuracy,
    use_container_width=True
)

fig = px.bar(
    accuracy,
    x="Model",
    y="Accuracy",
    color="Accuracy",
    text="Accuracy",
    title="Accuracy Comparison"
)

fig.update_traces(
    texttemplate="%{text:.3f}",
    textposition="outside"
)

fig.update_layout(
    yaxis_range=[0.80,1.00]
)

st.plotly_chart(
    fig,
    use_container_width=True
)

best = accuracy.loc[
    accuracy["Accuracy"].idxmax()
]

st.success(
    f"""
🏆 Best Model

**{best['Model']}**

Accuracy: **{best['Accuracy']:.4f}**
"""
)


st.divider()
st.subheader("📋 Classification Report")
st.dataframe(
    report,
    use_container_width=True
)


st.divider()
st.subheader("🎯 Confusion Matrix")
fig = px.imshow(
    cm,
    text_auto=True,
    color_continuous_scale="Blues",
    aspect="auto"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

footer()