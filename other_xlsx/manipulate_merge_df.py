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

peopleDF = pd.read_excel(myXLSXFile, "people")
managersDF = pd.read_excel(myXLSXFile, "managers")

#####################
# Create an empty dataframe
#####################
everyoneDF = pd.DataFrame()

#####################
# Merge two dataframes
#####################

everyoneDF = everyoneDF.append(peopleDF)
everyoneDF = everyoneDF.append(managersDF)
print("Merged dataframe")
print(everyoneDF)
