# Utility functions for Phishing URL Detector
def load_urls_from_file(path):
    """Load URLs from a text file, one per line."""
    with open(path, "r") as f:
        return [line.strip() for line in f.readlines()]
