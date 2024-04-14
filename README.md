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

5. Once the script has run successfully, you will find a new Jupyter Notebook file named `P{practical_number}_{topic}.ipynb` (Example: `P3_Magnetic Data Processing.ipynb`) in the repository directory. Open this notebook in Jupyter Lab or Jupyter Notebook to view the generated content.
   
6. Edit `create.py` for custom Jupyter Notebooks!


Feel free to explore and experiment with the practicals using this script! If you encounter any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## Content

| Sr. No. | Date       | Objective/Aim        | Link to .ipynb File |
| ------- | ---------- | -------------------- | ------------------- |
| 1       | 2024-01-01 | Introduction to XYZ  | [](path/to/practical1.ipynb) |
| 2       | 2024-01-08 | Data Analysis with ABC | [](path/to/practical2.ipynb) |
| 3       | 2024-01-15 | Machine Learning Basics | [](path/to/practical3.ipynb) |
| 4       | 2024-01-22 | Neural Networks Fundamentals | [](path/to/practical4.ipynb) |
| 5       | 2024-01-29 | Image Processing Techniques | [P5](P5_Magnetic Data Processing II.ipynb) |
| 6       | 2024-02-05 | Natural Language Processing | [](path/to/practical6.ipynb) |
| 7       | 2024-02-12 | Compute and plot the residual magnetic anomaly along the given magnetic profile data using the polynomial regression (LSM) technique. Also, write your comments on residual and polynomial regression anomaly plots. | [](path/to/practical7.ipynb) |
| 8       | 2024-02-19 | Discuss the effect of magnetic inclination (i) and depth (z) of the sphere body on the total magnetic anomaly profiles. Assume that magnetization only due to induction. | [](path/to/practical8.ipynb) |
| 9       | 2024-02-26 | Discuss the effect of depth (Z), width (T) and direction of arbitrary magnetization (Q) of dyke on the total magnetic anomaly profiles. Assume that magnetization only due to induction. | [P9_Dyke Anomaly Profiles](https://github.com/RiyaSinghRathore/Magnetic-Methods/blob/main/P1_Data%20Analysis.ipynb) |



