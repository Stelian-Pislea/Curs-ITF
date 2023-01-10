from datetime import date
from tabulate import tabulate
"""
Exerciții Opționale 
1. Clasa Factură
Atribute: seria (va fi constantă, nu trebuie constructor, 
toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fără serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)

● generează_factura() - va printa tabelar dacă reușiți
Factura seria x număr y
Data: generează automat data de azi
Produs | cantitate | preț bucată | Total
Telefon |    7     |         700 | 49000
"""

class Factura:
    serie = 'RoF'
    numar = 12345
    nume_produs = 'Telefon'
    cantitate = 7
    pret_bucata = 700

    def __init__(self, numar, nume_produs, cantitate, pret_bucata, total):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_bucata = pret_bucata
        self.total = total


    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_bucata = pret

    def  schimba_nume_produs(self, produs):
        self.nume_produs = produs


produs = Factura(12345, 'Telefon', 7, 700, 0)
produs.cantitate = 10
produs.schimba_pretul(800)
produs.schimba_nume_produs('Televizor')
produs.total = produs.cantitate * produs.pret_bucata
print(f'Factura seria {produs.serie} numar {produs.numar}')
print(f'Data: {date.today()}')
tabel = [['Produs', 'Cantitate', 'Pret bucata', 'Total'],
        [produs.nume_produs, produs.cantitate, produs.pret_bucata, produs.total]]
print(tabulate(tabel, headers='firstrow'))


"""
v2
produs2 = Factura(123456, 'Televizor', 10, 950, 0)
print(tabulate(tabel, headers='firstrow'))
print(40 * '*')
print(f'Factura seria {produs.serie} numar {produs2.numar}')
print(f'Data: {date.today()}')
produs2.total = produs2.cantitate * produs2.pret_bucata
tabel = [['Produs', 'Cantitate', 'Pret bucata', 'Total'],
        [produs2.nume_produs, produs2.cantitate, produs2.pret_bucata, produs2.total]]
print(tabulate(tabel, headers='firstrow'))
"""

#2. Clasa Mașină
print(40 * '*')
class Masina:
    marca = 'Audi'
    viteza_actuala = 0
    culoare = 'Gri'
    culori_disponibile = {'Albastru', 'Galben', 'Verde', 'Rosu', 'Negru', 'Portocaliu', 'Argintiu'}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descriere(self):
        return f'Marca: {self.marca}\n'\
               f'Model: {self.model}\n'\
               f'Viteza maxima: {self.viteza_maxima}\n'\
               f'Culoare: {self.culoare}\n'\
               f'Inmatriculata: {self.inmatriculata}\n'\
               f'Viteza actuala: {self.viteza_actuala}'

    def inmatriculare(self):
        self.inmatriculata = True


    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
        else:
            raise Exception(f'Nu avem aceasta culoare,'
                            f'Culorile disponibile sunt: {self.culori_disponibile}')

    def accelereaza(self, viteza):
        if viteza < 0:
            raise Exception('Viteza invalida')
        if viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = viteza

    def franeaza(self):
        self.viteza_actuala = 0


masina = Masina('A4', 220)
masina.vopseste('Verde')
masina.inmatriculare()
masina.accelereaza(150)
masina.franeaza()
print(masina.descriere())