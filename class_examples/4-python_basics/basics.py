
#####################
# First IF example
#####################

a = 33
b = 200
if b > a:
    # Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
    print("b is greater than a")

print("____________________")
#####################
# ELIF
#####################

# ELIF: "if the previous conditions were not true, then try this condition"
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

print("____________________")
#####################
# ELSE
#####################

# ELSE: catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# or you can also use else with elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print("____________________")
#####################
# First FOR Loop
####################

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

print("____________________")
#####################
# Nested for loops 
#####################

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

print("____________________")
#####################
# First WHILE examples
#####################

i = 1
while i < 6:
  print(i)
  i = i + 1