#1
# este un loc in memoria calculatorului unde stocam date

#2
animal = 'caine'
kg = 1000
lungime = 2.8
true = True

#3
print(type(animal))
print(type(kg))
print(type(lungime))
print(type(true))

#4
lungime = round(lungime)
print(type(lungime))

#5
print(f'Eu am un {animal} frumos!')
print(f'Un kilogram are {kg} grame.')
print(f'Acest fir are {lungime} metri.')
print(f'{true} friendship is the best.')

#6
nume = input('Care este numele tau? ')
prenume = input('Care este prenumele tau? ')
a = len(nume)
b = len(prenume)
c = a+b
print(f'Numele complet are {c} caractere')

#7
lungimea = 4
latimea = 5
aria = lungimea * latimea
print(f'Aria dreptunghiului este {aria}')

#8
prop = 'Coral is either the stupidest animal or the smartest rock'
print(prop.count('the', 14))

#9
print(prop.replace('the', 'THE',))

#10
assert prop != int
print('Acest exemplu nu are numar intreg')

#Exercitii optionale
#1
cuvant_impar = input('Scrie cifra 4 in litere: ')
print(cuvant_impar[2])

#2
a, b = input('Scrie 2 cuvinte: ').split(); print(a, b)
