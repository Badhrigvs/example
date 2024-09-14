import cv2
import pytesseract
from .text_cleaner import clean_text
from .extract_data import extract_diagnosis


def process_image(image_path):
    # Load the input image
    image = cv2.imread(image_path)
    
    # Preprocess the image: Convert to grayscale and thresholding
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    thresh = cv2.threshold(gray, 0, 256, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    

    
    #OCR software
    '''We can install the OCR software in the main directory also in the case of deployment and can update the path as "C:\\Folder\\Folder\\PS-2" ''' 
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Name\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
    
    # Perform OCR
    text = pytesseract.image_to_string(image=thresh, lang='eng',config=' --psm 6 --oem 3')

    # Clean and preprocess the text
    text = clean_text(text)

    # Look for diagnosis using regular expressions
    diagnosis = extract_diagnosis(text)
    return diagnosis