import re #will be default


def clean_text(text):
    """
    Cleans up the OCR extracted text by removing non-essential characters and lines
    """
    text = text.lower()
    # Remove unwanted characters, keep letters, digits, and common punctuation
    text = re.sub(r'[^a-zA-Z0-9\s:]', '', text)
    # Remove extra spaces and empty lines
    text = re.sub(r'\s+', ' ', text).strip()
    return text