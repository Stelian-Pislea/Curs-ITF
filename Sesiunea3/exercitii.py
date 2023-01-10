# sa scrie un program care citeste un test de la tastatura si afiseaza o lista cu fiecare caracter
# in ordinea aparitiei in text

# text = list(input('Sa  se scrie un text: '))
# text.reverse()
# print(text)
# chrs = [text.pop(-2), text.pop(7)]
# print(chrs)
# print(text)

'''
Sa scrie un program care citeste numele, email si vrasta unei pesoane de la tastatuta
si adauga datele intr-un dictionar pe care il afiseaza.
'''
#
# numele = input('Numele: ')
# email = input('Email:')
# vrasta = int(input('Vrasta:'))
#
# details = {
#     'nume' : numele,
#     'email': email,
#     'vrasta': vrasta
# }
# print(details)
#
# modyfy = input('Vrei sa modifici datele(y/n? ')
# if modyfy == 'y':
#     key_to_modyfy = input('Ce vrei sa modifici? ')
#     if key_to_modyfy not in details:
#         print('Nu exista aceasta valuare')
#         exit(0)
#     value_to_modyfy = input("Introdu noua valoare")
#     value_to_modyfy = int(value_to_modyfy) if key_to_modyfy == 'vrasta' else value_to_modyfy
#     details[key_to_modyfy] = value_to_modyfy
#
# print(details)

#  fie seturile
# toate elemetele care apar in set 1 si nu apar in set 2
#
set1 = {'yellow','orange', 'black'}
set2 = {'orange', 'blue', 'pink'}
print(set1 - set2)
print(set1 & set2)
print(set1 ^ set2)
