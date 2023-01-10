# studiu echipa 1

nr = int(input('Scrie un nr: '))

for i in range(1, nr + 1):
    print(i * str(i))

# varianta 2 piramida crescatoare
numar_randuri = int(input("Selecteaza numarul de randuri: "))

for i in range(numar_randuri):
    for j in range(i+1):
        print(j+1, end=" ")
    print("")

# studiu echipa 2

tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]

for rand in tastatura_telefon:
    for item in rand:
        print(f'Cifra curenta {item}')

