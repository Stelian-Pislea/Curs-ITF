# 1 sa se scrie un program care citeste numere de la tastatura pana se introduce
# numarul 0 pentru fiecare nr introdus se verifica daca este par , iar la final
# se vor afisa intr-  o lista toate numerele
"""
nr = int(input('Introdu un nr:'))
result = []
while nr != 0:
    if nr % 2 == 0:
        result.append(nr)
    nr = int(input('Introdu un nr:'))
print(result)
"""

# ex 2
#sa se scrie un programcare citeste de la tastatura
#si va afisa un dictionar cu toate caracterele
# din text in care cheile vor fi caracterele
#si valoriile daca caracterul este vocala

"""
txt = input('Scrie un text: ')
result = {}
vocale = 'aeiou'

for char in txt:
    if not char.isalpha():
        continue
    char_type = 'vocala' if char in vocale else 'consuana'
    result[char] = [char_type]
print(result)
"""
# ex 3
#sa se scrie un program care citeste de la
# tastatura o lista de fructe iar la final
#le va afisa doar pe cele care incep cu a

"""
fruit = None
result = []
while fruit != '':
    fruit = input('Scrie un fruct: ')
    if fruit.startswith('a'):
        result.append(fruit)
print(result)
"""

"""
 4 fie ductionarul dct. Fiecare element din dictionar 
 sa se afiseze sub format -> valoare pe un rand nou 
"""
"""
dct = {'a': 6, 'b': 9}

for key, value in dct.items():
    print(f'{key} -> {value}')
"""

"""
se se scrie un program ca re cisteste de la tastura 
6 numere si le afiseaza pe cele mai mari decat 9
"""
"""
result = []
for i in range(6):
    numar = int(input('Introdu un nr: '))
    if numar > 9:
        result.append(numar)
print(result)
"""

"""
6. sa scrie un  program care citeste de la 
tastatura litere . la final se vor afisa toate 
literele unice.
"""


"""
letters = set()
while True:
    char = input(' Introdu o litera: ')
    if not char.isalpha():
        break
    letters.add(char)
lst = list(letters)
lst.sort()

print(lst)
"""

"""
7. fie lista 1 2 3 6 5 10 sa scrie un program care creeaza
un dictionar care sa contina ca si cheie elementele
din lista iar ca valori index - ul care se afla acel element
"""
lst = [1, 2, 3, 6, 5, 10]
dct = {}
for i in range(len(lst)):
    dct[lst[i]] = i

print(dct)

# v2
for index, elem in enumerate(lst):
    dct[elem] = index
print(dct)