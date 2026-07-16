from utils.preprocessing import preprocess_text
from utils.model_loader import model, vectorizer

label_map = {
    0: "Negative 😞",
    1: "Positive 😊"
}


def predict(review):
    cleaned = preprocess_text(review)
    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)[0]

    confidence = None

    if hasattr(model, "predict_proba"):
        confidence = model.predict_proba(vector).max()

    return prediction, confidence