# Python Scripts for Finance

## Install Python on Windows

First install python on your computer:

1. Go to [Python official website](https://www.python.org/downloads/)
1. Download the latest Python version
1. Install Python (Note make sure to tick the option mentioning `PATH`)

Install the environment library with `pip` our library manager:

1. Run `pip install virtualenv`

## Generate SSH key on Windows

[doc](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)

## Create and use Python environment

1. Create env with `py -m venv penv`
1. Install dependencies
    1. `pip install pandas`
    1. `pip install xlsxwriter`
    1. `pip install openpyxl`

Note: Creating an environment ensures that all the libraries installed will stay only inside this environment. If someone else or another project needs other libraries this will no affect this project.

1. Activate environment
    1. `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted`
    1. `.\penv\Scripts\activate`
