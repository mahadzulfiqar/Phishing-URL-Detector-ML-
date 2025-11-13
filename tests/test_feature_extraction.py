import pytest
from src.pud.feature_extraction import extract_features

def test_extract_features_basic():
    urls = ["http://example.com", "https://secure.com/path"]
    df = extract_features(urls)
    assert df.shape[0] == 2
    assert "url_length" in df.columns
    assert "https" in df.columns
