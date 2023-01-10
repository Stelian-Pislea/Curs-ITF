import random
dice_roll = random.randint(1, 6)
utilizator = int(input('Introdu un nr de la 1-6: '))
if dice_roll > utilizator:
    print(f'Ai pierdut, ai ales un nr mai mic.Ai ales {utilizator} dar a fost {dice_roll}')
elif dice_roll < utilizator:
    print(f'Ai pierdut, ai ales un nr mai mare.Ai ales {utilizator} dar a fost {dice_roll}')
else:
    print(f'Ai ghicit.Felicitari!Ai ales {utilizator} si zarul a fost {dice_roll}')