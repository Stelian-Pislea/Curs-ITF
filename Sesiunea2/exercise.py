#1. ssa sescrie un program care citeste un text de la tastatura
# si verifica daca are lungimea numar par sau impar(rez in 2 moduri
text = input('Introdu un text: ')
if len(text) % 2 == 0:
    print('lungimea textului este numar par')
else:
    print('lungimea textului impar')

# varianta 2 shorthand
paritate = 'par' if len(text) % 2 == 0 else 'impar'
print(f'Lungimea textului este numar {paritate}')


# 2 se citesc 2 numere de la tastatura sa se afiseze cuvantul 'Adevarat'
# daca ambele au acelasi semn ,altfel se afiseaza cuvantul Fals
x = int(input('introdu un nr: '))
y = int(input('introdu un nr: '))
if (x > 0 and y > 0) or (x < 0 and y < 0):
    print('Adevarat')
else:
    print('Fals')