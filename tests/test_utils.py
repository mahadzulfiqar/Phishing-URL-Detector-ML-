import pytest
from src.pud.utils import load_urls_from_file

def test_load_urls_from_file(tmp_path):
    file = tmp_path / "urls.txt"
    file.write_text("http://example.com\nhttps://secure.com")
    urls = load_urls_from_file(file)
    assert urls == ["http://example.com", "https://secure.com"]
