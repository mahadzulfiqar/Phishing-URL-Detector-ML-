import argparse
from src.pud.feature_extraction import extract_features
from src.pud.model import load_model, predict_urls

def main():
    parser = argparse.ArgumentParser(description="Phishing URL Detector CLI")
    parser.add_argument("--url", type=str, help="Single URL to check")
    parser.add_argument("--input", type=str, help="Input file with URLs (one per line)")
    parser.add_argument("--model", type=str, required=True, help="Path to trained ML model (.joblib)")
    parser.add_argument("--output", type=str, help="Path to save predictions (CSV/JSON)")
    args = parser.parse_args()

    model = load_model(args.model)

    if args.url:
        features = extract_features([args.url])
        prediction = predict_urls(model, features)
        print(f"URL: {args.url} --> Prediction: {prediction[0]}")
    elif args.input:
        with open(args.input, "r") as f:
            urls = [line.strip() for line in f.readlines()]
        features = extract_features(urls)
        predictions = predict_urls(model, features)
        if args.output:
            import pandas as pd
            df = pd.DataFrame({"URL": urls, "Prediction": predictions})
            df.to_csv(args.output, index=False)
            print(f"Predictions saved to {args.output}")
        else:
            for url, pred in zip(urls, predictions):
                print(f"URL: {url} --> Prediction: {pred}")
    else:
        print("Provide either --url or --input file to scan.")

if __name__ == "__main__":
    main()
