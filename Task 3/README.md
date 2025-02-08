# Data Analysis and Cleaning Tool

This repository contains a Python command-line tool for analyzing and cleaning a dataset of spare parts. The tool allows users to:

- Analyze spare parts data, including calculations of average prices, part counts, and top expensive/low-stock parts.
- Remove duplicate entries from the dataset.
- Generate a structured report of the analyzed data.

## Environment Setup

You can set up the Python environment using either `venv` or `pipenv`. Follow one of the methods below.

### Using `venv`

1. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**

   run:

   ```bash
   pip install -r requirements.txt
   ```

### Using `pipenv`

1. **Install pipenv (if not already installed):**

   ```bash
   pip install pipenv
   ```

2. **Create and Activate a New Pipenv Environment**

   ```bash
   pipenv shell
   ```

3. **Install Dependencies**

   ```bash
    pipenv install -r requirements.txt
   ```

## How to Use the Tool

This tool provides three main functionalities:

1. **Analyze the Data**  
   Perform data analysis and display results in the console.
   ```bash
   python script.py --analyze
   ```

2. **Remove Duplicate Entries**  
   Cleans the dataset and saves the cleaned version as `cleaned_data.csv`.
   ```bash
   python script.py --remove-duplicates
   ```

3. **Generate a Report**  
   Generates a structured CSV report with data analysis results.
   ```bash
   python script.py --generate-report
   ```

## Code Overview

The script consists of the following functions:

- **`analyze(filename, print_to_console=True)`**
  - Computes:
    - Average price of spare parts by manufacturer.
    - Count of spare parts by compatible car models.
    - Top 10 expensive parts.
    - Average price of parts by category.
    - Top 10 parts with the lowest stock.
  - Prints results to the console if `print_to_console=True`.

- **`remove_dups(filename)`**
  - Removes duplicate entries from the dataset and saves the cleaned data to `cleaned_data.csv`.

- **`generate_report(filename)`**
  - Calls `analyze()` to obtain analysis results and writes them into `report.csv`.

- **`main()`**
  - Parses command-line arguments and calls the appropriate function based on user input.

## Output Files

- `cleaned_data.csv` - A cleaned version of the dataset without duplicate entries.
- `report.csv` - A structured report containing analysis results.

