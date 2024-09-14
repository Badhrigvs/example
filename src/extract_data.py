import re #will be default

def extract_diagnosis(text):
    """
    Extracts the provisional diagnosis or diagnosis from the OCR text
    """
    
    # Regex pattern to find diagnosis information after certain keywords
    diagnosis_pattern = re.compile(r'(provisional diagnosis|diagnosis | provisional diagnosts)[:\s]*([\w\s]+)')
    
    match = diagnosis_pattern.search(text)
    
    if match:
        diagnosis = match.group(2).strip()
        stop_words = ['i','icd','i.','i. ' ,'i.  icd','i. icd 10','i. icd 10 code']

        # Split diagnosis into words and check for stop words
        words = diagnosis.split()
        for word in stop_words:
            if word.lower() in words:
                # Stop extracting text after encountering a stop word
                diagnosis = ' '.join(words[:words.index(word.lower())])
                return diagnosis.strip()
        # Check for and clean up noisy text
        if len(diagnosis.split()) > 2:  # If it looks long enough to be a diagnosis
            return diagnosis
    return "Diagonasis not found"
