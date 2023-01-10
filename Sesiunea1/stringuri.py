from itertools import count


name = 'Dragos'
print(len(name)) #length of the string

print(name.upper()) # convert string to uppercase
print(name.lower()) # convert string to lowercase

name = 'Anamaria'
print(name.count('a'))
print(name.count('s')) # count the number of occurencesof the given character

prop = 'Oare vreau sa merg acolo!\n Unde sa mergi!'
print(prop)
prop = prop.replace('!', '?')
print(prop)
food = 'pizza'
print(food.replace('zz', 't'))

name = 'Jhon'
print(name.index('o'))  #finds the index of the given character
print(name[0])
print(name[-1]) #negativ sign = transversare inversa a stringului


d = 'hello world'
print(d[2:5]) #from 2 to 5(without 5) = slicing
print(d[:5]) # from start to 5
print(d[2:]) # from 2 to end
print(d[-5:-2]) # from -5
print(d[-5:-8]) # -1 => trasversare inversa
print(d[2:8:2]) # 
