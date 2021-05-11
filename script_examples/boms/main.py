import pandas as pd

# Accesing the excel file
filename = r"20201120 BOM's updated chemicals usage.xlsx"
xl = pd.ExcelFile(filename)

# Read tabs and remove first 4
sheetNames = xl.sheet_names[4:]
# print(sheetNames)

# Merge DF
mainDF = pd.DataFrame() # Create empty dataframe
for sheetName in sheetNames:
    df = pd.read_excel(xl, sheetName, header=[0,1])
    df.columns = df.columns.map('_'.join)
    dfSize = len(df)
    newCol = [sheetName for x in range(dfSize)]
    colName = "tab"
    df[colName] = newCol
    mainDF = mainDF.append(df)

# Write to another excel file
outputFilename = r"output.xlsx"
writer = pd.ExcelWriter(outputFilename, engine="xlsxwriter")
mainDF.to_excel(writer, sheet_name="main")
writer.save()
