
#####################
# First functions
#####################

print("This text")
print(412)
print(4.13)
print(False)

print(type("This text"))
print(type(412))
print(type(4.13))
print(type(False))

x = 5
print(type(x))

#####################
# First IF example
#####################

a = 33
b = 200
if b > a:
    # Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
    print("b is greater than a")

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



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

#####################
# Nested for loops 
#####################

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#####################
# First while examples
#####################

i = 1
while i < 6:
  print(i)
  i += 1