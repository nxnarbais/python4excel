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
print("Merged dataframe")
print(everyoneDF)

columnNameToMergeOn = "person_number"
mainDF = pd.merge(expensesDF, 
                    everyoneDF, 
                    on = columnNameToMergeOn, 
                    how ='left')

print("Expenses")
print(mainDF)

#####################
# Add today's date column
#####################
dfSize = len(mainDF) # Get number of rows
todayDate = date.today() # Get today's date
newCol = [todayDate for x in range(dfSize)] # Create a list with only today's date
colName = "date"
mainDF[colName] = newCol

#####################
# Add price per unit column
#####################

colName = "price_per_unit"
mainDF[colName] = mainDF["price"] / mainDF["qty"]

# def getCostPerUnit(row):
#     return float(row['price']) / float(row['qty'])
# mainDF[colName] = mainDF.apply (lambda row: getCostPerUnit(row), axis=1)

#####################
# Add full name column
#####################

def getFullName(row):
    return row['person_first_name'] + " " + row['person_last_name']
colName = "full_name"
mainDF[colName] = mainDF.apply (lambda row: getFullName(row), axis=1)

print("Expenses with added columns")
print(mainDF)
