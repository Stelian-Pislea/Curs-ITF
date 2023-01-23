# 1 Alegeti 3 functii din cele implementate la tema anterior,
# si scrieti unit tests pentru ele folosind unittest.
from dataclasses import dataclass
from math import pi
from abc import abstractmethod, ABC
def aria_cercului(raza):
    aria = 3.14 * raza ** 2
    return aria

def diametru(raza):
    diametru = raza * 2
    return diametru

def circumferinta(raza):
    circumferinta = 2 * 3.14 * raza
    return circumferinta

# 2 Alegeti 2 clase din cele implementate la tema anterior,
# si scrieti unit teste pentru toate metodele folosind
# unittest

@dataclass
class Angajat:
    nume: str
    prenume: str
    salariu: int

    def descriere(self):
        return f'Nume angajat: {self.nume}'\
               f'Prenume angajat: {self.prenume}'\
               f'Salariu angajat: {self.salariu}'

    def salariu_anual(self):
        salariu_anual = self.salariu * 12
        return salariu_anual

    def salariu_marire(self):
        marire =self.salariu + (self.salariu * 0.10)
        return marire

@dataclass
class Cont:
    iban: str
    titular_cont: str
    sold: int

    def afisare_sold(self):
        return f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.'

    def debitare_cont(self, suma):
        self.sold -= suma

    def creditare_cont(self, suma):
        self.sold += suma

# 3 Alegeti una din temele de mai sus, si convertiti
# testele din unittest in pytest

# 4 Folosind TDD, rezolvati urmatoarea problema:
# Sa se scrie o ierarhie de clase pentru forme
# geometrice: FormaGeometrica, Patrat, Dreptunghi, Cerc.
# FormaGeometrica este interfata, adica clasa abstracta
# cu doar metode astracte. Metode: arie(), perimetru().
# Sa se mosteneasca interfata, si sa se implementeze
# cele 2 metode pentru fiecare din cele 3 forme
# geometrice.

class FormaGeometrica(ABC):
    PI = pi
    @abstractmethod
    def arie(self):
        ...

    @abstractmethod
    def perimetru(self):
        ...
@dataclass
class Patrat(FormaGeometrica):
    latura: int
    def arie(self):
        aria = self.latura ** 2
        return aria

    def perimetru(self):
        perimetru = 4 * self.latura
        return perimetru
@dataclass
class Dreptunghi(FormaGeometrica):
    lungime: int
    latime: int
    def arie(self):
        aria = self.lungime * self.latime
        return aria

    def perimetru(self):
        perimetru = 2 * (self.lungime + self.latime)
        return perimetru
@dataclass()
class Cerc(FormaGeometrica):
    raza: int
    def arie(self):
        aria = self.PI * self.raza ** 2
        return aria

    def perimetru(self):
        perimetru = 2 * self.PI * self.raza
        return perimetru