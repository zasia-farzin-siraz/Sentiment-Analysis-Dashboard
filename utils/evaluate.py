import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier

from utils.preprocessing import preprocess_text
from utils.data_loader import load_data


@st.cache_data
def evaluate_models():

    df = load_data().copy()

    df["clean_review"] = df["review"].apply(preprocess_text)

    X = df["clean_review"]
    y = df["sentiment"]

    vectorizer = TfidfVectorizer(max_features=5000)

    X = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Naive Bayes": MultinomialNB(),
        "Linear SVM": LinearSVC(),
        "Random Forest": RandomForestClassifier(random_state=42)
    }

    results = []

    best_model = None
    best_accuracy = 0

    for name, model in models.items():

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)

        results.append({
            "Model": name,
            "Accuracy": accuracy
        })

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = model
            best_predictions = predictions

    report = classification_report(
        y_test,
        best_predictions,
        output_dict=True
    )

    cm = confusion_matrix(y_test, best_predictions)

    return (
        pd.DataFrame(results),
        pd.DataFrame(report).transpose(),
        cm
    )