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

columnNameToMergeOn = "person_number"
mainDF = pd.merge(expensesDF, 
                    everyoneDF, 
                    on = columnNameToMergeOn, 
                    how ='left')

# print("Expenses")
# print(mainDF)

#####################
# Filter only the rows with a high price
#####################

highPriceDF = mainDF[mainDF['price'] > 70]
print("Highest expenses")
print(highPriceDF)

#####################
# Filter only the apples
#####################

appleDF = mainDF[mainDF['fruit'] == "apple"]
print("Apple expenses")
print(appleDF)

#####################
# Filter only the rows with apples and a high price
#####################

highestPriceAppleDF = mainDF[(mainDF['fruit'] == "apple") & (mainDF['price'] > 50)]
print("Highest apple expenses")
print(highestPriceAppleDF)

#####################
# Filter only the apples and the peers
#####################

appleAndPeerDF = mainDF[(mainDF['fruit'] == "apple") | (mainDF['fruit'] == "peer")]
print("Apple and peer expenses")
print(appleAndPeerDF)

#####################
# Filter lines with empty firstname
#####################

noFirstName = mainDF[mainDF['person_first_name'].isnull()]
print("No first name")
print(noFirstName)

#####################
# Sort by city
#####################

sortByCityDF = mainDF.sort_values(by=['city'], ascending=True)
print("Sorted by city")
print(sortByCityDF)

#####################
# Sort by price and city
#####################

sortByCityAndPriceDF = mainDF.sort_values(by=['price'], ascending=True).sort_values(by=['city'], ascending=True)
print("Sorted by city and price")
print(sortByCityAndPriceDF)
