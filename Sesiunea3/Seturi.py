# sets are used to store multiple unique items in a single value

# create
fruits = {'apple', 'banana', 'cherry'}
cars = {} # atentie! acesta este un dictionar!
car = set()

# add elements
print(20 * '-', 'add elements', 20 * '-')
fruits.add('pear')
print(fruits)
fruits.add('pear')
print(fruits)

tropical = {'papaya', 'mango'}
fruits.update(tropical)
print(fruits)

my_list = ['kiwi', 'orange']
fruits.update(my_list)
print(fruits)

# remove
print(20 * '-', 'remove', 20 * '-')
fruits.remove('mango')
print(fruits)
fruits.discard('pear')
print(fruits)
#fruits.remove('grapes') # can 't eliminate elements in set
fruits.discard('grapes')
print(fruits)


fruits.pop() # remove random element
print(fruits)

a = fruits.pop()
print(a)

# remove all elements
print(20 * '-', 'remove all elements', 20 * '-')
a = {1, 2, 3}
a.clear()
print(a)

# join
print(20 * '-', 'join', 20 * '-')
s1 ={'a', 'b', 'c'}
s2 = {1, 2, 3}
s3 = s1.union(s2)
print(s3)
print(s1|s2)

# 3 intersection
print(20 * '-', 'intersection', 20 * '-')
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.intersection(y)
print(z)

print(x & y)

# diference
print(20 * '-', 'indexing', 20 * '-')
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.difference(y)
print(z)
print(x - y)

# simetric diference
print(20 * '-', 'simetric diference', 20 * '-')
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.symmetric_difference(y)
print(z)
print(x ^ y)

# issubset,issuperset
print(20 * '-', 'issubset,issuperset', 20 * '-')
a = { 1, 2, 3, 4, 5}
b = {1, 2, 3}
print(b.issubset(a))
print(a.issuperset(b))