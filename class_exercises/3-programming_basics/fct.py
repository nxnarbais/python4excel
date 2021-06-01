#####################
# Write a function called `printMy3Vars` that takes 3 parameters and simply print them in order one below the other.
#####################

def printMy3Vars(var1, var2, var3):
    print(var1)
    print(var2)
    print(var3)

#####################
# Write a function called getNumberStats that takes 2 arguments and return an dictionary with a key `avg` containing the average and another key `prod` containing the multiplication of the two numbers.
#####################

def getNumberStats(num1, num2):
  avg = (num1 + num2) / 2
  prod = num1 * num2
  return {
    "avg": avg,
    "prod": prod
  }