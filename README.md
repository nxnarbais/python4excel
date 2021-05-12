# Python 4 Excel

This class contains various examples that are used in the lecture to present in practice the concepts of Python for Excel.

In addition, this also includes exercises and solutions to help you improve by practicing. I hope that this will give you some meaningful examples that can be reused in parts for your own projetcs.

## Get started

### First use

The section below is required for first use only.

1. Create an environment of work with `py -m venv venv`
1. Activate the environment `.\venv\Scripts\activate`
1. Install dependencies
    1. `pip install pandas`
    1. `pip install xlsxwriter`
    1. `pip install openpyxl`
    1. `pip install numpy`
    1. `pip install matplotlib`

Note: Creating an environment ensures that all the libraries installed will stay only inside this environment. If someone else or another project needs other libraries this will no affect this project, they will be able to do so withing their own environment.

### Regular use

For any use of those scripts, follow the steps below:

1. Activate the environment created before
    1. `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted`
    1. `.\venv\Scripts\activate`
1. Launch your script with `py path\to\main_script.py`
