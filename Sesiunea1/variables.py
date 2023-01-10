#variable => a container from memory for storing values

# creating a variable
x = 5
y = "Jhon"
print(x)
print(y)

x = y
print(x)

# 2. naming a variable
'''
a) a variable must start with a letter or the underscore character:_
b) a variable cannot start with a number
c)a variable name can only contain alpha-numeric charcaters and _ (A-Z, a-z, 0-9)
d)variablenames are case-sensitive
'''
# this way
myvar = 5
my_var = 5
_my_var = 5
myVar = 5
MYVAR = 5
myvar2 = 5
# NOT THIS WAY
#
#2myvar = 5
#my-var = 5
#my var = 5

# many values to multiple variable
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)
k, h, j = x, "mere", True
print(k, h, j)

# 4. One value to multiples variables
x = y = z = 'portocala'
print(x, y, z)