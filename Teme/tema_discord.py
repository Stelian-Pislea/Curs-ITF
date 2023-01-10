""" 1. Ce inseamna if __name__=="__main__" scris intr-un fisier python?
Se foloseste cand importam module si dorim sa executam
doar anumite linii de cod.
Un program Python folosește condiția if __name__ == '__main__'
pentru a rula codul din interiorul instrucțiunii if numai atunci
când programul este rulat direct de interpretul Python. Codul din
interiorul instrucțiunii if nu este executat atunci când codul
fișierului este importat ca modul.

2. Cum instalam un pachet extern python?
Un pachet extern python il putem instala din IDE in terminal
prin comanda pip  ex: pip3 install pandas, sau le putem
accesa online.

3. Ce este dataclass in python?
Modulul dataclasses oferă o modalitate de a crea
clase de date într-un mod mai simplu, fără a fi
nevoie să se scrie metode.
Când facem asta, nu mai trebuie să scriem funcția
__init__, ci doar să specificăm atributele clasei
și tipurile acestora, si putem seta valori pentru
atributele clasei.

4. Ce este functia hash?
Funcția hash este folosită pentru
a returna o valoare întreagă hash a obiectului
pe care îl trecem ca parametru în el dacă
obiectul este hashable. În general, valorile
hash sunt folosite pentru a compara cheile de
dicționar în timpul căutării în dicționar.

5. Cum pot face codul de mai jos sa functioneze corect?


    class Person:
        def __init__(self, age, name):
            self.age = age
            self.name = name

        def __eq__(self, other):
            return isinstance(other, Person) and self.age == other.age and self.name == other.name

    s = set()
    p = Person(29, "Adrian")
    s.add(p)
"""
#Corect

class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Person) and self.age == other.age and self.name == other.name

    def __hash__(self):
        return hash(self.name) + hash(self.age)

s = set()
p = Person(29, "Adrian")
s.add(p)
print(s)