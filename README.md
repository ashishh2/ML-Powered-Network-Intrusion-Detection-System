# **ML-Powered Network Intrusion Detection System (NIDS)**

This project implements a machine learning model to classify network traffic as benign or malicious using the CIC-IDS2017 dataset.

## **Project Structure**

nids\_project/  
├── .gitignore          
├── data/                \# (Created by script) Stores the dataset  
├── notebooks/  
│   └── NIDS\_Project.ipynb  \# Main Jupyter Notebook for analysis  
├── scripts/  
│   └── download\_dataset.py \# Script to download and extract the data  
└── requirements.txt    \# Python package dependencies

## **Setup and Usage**

Follow these steps to set up your environment and run the project.

1. **Clone the Repository:**
    ```commandline
   git clone https://github.com/ashishh2/ML-Powered-Network-Intrusion-Detection-System 
   cd ML-Powered-Network-Intrusion-Detection-System
   ```
   
2. Create a Python Virtual Environment:  
   This isolates the project's dependencies from your system's Python.  
    ```zsh
   python -m venv .venv  
   source .venv/bin/activate
    ```

3. Install Python Packages:  
   ```zsh
    pip install -r requirements.txt
   ```

4. Download the Dataset  
   Run the download script from the project's root directory. This will create the data/ folder and populate it with the dataset CSVs.
   ```zsh
   python scripts/download\_dataset.py
   ```

5. Run the Jupyter Notebook  
   Launch Jupyter and open the notebook to run the analysis.
   ```zsh
   jupyter notebook
   ```

   In the Jupyter interface in your browser, navigate to the notebooks/ folder and click on NIDS\_Project.ipynb. You can then run the cells sequentially.