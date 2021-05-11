import pandas as pd
from datetime import date

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
# Create a dataframe with the content of a sheet
#####################

peopleDF = pd.read_excel(myXLSXFile, "people")
managersDF = pd.read_excel(myXLSXFile, "managers")
expensesDF = pd.read_excel(myXLSXFile, "expenses")

everyoneDF = pd.DataFrame()
everyoneDF = everyoneDF.append(peopleDF)
everyoneDF = everyoneDF.append(managersDF)

columnNameToMergeOn = "person_number"
mainDF = pd.merge(expensesDF, 
                    everyoneDF, 
                    on = columnNameToMergeOn, 
                    how ='left')

# print("Expenses")
# print(mainDF)

#####################
# First pivot tables
#####################

pivotDF = mainDF.pivot_table(index='person_number', values=['qty', 'price'], aggfunc='sum')
print(pivotDF)

pivotDF = mainDF.pivot_table(index=['person_number','person_first_name','person_last_name'], values=['qty', 'price'], aggfunc=['sum', 'mean'])
print(pivotDF)

pivotDF = mainDF.pivot_table(index='fruit', values=['qty', 'price'], aggfunc=['sum', 'mean'])
print(pivotDF)