import nbformat as nbf
from datetime import datetime
import sys
import re

def create(practical_number, topic):
    # Convert practical number to roman numeral
    roman_numerals = {
        1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 
        6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 
        11: 'XI', 12: 'XII', 13: 'XIII', 14: 'XIV', 15: 'XV'
    } 

    roman_practical_number = roman_numerals.get(int(practical_number), 'Invalid')

    if roman_practical_number == 'Invalid':
        print("Error: Invalid practical number. Please enter a number between 1 and 15.")
        sys.exit(1)

    # Construct file name
    file_name = f"P{practical_number}.ipynb"

    current_date = datetime.now().strftime("%B %d, %Y")

    markdown_content = f"""\
<!DOCTYPE html>
<html>
<head>
<style>
  h1, h2, h4 {{
    margin-bottom: 0; /* Reduce the bottom margin */
  }}
</style>
</head>
<body>

<h1 style="text-align: center; font-family: Times New Roman; margin-bottom: 0;">M<span style="font-size: x-large;">AGNETIC</span> M<span style="font-size: x-large;">ETHODS</span> L<span style="font-size: x-large;">AB</span> (GPC522)</h1>

<h2 style="text-align: center; font-family: Times New Roman; margin-top: 0;"><sup style="font-size: larger;">PRACTICAL - {roman_practical_number}</sup> </h2>

<h3 style="text-align: center; font-family: Times New Roman; margin-top: 0;"><sup style="font-size: larger; font-weight: bold;">{topic}</sup> </h3>

<h4 style="text-align: center; font-family: 'Courier New'; margin-bottom: 0;">{current_date}</h4>
<h4 style="text-align: center; font-family: 'Courier New'; margin-bottom: 0;">Name: Riya Singh Rathore</h4>
<h4 style="text-align: center; font-family: 'Courier New';">Admission Number: 20JE0801</h4>
<h4 style="text-align: center; font-family: 'Times New Roman';">Visit: <a href="https://github.com/RiyaSinghRathore/Magnetic-Methods";">https://github.com/RiyaSinghRathore/Magnetic-Methods</a> for the Lab Repository</h4>

</body>
</html>
"""

    notebook_content = nbf.v4.new_notebook()
    markdown_cell = nbf.v4.new_markdown_cell(markdown_content)
    notebook_content.cells.append(markdown_cell)

    import_cell = nbf.v4.new_code_cell(
        """\
# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
""")
    notebook_content.cells.append(import_cell)

    with open(file_name, 'w') as f:
        nbf.write(notebook_content, f)

    print(f"Jupyter Notebook '{file_name}' created successfully.")

# Check if inputs are provided in the command line
if len(sys.argv) > 1:
    inputs = sys.argv[1:]
    if len(inputs) != 2:
        print("Error: Invalid number of inputs. Please provide all required inputs in the format '--<practical_number> --<topic>'")
        sys.exit(1)
else:
    print("Error: No inputs provided. Please provide all required inputs in the format '--<practical_number> --<topic>'")
    sys.exit(1)

practical_number, topic = inputs
practical_number = re.sub('[^0-9]', '', practical_number)  # Extract only digits
topic = topic.strip('-').strip()  # Remove leading and trailing hyphens and whitespaces

create(practical_number, topic)
