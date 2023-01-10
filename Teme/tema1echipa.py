'''
# 1. Exercițiu:
# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă
#  cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot,
#  mai puțin pentru primul și ultimul
# caracter => alAbAlA portocAla.
# o varianta
cuvinte = input('Scrie 2 cuvinte: ')  # Definim exemplu
prima_litera = cuvinte[0]  # Bagam prima litera intr-o variabila
ultima_litera = cuvinte[-1]  # Bagam ultima litera intr-o variabila
mijloc = cuvinte[1: -1]  # Stocam literele din mijloc
print(f'{prima_litera}{mijloc.replace(prima_litera, prima_litera.upper())}{ultima_litera}') # Facem replace in functie de primul caracter si printam

#2 varianta
x = input("Scrie 2 cuvinte: ")
y =(x[0])
print(y)

print(f'{x[0]}{x.replace(y, y.upper())[1:-1]}{x[-1]}')


# 2.Exercițiu:
# - citește un user de la tastatură;
# - citește o parolă;
# - afișează: 'Parola pt user x este  și are x caractere';
# -  se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
# afișeze corect.
# eg: parola abc => ***
# parola abcd => ****
'''

user = input('User: ')
parola = input('Parola: ')
caracter_parola = input('Inlocuieste parola cu un caracter la alegere: ')
print(f'Parola pentru user {user} este {caracter_parola * len(parola)} si are {len(parola)} caractere')
