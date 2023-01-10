# 1. Citește de la tastatură un string
# Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat

exemplu = input('Scrie un cuvant: ').lower()
assert exemplu[0] == exemplu[-1]

# 2 Având stringul '0123456789'
# ● Afișează doar numerele pare
# ● Afișează doar numerele impare
# (hint: folosește slicing, controlează din pas)

cifre_string = ('0123456789')
numar_par = cifre_string[0:-1:2]
print(numar_par)
numar_impar = cifre_string[1::2]
print(numar_impar)

# varianta 2
cifre_stringg = input('Scrie un sir de numere: ')
lista_string = list(map(int, cifre_stringg))

lista_pare = []
lista_impare = []
for i in lista_string:
    if i % 2 == 0:
        lista_pare.append(i)
    else:
        lista_impare.append(i)

print(lista_pare)
print(lista_impare)
