import random
# 1
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun',
'Fiat', 'Trabant', 'Opel']

for i in range(len(masini)):
    print(f'Masina mea preferata este {masini[i]}')

for masina in masini:
    print(f'Masina mea preferata este {masina}')

i = 0
while i < len(masini):
    print(f'Masina mea preferata este {masini[i]}')
    i += 1

# 2
for i in range(1, len(masini)-1):
    masini[i] = masini[i].upper()
else:
    print(masini)

# 3

cumparator = 'Mercedes'

for masina in masini:
    if  cumparator in  masini:
        print('Am gasit masina dorita de dvs')
        break
else:
    print(f'Am gasit masina {cumparator}. Mai cautam')

# 4

for masina in masini:
    if masina == 'Trabant' or masina == 'Lastun':
        continue
    print(f'S-ar putea sa va placa: {masina}')

# 5

masini_vechi = []

for masina in masini:
    if 'Trabant' in masina or 'Lastun' in masina:
        masini_vechi.append(masina)

for i in range(len(masini)):
    if masini[i] == 'Lastun' :
        masini[i] = 'Tesla'
    if masini[i] == 'Trabant':
        masini[i] = 'Tesla'

print(masini_vechi)
print(masini)

# 6
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
buget = 15000

for key, value in pret_masini.items():
    if value <= buget:
        print(key)

for key, value in pret_masini.items():
    if value <= buget:
        print(f'{key} -> {value}')

for key, value in pret_masini.items():
    if value <= buget:
        print(f'Pentru un buget de sub {buget} puteti alege masina {key}')

# 7

numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
x = 0
for numar in numere:
    if numar == 3:
        x += 1
print(x)

# 8
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
total = 0
for numar in numere:
    total += numar
print(total)

# 9

numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

mare = numere[0]
for numar in numere:
    if numar > mare:
        mare = numar
print(mare)

# 10
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

lista_noua = [- abs(numar) for numar in numere]
print(lista_noua)

# varianta 2

lista_noua = []

for numar in numere:
    lista_noua.append(-abs(numar))
print(lista_noua)

# Ex optionale
# 1
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    if numar % 2 != 0:
        numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    if numar < 0:
        numere_negative.append(numar)
print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)

# 2
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

for numar in range(len(alte_numere)):
    for i in range(numar + 1, len(alte_numere)):
        if alte_numere[numar] > alte_numere[i]:
            alte_numere[numar],  alte_numere[i] = alte_numere[i],  alte_numere[numar]
print(alte_numere)