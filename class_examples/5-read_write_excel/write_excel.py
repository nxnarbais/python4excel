import pandas as pd

#####################
# Create a simple dataframe
#####################

d = {'col1': [1, 2], 'col2': [3, 4]}
simpleDF = pd.DataFrame(data=d)

#####################
# Set a variable with the path of the excel file
# Set a variable with the name of the file
# Note: All the \ have to be doubled
#####################

# mFolderPath = "C:\\Users\\nxn\\OneDrive\\Documents\\GitHub\\python4accountants\\other_xlsx" # absolute path
myFolderPath = "other_xlsx" # relative path
myFilename = "myFirstExcelFromPython.xlsx"

myFilePath = myFolderPath + "\\" + myFilename

#####################
# Create a writer
# Tell the write on which tab the dataframe has to be written
# Save the new file
# Set a variable with the name of the file
# Note: All the \ have to be doubled
#####################

writer = pd.ExcelWriter(myFilePath, engine="xlsxwriter")
simpleDF.to_excel(writer, sheet_name="myFirstSheet")
writer.save()
