#####################
# With an if function print the content of a variable called myVar if it is positive or the opposite if not
#####################

myVar = 22

if myVar > 0:
  print(myVar)
else:
  print(-myVar)

#####################
# With an if function, print "yes" if the letter "a" is included in a variable called myString otherwise print "no"
##################### 

myString = "hello world"

if "a" in myString:
  print("yes")
else:
  print("no")

#####################
# With an if function, if the value of a variable is above 10, print something and concatenate the number value. If it is above 100, print something else. If it is between 0 and 10, print another thing and if this is below or equal to 0 print one last message
##################### 

myFavoriteNumber = 42

if myFavoriteNumber > 10:
  print("What a big number: " + myFavoriteNumber)
  if myFavoriteNumber > 100:
    print("It is actually above 100, that's a lot")
elif myFavoriteNumber > 0:
  print("Just a single digit?")
else:
  print("Really, a negative number!")