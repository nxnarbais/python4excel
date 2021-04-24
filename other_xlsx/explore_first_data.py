import pandas as pd

#####################
# Set a variable with the path of the excel file
# Note: All the \ have to be doubled
#####################

# myFilePath = "C:\\Users\\nxn\\OneDrive\\Documents\\GitHub\\python4accountants\\other_xlsx\\v0.keep.xlsx" # absolute path
myFilePath = "other_xlsx\\v0.keep.xlsx" # relative path

#####################
# Read the excel file
#####################

myXLSXFile = pd.ExcelFile(myFilePath)

#####################
# List all sheet names
#####################

mySheetNames = myXLSXFile.sheet_names
print("My sheet names")
print(mySheetNames)

#####################
# Create a dataframe with the content of a sheet
#####################

sheetName = "people"
peopleDF = pd.read_excel(myXLSXFile, sheetName)

#####################
# List all the columns
#####################

peopleDFColumns = peopleDF.columns
print("Columns")
print(peopleDFColumns)

peopleDFColumnsList = peopleDFColumns.tolist()
print("Columns (to list)")
print(peopleDFColumnsList)

#####################
# Read the type of each column
#####################

peopleDFColTypes = peopleDF.dtypes
print("Columns and their types")
print(peopleDFColTypes)

#####################
# Quick mathematical description of the numerical columns
#####################

peopleDFNumDescription = peopleDF.describe()
print("Numerical description")
print(peopleDFNumDescription)
