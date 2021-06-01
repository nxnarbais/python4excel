#####################
# Write a for loop, add all the numbers within myList
##################### 

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

total = 0
for num in myList:
  total = total + num
print(total)

#####################
# Write a for loop and an if statement, find the largest number in myList
##################### 

myList = [12, 23, 78, 11, 9, 33]

largestNumber = 0
for num in myList:
  if num > largestNumber:
    largestNumber = num
print(largestNumber)
