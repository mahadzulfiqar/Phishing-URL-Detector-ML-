import re
import pandas as pd

def extract_features(urls):
    """
    Extract simple features from URLs for phishing detection.
    Returns a pandas DataFrame.
    """
    data = []
    for url in urls:
        features = {
            "url_length": len(url),
            "count_dots": url.count("."),
            "count_hyphen": url.count("-"),
            "count_at": url.count("@"),
            "https": 1 if url.lower().startswith("https://") else 0,
            "count_digits": sum(c.isdigit() for c in url),
            "count_subdir": url.count("/")
        }
        data.append(features)
    return pd.DataFrame(data)
