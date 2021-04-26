import pandas as pd
import datetime

#####################
# Set a variable with the path of the excel file
# Note: All the \ have to be doubled
#####################

myFilePath = "other_xlsx\\v1-to_clean.keep.xlsx" # relative path

#####################
# Read the excel file
#####################

myXLSXFile = pd.ExcelFile(myFilePath)

#####################
# Create a dataframe with the content of a sheet
#####################

# Get a dataframe from the sheet called people
sheetName = "company"
companyDF = pd.read_excel(myXLSXFile, sheetName)
print("companyDF")
print(companyDF.dtypes)
print(companyDF)

#####################
# Clean column titles
#####################

print("Existing column names")
print(companyDF.columns)

companyDF.columns = companyDF.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
print("Cleaned column names")
print(companyDF.columns)

#####################
# Convert to string and strip spaces on both sides
#####################


print("Existing column supplier id type")
print(companyDF["supplier_id"])

companyDF['supplier_id'] = companyDF['supplier_id'].astype(str) # Convert to string
companyDF['supplier_id'] = companyDF['supplier_id'].str.strip() # Strip spaces

print("Cleaned column supplier id type")
print(companyDF["supplier_id"])

#####################
# Convert to numeric values
#####################

print("Existing column supplier id type")
print(companyDF['rev._/2021'])

companyDF['rev._/2021'] = pd.to_numeric(companyDF['rev._/2021'], errors='coerce') # Convert all non numbers to NaN

print("Cleaned column supplier id type")
print(companyDF['rev._/2021'])

#####################
# Convert to datetime
#####################

print("Existing column last_updated")
print(companyDF['last_updated'])

companyDF['next_update_us'] = pd.to_datetime(companyDF['next_update_us'], errors='coerce', dayfirst=False)
companyDF['next_update_eu'] = pd.to_datetime(companyDF['next_update_eu'], errors='coerce', dayfirst=True)
companyDF['last_updated_dt'] = pd.to_datetime(companyDF['last_updated'], errors='coerce') # default dayfirst is set to False, see doc: https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html

print("Cleaned column last_updated_dt")
print(companyDF['last_updated_dt'])

#####################
# Filter thanks to cleaned columns
#####################

customDate = datetime.datetime(2019,12,31)
# customDate = datetime.datetime.now() # now

afterDF = companyDF[(companyDF['last_updated_dt'] > customDate)]
beforeDF = companyDF[(companyDF['last_updated_dt'] < customDate)]
invalidDatesDF = companyDF[companyDF['last_updated_dt'].isnull()]

print("Dataframe with invalid dates")
print(invalidDatesDF)

print("Dataframe with previous dates")
print(beforeDF)

#####################
# Drop duplicate, sort and drop NA
#####################

companyDF = companyDF.dropna(subset=['last_updated_dt']) # Remove rows where the conversion did not work
companyDF = companyDF.sort_values(by=['rev._/2021'], ascending=False)
companyDF = companyDF.drop_duplicates(subset ="supplier_id", keep='first')
print("Dataframe after drop and sort")
print(companyDF)

#####################
# Use first two rows as column name
#####################

sheetName = "expenses"
expensesDF = pd.read_excel(myXLSXFile, sheetName, header=[0,1]) # list all the row numbers used for the table head into header. doc: https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html
print(expensesDF.columns)

expensesDF.columns = expensesDF.columns.map('_'.join) # merge the various column headers with a _
print(expensesDF.columns)
