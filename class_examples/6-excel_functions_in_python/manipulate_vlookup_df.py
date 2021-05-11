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
expensesDF = pd.read_excel(myXLSXFile, "expenses")

#####################
# Test different variants of VLOOKUP
#####################

columnNameToMergeOn = "person_number"

# Inner join: Inner join produces an output data frame of only those rows for which the condition is satisfied in both the rows. To perform inner join you may specify inner as a keyword in how.
inner_join = pd.merge(expensesDF, 
                      peopleDF, 
                      on = columnNameToMergeOn, 
                      how ='inner')
print("Inner join")
print(inner_join)

# Left join: Left join operation provides all the rows from 1st dataframe and matching rows from the 2nd dataframe. If the rows are not matched in the 2nd dataframe then they will be replaced by NaN.
left_join = pd.merge(expensesDF, 
                      peopleDF, 
                      on = columnNameToMergeOn, 
                      how ='left')
print("Left join")
print(left_join)

# Right join: Right join is somewhat similar to left join in which the output dataframe will consist of all the rows from the 2nd dataframe and matching rows from the 1st dataframe. If the rows are not matched in 1st row then they will be replaced by NaN
right_join = pd.merge(expensesDF, 
                      peopleDF, 
                      on = columnNameToMergeOn, 
                      how ='right')
print("Right join")
print(right_join)

# Outer join: Outer join provides the output dataframe consisting of rows from both the dataframes. Values will be shown if rows are matched otherwise NaN will be shown for rows that do not match.
outer_join = pd.merge(expensesDF, 
                      peopleDF, 
                      on = columnNameToMergeOn, 
                      how ='outer')
print("Outer join")
print(outer_join)

# More: # https://www.geeksforgeeks.org/how-to-do-a-vlookup-in-python-using-pandas/
