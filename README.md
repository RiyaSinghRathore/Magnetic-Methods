# GPC522: Magnetic Methods Lab

This repository contains a Python script to automatically generate Jupyter Notebook files for conducting practicals in the Magnetic Methods Lab.

## Usage

To use the script, follow these steps:

1. Clone this repository to your local machine.

2. Navigate your directory to the cloned repository.

3. Execute the Python script `create.py` in your terminal or command prompt.

    ```
    python3 create.py --<practical_number> --<topic>
    ```

   Replace `<practical_number>` with the desired practical number (1 to 15) and `<topic>` with the topic of the practical.

   Example:
    ```
    python3 create.py --3 --"Magnetic Data Processing"
    ```

5. Once the script has run successfully, you will find a new Jupyter Notebook file named `P{practical_number}_{topic}.ipynb` (Example: `P3_Magnetic Data Processing`) in the repository directory. Open this notebook in Jupyter Lab or Jupyter Notebook to view the generated content.
   
6. Edit `create.py` for custom Jupyter Notebooks!


Feel free to explore and experiment with the practicals using this script! If you encounter any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.



