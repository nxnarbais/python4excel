# Pricing Condition

## Get started

### First use

1. Create env with `py -m venv penv`
1. Install dependencies
    1. `pip install pandas`
    1. `pip install xlsxwriter`
    1. `pip install openpyxl`

Note: Creating an environment ensures that all the libraries installed will stay only inside this environment. If someone else or another project needs other libraries this will no affect this project.

### Regular use

1. Activate environment
    1. `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted`
    1. `.\penv\Scripts\activate`
1. Copy all the file in *xlsx* format in the folder `raw_xlsx`
1. Launch the script with `py main.py`
1. Visualize the output in the folder `xlsx` in the file called `output.xlsx`
