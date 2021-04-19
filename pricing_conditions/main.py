import pandas as pd
import openpyxl
from os import listdir
from os.path import isfile, join

xlsxFolderPath = "xlsx"
xlsxFolderPathRaw = "raw_xlsx"

def getFilesFromDirectory(selectedPath):
    return [f for f in listdir(selectedPath) if isfile(join(selectedPath, f))]

filesToHandle = getFilesFromDirectory(xlsxFolderPathRaw)

def getConditionValue(sheet):
    condition = sheet.cell(1, 1).value
    return condition.split(": ")[1].strip()

mainDF = pd.DataFrame() # Create empty dataframe

for filename in filesToHandle:

    # Get condition value and delete first row
    print("Start processing {}...".format(filename))
    wb = openpyxl.load_workbook(xlsxFolderPathRaw + "\\" + filename)
    sheet = wb.worksheets[0]
    conditionValue = getConditionValue(sheet)
    print("Condition value {}".format(conditionValue))
    print("Start removing first row and saving file...")
    sheet.delete_rows(1, 1)
    newFilePath = xlsxFolderPath + "\\" + filename
    wb.save(newFilePath)
    print("First row deleted and file saved at {}".format(newFilePath))

    # Get dataframe from first sheet
    print("Start reading file at {}...".format(newFilePath))
    xlsx = pd.ExcelFile(newFilePath)
    df = pd.read_excel(xlsx, sheet_name=0)

    # Normalize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    colNames = df.columns.tolist()
    print("Column names have been normalized {}".format(colNames))

    # Add column with the conditionValue
    dfSize = len(df)
    newCol = [conditionValue for x in range(dfSize)]
    colName = "condition_value"
    df[colName] = newCol
    print("Condition value has been added to column {}".format(colName))
    
    # Create product code with concatenation
    df['inv._pty'] = df['inv._pty'].str.strip() # Remove unecessary spaces
    def getProductCode(row):
        return str(row['inv._pty']) + str(row['material'])
    colName = "product_code"
    df[colName] = df.apply (lambda row: getProductCode(row), axis=1)
    print("Product code has been added to column {}".format(colName))

    # Create new cost per unit
    def getCostPerUnit(row):
        if (not ((isinstance(row['amount'], float) or isinstance(row['amount'], int)) and (isinstance(row['per'], float) or isinstance(row['per'], int)))):
            return 0
        return float(row['amount']) / float(row['per'])
    colName = "cost_per_unit"
    df[colName] = df.apply (lambda row: getCostPerUnit(row), axis=1)
    print("Cost per unit has been added to column {}".format(colName))

    mainDF = mainDF.append(df)

print("Main dataframe is now complete")
print(mainDF)

# Remove duplicates
mainDF['valid_from'] = pd.to_datetime(mainDF['valid_from'], errors='coerce') # Convert column valid_from to datetime
mainDF = mainDF.dropna(subset=['valid_from']) # Remove rows where the conversion did not work
mainDF = mainDF.sort_values(by=['valid_from'])
mainDF = mainDF.drop_duplicates(subset ="product_code", keep='first')
print("Duplicates have been removed")
print(mainDF)

# Write output to final excel file
print("Start writing to ouput file...")
filename = "output.xlsx"
writer = pd.ExcelWriter(xlsxFolderPath + "\\" + filename, engine="xlsxwriter")
mainDF.to_excel(writer, sheet_name="main")
writer.save()
