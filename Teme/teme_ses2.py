# 1 urmeaza anumite conditii introduse de utilizator

# 2
x = 8
y = 5
print(x // 2)

# 3
if x > 0:
    print('x este pozitiv')
elif x < 0:
    print('x este negativ')
else:
    print('x este neutru')

# 4
if x > -2 and x < 13:
    print('x se afla intre -2 si 13')
else:
    print('x nu se afla intre -2 si 13')

# 5
z = x - y
if z < 5:
    print('Diferenta este mai mica de 5')
else:
    print('diferenta este mai mare de 5')

# 6
print(x not in range(5,27))

# 7
if x == y:
    print('x este egal cu y')
elif x > y:
    print('x este mai mare decat y')
else:
    print('y este mai mare decat x')

# 8
x, y, z = 10, 10, 7
if x == y or y == z or z == x:
    print('triunghi isoscel')
elif x == y == z:
    print('triunghi echilateral')
else:
    print('triunghi oarecare')

# 9
litera = input('Scrie o litera: ').lower()
vocala = 'aeiou'
if litera in vocala:
    print('Litera este o vocala')
else:
    print('Litera este o consoana')

# 10
nota = int(input('Introdu nota: '))
if nota > 9:
    print('A')
elif nota > 8:
    print('B')
elif nota > 7:
    print('C')
elif nota > 6:
    print('D')
elif nota > 4:
    print('E')
elif nota <= 4:
    print('F')

# Ex optionale 1
x = 1927
if 9999 >= x >= 1000:
    print('x are 4 cifre')

# 2
if x <= 999999 and x >= 100000:
    print('x are 6 cifre')

# 3
x = 6
print('par')if x % 2 == 0 else ('impar')

# 4
x, y, z = 4, 6, 8
if x > y and x > z:
    print('x este mai mare')
elif y > x and y > z:
    print('y este mai mare')
else:
    print('z este mai mare')

# 5
if x + y > z:
    if x + z > y:
        if z + y > x:
            print('Triunghiul este valid')
else:
    print('triunghiul nu este valid')

# 6
prop = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Introdu un nr: '))
print(prop[:-x])

# 7
exemplu = 'Coral is either the stupidest animal or the smartest rock'
string_nou = exemplu[:5] + exemplu[-5:]
print(string_nou)

# 8
# 8.1
variabila_rock = exemplu.index('rock')
print(variabila_rock)
# 8.2
print(exemplu[:variabila_rock])