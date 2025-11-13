import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from src.pud.feature_extraction import extract_features
import joblib

def main():
    parser = argparse.ArgumentParser(description="Train Phishing URL Detector ML model")
    parser.add_argument("--input", type=str, required=True, help="CSV or TXT file with URLs and labels")
    parser.add_argument("--model-output", type=str, required=True, help="Path to save trained model (.joblib)")
    args = parser.parse_args()

    # Load dataset
    if args.input.endswith(".csv"):
        df = pd.read_csv(args.input)
    else:
        df = pd.read_csv(args.input, names=["url", "label"])

    urls = df["url"].tolist()
    labels = df["label"].tolist()

    features = extract_features(urls)

    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    acc = model.score(X_test, y_test)
    print(f"Model trained. Test accuracy: {acc:.2f}")

    joblib.dump(model, args.model_output)
    print(f"Model saved to {args.model_output}")

if __name__ == "__main__":
    main()
