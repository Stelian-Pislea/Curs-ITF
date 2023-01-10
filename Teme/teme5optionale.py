from calendar import monthrange
# Teme optionale
# 1
def zile_luna(an=2022, luna=12):
    return monthrange(an, luna)[1]

print(zile_luna())

# 2
def calculator(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c ,d
a, b, c, d = calculator(10,2)
print(
    f'Suma: {a}\n'
    f'Diferenta: {b}\n'
    f'Inmultirea: {c}\n'
    f'Impartirea: {d}'
)

# 3
lista = [1, 3, 1, 5, 9, 7, 7, 5, 5]
def numara_cifra(lista):
    dct = {}
    for item in lista:
        if item in dct:
            dct[item] += 1
        else:
            dct[item] = 1
    for key, value in dct.items():
        print('% d: % d'%(key, value))


numara_cifra(lista)
# varianta 2
lista = [1, 3, 1, 5, 9, 7, 7, 5, 5]
def numara_cifra(lista):
    dct = {}
    for item in range(10):
        dct[item] = lista.count(item)
    return dct.items()

print(list(numara_cifra(lista)))

# 4
def val_maxim(a, b, c):
    x =  a + b
    y = b + c
    z = a + c
    return max(x,y,z)

print(val_maxim(4,5,3))

# 5
def suma_tuturor_numerelor(n):
    if n == 0:
        return 0
    return n + suma_tuturor_numerelor(n-1)

print(suma_tuturor_numerelor(4))

# Optionale bonus
# 1
def numere_comune():
    list1 = [1, 1, 2, 3]
    list2 = [2, 2, 3, 4]
    a = set(list1)
    b = set(list2)
    c = a.intersection(b)
    print(c)
numere_comune()

# 2
def reducere_pret():
    pret = int(input('Introdu pretul: '))
    reducere = int(input(f'Introdu reducerea: '))
    if reducere > 100:
        print(f'Reducerea mai mare de {reducere}% este invalida!')
        exit(0)
    reducere = reducere / 100
    total = pret - (pret * reducere)

    print(f'Pretul total este {total}')

reducere_pret()