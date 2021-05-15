from os import listdir
from os.path import isfile, join
import pandas as pd
import openpyxl

#####################
# List all files in folder
#####################

myFolderPath = "other_xlsx"

def getFilesFromDirectory(selectedPath):
    return [f for f in listdir(selectedPath) if isfile(join(selectedPath, f))]

allFilesInDirectory = getFilesFromDirectory(myFolderPath)
print(allFilesInDirectory)

allXlsxFilesInDirectory1 = [filename for filename in allFilesInDirectory if filename.endswith("xlsx")]
print(allXlsxFilesInDirectory1)

def isXlsxFile(filename):
	return filename.endswith("xlsx")
an_iterator = filter(isXlsxFile, allFilesInDirectory)
allXlsxFilesInDirectory2 = list(an_iterator)
print(allXlsxFilesInDirectory2)

an_iterator = filter(lambda filename: filename.endswith("xlsx"), allFilesInDirectory)
allXlsxFilesInDirectory3 = list(an_iterator)
print(allXlsxFilesInDirectory3)

#####################
# Read from a CSV file
#####################

myDF = pd.read_csv("myfile.csv")

#####################
# Delete the first row
#####################

filename = "v0.keep.xlsx"
wb = openpyxl.load_workbook(filename)
sheet = wb.worksheets[0]
firstCell = sheet.cell(1, 1).value
sheet.delete_rows(1, 1)
newFilePath = "modified_" + filename
wb.save(newFilePath)

#####################
# Reuse code with functions
#####################

def getPeopleDFFromExcel():
    myFilePath = "v0.keep.xlsx" # relative path
    myXLSXFile = pd.ExcelFile(myFilePath)
    return pd.read_excel(myXLSXFile, "people")

peopleDF = getPeopleDFFromExcel()
