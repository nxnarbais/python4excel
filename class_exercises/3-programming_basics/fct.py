#####################
# With an if function print the content of a variable called myVar if it is positive or the opposite if not
#####################

def getNumberStats(num1, num2):
  avg = (num1 + num2) / 2
  prod = num1 * num2
  return {
    "avg": avg,
    "prod": prod
  }