import random
numar_secret = random.randint(1, 30)
numar_ghicit = None

while True:
    user_numar = int(input('Alege un nr intre 1 -30: '))
    if user_numar < numar_secret:
        print('Nr secret e mai mare')
    elif user_numar > numar_secret:
        print('Nr secret e mai mic')
    else:
        print('Felicitari! Ai ghicit')