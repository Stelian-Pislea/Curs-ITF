# clasele se scriu cu litera mare si fara  (bara jos): NumeClasa
# numele fisierelor in care se afla o clasa au acelasi nume cu clasa doar ca se scrie cu litera mica si '' : nume_clasa

from magic_method import Dog
from class_with_atributes import Dog as DogWithAttributes
from classes.dogs.dog import Dog as Dog2

d = Dog(1, 'Dino')
print(d)

d2 = DogWithAttributes()
print(d2)

d3 = Dog2(1, 'Rex')
print(d3)