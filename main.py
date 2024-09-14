import os  #will be default
import sys  #will be default
import pandas as pd
from src.process_img import process_image



def process_folder(folder_path):
    
    output_data = []  # Collect data for CSV
    for filename in os.listdir(folder_path):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(folder_path, filename)
            diagnosis = process_image(image_path)
            output_data.append({'file_name': filename, 'provisional diagnosis': diagnosis})
    
    # Convert the list to a DataFrame and save it
    output_df = pd.DataFrame(output_data)
    output_df.to_csv('output3.csv', index=False)



def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <folder_path>")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    process_folder(folder_path)

if __name__ == "__main__":
    main() 
