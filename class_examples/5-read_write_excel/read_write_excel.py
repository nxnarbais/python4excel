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
# Create a dataframe with the content of a sheet
#####################

# Get a dataframe from the first sheet
firstDF = pd.read_excel(myXLSXFile, sheet_name=0)
print("First DF")
print(firstDF)

# Get a dataframe from the sheet called people
sheetName = "people"
peopleDF = pd.read_excel(myXLSXFile, sheetName)
print("PeopleDF")
print(peopleDF)

#####################
# Set file path for new excel file
#####################

# mFolderPath = "C:\\Users\\nxn\\OneDrive\\Documents\\GitHub\\python4accountants\\other_xlsx" # absolute path
myFolderPath = "other_xlsx" # relative path
myFilename = "fromOneToTheOther.xlsx"

myFilePath = myFolderPath + "\\" + myFilename

#####################
# Create a writer
# Tell the write on which tab the dataframe has to be written
# Save the new file
# Set a variable with the name of the file
# Note: All the \ have to be doubled
#####################

writer = pd.ExcelWriter(myFilePath, engine="xlsxwriter")
firstDF.to_excel(writer, sheet_name="some_data_types")
peopleDF.to_excel(writer, sheet_name="some_people")
writer.save()
