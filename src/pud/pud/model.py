import joblib

def load_model(path):
    """Load a trained ML model from disk."""
    return joblib.load(path)

def predict_urls(model, features_df):
    """
    Predict if URLs are phishing or safe.
    Returns a list of predictions.
    """
    preds = model.predict(features_df)
    return ["Phishing" if p == 1 else "Safe" for p in preds]
