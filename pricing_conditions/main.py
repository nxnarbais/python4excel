import pandas as pd
import openpyxl
from os import listdir
from os.path import isfile, join
import datetime

xlsxFolderPath = "xlsx"
xlsxFolderPathRaw = "raw_xlsx"

# xlsxFolderPath = "test\\xlsx"
# xlsxFolderPathRaw = "test\\raw_xlsx"

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
    print(df.dtypes)

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
    if df['inv._pty'].dtypes != "float" and df['inv._pty'].dtypes != "int64":
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

# Convert the content of the valid_from column to a date type
print("Converting valid_from column to type date")
mainDF['valid_from_dt'] = pd.to_datetime(mainDF['valid_from'], errors='coerce') # doc on pd.to_datetime https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html
print(mainDF.dtypes)
print("Dataframe with invalid dates")
invalidDatesDF = mainDF[mainDF['valid_from_dt'].isnull()]
print(invalidDatesDF)

# Split dataframe based on valid_from future dates
dateToLimit = datetime.datetime(2021,12,31)
# dateToLimit = datetime.datetime.now() # now
futureDatesDF = mainDF[(mainDF['valid_from_dt'] > dateToLimit)]
keepDF = mainDF[(mainDF['valid_from_dt'] < dateToLimit)]
print("Dataframe with future dates")
print(futureDatesDF)

# Remove duplicates
keepDF = keepDF.dropna(subset=['valid_from_dt']) # Remove rows where the conversion did not work
keepDF = keepDF.sort_values(by=['valid_from_dt'], ascending=False)
keepDF = keepDF.drop_duplicates(subset ="product_code", keep='first')
print("Duplicates have been removed")
print(keepDF)

# Write output to final excel file
print("Start writing to output file...")
filename = "output.xlsx"
writer = pd.ExcelWriter(xlsxFolderPath + "\\" + filename, engine="xlsxwriter")
keepDF.to_excel(writer, sheet_name="main")
mainDF.to_excel(writer, sheet_name="all")
futureDatesDF.to_excel(writer, sheet_name="future_dates")
invalidDatesDF.to_excel(writer, sheet_name="wrong_dates")
writer.save()

# Get all inv._pty
keepDF['inv._pty'] = keepDF['inv._pty'].astype(str).str.strip() # Convert as string and remove spaces
invParties = keepDF["inv._pty"].unique()

# Write one file per inv._pty
for invParty in invParties:
    filename = "output_{}.xlsx".format(invParty)
    writer = pd.ExcelWriter(xlsxFolderPath + "\\" + filename, engine="xlsxwriter")
    keepDF[keepDF['inv._pty'] == invParty].to_excel(writer, sheet_name="main")
    writer.save()
    print("Saved output file for inv.Pty: {}".format(invParty))
