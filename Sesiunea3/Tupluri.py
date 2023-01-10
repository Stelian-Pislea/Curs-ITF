#tuples are used to store multiple values
# tuples are unchageable

# create
print(20 * '-', 'create', 20 * '-')
fruits = ('apple', 'banana', 'cherry', 'cherry')

#count
print(20 * '-', 'count', 20 * '-')
print(fruits.count('cherry'))

# indexing
print(20 * '-', 'indexing', 20 * '-')
print(fruits[0])
print(fruits[-1])
print(fruits[1:3])

# adding elements
print(20 * '-', 'adding elements', 20 * '-')
fruits +=('pear',)
print(fruits)
fruits2 = ('mango', 'papaya', 'kiwi')
y = list(fruits2)
y.append('orange')
fruits2 = tuple(y)
print(fruits2)

# remove element
print(20 * '-', 'remove element', 20 * '-')
fruits2 = ('mango', 'papaya', 'kiwi')

y = list(fruits2)
y.remove('kiwi')
fruits2 = tuple(y)
print(fruits2)

