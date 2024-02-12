import cv2
import pytesseract
import pandas as pd


input_image_path = "/Users/riyarathore/Desktop/Screenshot 2024-02-11 at 2.41.26 PM.png"


image = cv2.imread(input_image_path)


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


_, thresholded_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)


extracted_text = pytesseract.image_to_string(thresholded_image)


table_data = [line.split() for line in extracted_text.strip().split('\n')]


df = pd.DataFrame(table_data[1:], columns=table_data[0])

# Save the DataFrame as a .csv file
output_csv_path = "output.csv"
df.to_csv(output_csv_path, index=False)

print(f"Table data saved as {output_csv_path}")
