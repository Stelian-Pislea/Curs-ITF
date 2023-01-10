# 1 sa se scrie o functie care primeste oricati
# parametri si de orice fel si returneaza lista valoriilor argumentelor

def list_all_parameters_values(*args, **kwargs):
    return list(args) + list(kwargs.values())

print(list_all_parameters_values(2,8,-18,a=55))

# sa scrie o functie care primeste ca parametru
# o lista si returneaza inversul acelei liste

def get_list_reversed(lst):
    return lst[::-1]

print(get_list_reversed([1,8,13,55,-14,0]))

# # sa scrie o functie care primeste ca parametru
# doua numere si il returneaza pe cel mai mare

def max_between(a,b):
    return a if a > b else b

print(max_between(5,0))
print(max_between(5,6))

# sa scrie o functie care primeste ca parametru
# o lista si un numar functia va returna de cate ar
# aparea acel numar in lista
#iar daca nu apara deloc va arunca o eroare

def get_count_in_list(lst,a):
    counter = lst.count(a)
    if not counter:
        raise Exception (f'{a} nu se afla in lista.')
    return counter
print(get_count_in_list([1,5,8,13,-14,2,15,1,16,1],1))

# 5
# 5. Sa se scrie o functie care citeste un string de la tastatura
# si returneaza toate caracterele folosite in acel string

def get_unique_characters():
    exemplu = input('Scrie-mi ceva frumos: \n')
    return list(set(exemplu))

print(get_unique_characters())

# 6. Sa se scrie o functie care citeste de la tastatura un text
# si returneaza toate caracterele folosite in text ordonate alfabetic

def get_sorted_unique_characters():
    chars = get_unique_characters()
    chars.sort()
    return chars

print(get_sorted_unique_characters())