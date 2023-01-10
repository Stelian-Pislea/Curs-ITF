# 1
def suma_2_numere(a, b):
    return a + b

print(suma_2_numere(3, 4))

# 2
numar = int(input('Introdu un nr: '))
def numar_par(numar):
    return True if numar % 2 == 0 else False

print(numar_par(numar))

# 3
def nr_total_caractere():
    nume = input('Introdu numele tau complet: ')
    return len(nume)

print(nr_total_caractere())

# 4
def aria_dreptunghiului():
    a = int(input('Introdu lungimea: '))
    b = int(input('Introdu latimea: '))
    return a * b

print(aria_dreptunghiului())

# 5
def aria_cercului():
    raza = float(input('Introdu raza cercului: '))
    aria = 3.14 * raza ** 2
    return aria

print(f'Aria cercului este {aria_cercului()}')

# 6
def caracter_gasit():
    prop = input('Scrie o propozitie: ')
    caracter = input('Scrie carcaterul care vrei sa il gasesti: ')
    return True if caracter in prop else False

print(caracter_gasit())

# 7
def caractere_mici_mari():
    mici = 0
    mari = 0
    exemplu = input('Scrie ceva cu litere mari si mici: ')
    for litere in exemplu:
        if litere.islower():
            mici += 1
        if litere.isupper():
            mari += 1
    print(mici)
    print(mari)

caractere_mici_mari()

# 8
def numere_pozitive():
    numere = [1, 3, 7, -4, -6, -2, 5]
    nr_pozitiv = []
    for numar in numere:
        if numar > 0:
            nr_pozitiv.append(numar)
    return nr_pozitiv

print(numere_pozitive())

# 9
x = int(input('Scrie un nr: '))
y = int(input('Scrie un nr: '))

def doua_numere(x, y):
    if x > y:
        print(f'Primul numar {x} este mai mare decat al doilea numar {y}')
    elif y > x:
        print(f'Al doilea numar {y} este mai mare decat primul numar {x}')
    else:
        print('Numerele sunt egale')

doua_numere(x, y)

# 10
def numar_set(a, b):
    if a not in b:
        b.add(a)
        print(f'Am adaugat numarul nou in set')
        return True
    print(f'Nu am adaugat numarul in set. Acesta exista deja')
    return False
print(numar_set(4, {2, 4, 6}))
