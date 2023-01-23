'''
1.Clasa Cerc
Atribute: rază, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
'''

class Cerc:
    raza = 5
    culoare = 'verde'

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere(self):
        return f'Raza este: {self.raza}\n'\
               f'Culoarea este: {self.culoare}'

    def aria_cercului(self):
        aria = 3.14 * self.raza ** 2
        return aria

    def diametru(self):
        diametru = self.raza * 2
        return diametru

    def circumferinta(self):
        circumferinta = 2 * 3.14 * self.raza
        return circumferinta


descriere_cerc = Cerc(5, 'verde')
print(descriere_cerc.descriere())
print(descriere_cerc.aria_cercului())
print(descriere_cerc.diametru())
print(descriere_cerc.circumferinta())

"""
v2
class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare


    def aria_cercului(self):
        aria = 3.14 * self.raza **2
        return aria


    def diametru_cerc(self):
        diametru = self.raza * 2
        return diametru


    def circumferinta_cerc(self):
        circumferinta = 2 * 3.14 * self.raza
        return circumferinta

descriere_cerc = Cerc(5, 'verde')
print(descriere_cerc.raza)
print(descriere_cerc.culoare)
print(descriere_cerc.aria_cercului())
print(descriere_cerc.diametru_cerc())
print(descriere_cerc.circumferinta_cerc())
"""

"""
2 Clasa Dreptunghi
Atribute: lungime, lățime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă
 nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare
 și va suprascrie atributul
self.culoare. Poți verifica schimbarea culorii 
prin apelarea metodei
descrie().
"""

class Dreptunghi:
    lungime = 10
    latime = 5
    culoare = 'galben'

    def __init__(self, lungime, latime , culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        return f'Lungimea dreptunghilui este: {self.lungime}\n'\
               f'Latimea dreptunghiului este: {self.latime}\n'\
               f'Culoarea triunghilui este: {self.culoare}'

    def aria(self):
        aria = self.lungime * self.latime
        return aria

    def perimetru(self):
        perimetru = 2 * (self.lungime + self.latime)
        return perimetru


dreptunghi = Dreptunghi(5, 3, 'galben')
print(dreptunghi.descriere())
print(dreptunghi.aria())
print(dreptunghi.perimetru())
dreptunghi.culoare = 'albastru'
print(dreptunghi.descriere())

"""
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pentru toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
"""
class Angajat:
    nume = 'Pislea'
    prenume = 'Dumitru Stelian'
    salariu = 100

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere(self):
        return f'Nume angajat: {self.nume}\n'\
               f'Prenume angajat: {self.prenume}\n'\
               f'Salariu angajat: {self.salariu}'

    def __str__(self):
        return f'{self.nume} {self.prenume}'

    def __repr__(self):
        return self.__str__()

    def salariu_anual(self):
        salariu_anual = self.salariu * 12
        return salariu_anual

    def salariu_marire(self):
        marire =self.salariu + (self.salariu * 0.10)
        return marire

angajat = Angajat('Pislea', 'Dumitru Stelian', 100)
print(angajat.descriere())
nume_complet = [angajat]
print(nume_complet)
salariu_lunar = angajat.salariu
print(salariu_lunar)
print(angajat.salariu_anual())
print(angajat.salariu_marire())

"""
4. Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
"""

class Cont:
    iban = 'RO12345'
    titular_cont = 'Pislea Dumitru Stelian'
    sold = 1000

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.')

    def debitare_cont(self, suma):
        self.sold -= suma

    def creditare_cont(self, suma):
        self.sold += suma

cont_bancar = Cont('RO12345', 'Pislea Dumitru Stelian', 1000)
cont_bancar.afisare_sold()
cont_bancar.debitare_cont(200)
cont_bancar.creditare_cont(300)
cont_bancar.afisare_sold()