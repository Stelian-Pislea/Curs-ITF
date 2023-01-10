# exeption are event that might happen durring the execution
# of the cod that python does not know to treat



try:  # test a block of cod for errors
    print(x)
except:  # treats different types of errors
    print('A aparut o eraore.')

##############################################
try:
    a =1/0
    l =[1,2,3]
    l.add(5)
    print(x)
except NameError:
    print('A aparut NameError.')
except AttributeError as ex:
    print(f'Eroarea: {ex}')
except:
    print('Alt tip de eroare')

##############################
try:
    print('Hello1')
except:
    print('A aparut o eroare')
else: # executes if there were no errors
    print('Nici o eroare')

############################################
try:
    print(x)
except:
    print('A aparut o eroare.')
finally: # always executes at the end.
    print('Finnished')
#########################
x = int(input('Introdu un nr: '))
if x < 0:
    raise Exception(f'{x} is bellow 0')
##########################################
