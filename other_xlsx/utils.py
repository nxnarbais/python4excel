from os import listdir
from os.path import isfile, join

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
