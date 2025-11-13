import pytest
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from src.pud.model import predict_urls

def test_predict_urls_basic():
    data = pd.DataFrame({"url_length": [10, 20], "count_dots": [1,2],
                         "count_hyphen":[0,1], "count_at":[0,0],
                         "https":[0,1], "count_digits":[0,1], "count_subdir":[1,2]})
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(data, [0,1])
    preds = predict_urls(model, data)
    assert preds == ["Safe", "Phishing"]
