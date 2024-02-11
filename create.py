import nbformat as nbf
from datetime import datetime

def create(file_name, markdown_content):
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


practical_number = input("Practical Number: ")
topic = input("Topic: ")
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

<h2 style="text-align: center; font-family: Times New Roman; margin-top: 0;"><sup style="font-size: larger;">PRACTICAL - {practical_number}</sup> </h2>

<h3 style="text-align: center; font-family: Times New Roman; margin-top: 0;"><sup style="font-size: larger; font-weight: bold;">{topic}</sup> </h3>

<h4 style="text-align: center; font-family: 'Courier New'; margin-bottom: 0;">{current_date}</h4>
<h4 style="text-align: center; font-family: 'Courier New'; margin-bottom: 0;">Name: Riya Singh Rathore</h4>
<h4 style="text-align: center; font-family: 'Courier New';">Admission Number: 20JE0801</h4>

</body>
</html>
"""

file_name = input("Jupyter Notebook file: ")
create(f"{file_name}.ipynb", markdown_content)
print(f"Jupyter Notebook '{file_name}.ipynb' created successfully.")