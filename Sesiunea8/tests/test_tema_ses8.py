import unittest
from parameterized import parameterized
from Teme.tema_ses8 import aria_cercului, diametru, circumferinta, Angajat, Cont, Patrat, Dreptunghi, Cerc
import pytest

# 1
class TestTema(unittest.TestCase):
    def test_aria_cercului(self):
        self.assertEqual(aria_cercului(5), 78.5)

    def test_diametru(self):
        self.assertEqual(diametru(5), 10)

    def test_circumferinta(self):
        self.assertEqual(circumferinta(3), 18.84)


# 2
class TestAngajat(unittest.TestCase):
    def setUp(self):
        self.angajat = Angajat('Pislea', 'Stelian', 100)

    def test_descriere(self):
        self.assertEqual(self.angajat.descriere(),
                         'Nume angajat: Pislea'
                         'Prenume angajat: Stelian'
                         'Salariu angajat: 100')

    def test_salariu_anual(self):
        self.assertEqual(self.angajat.salariu_anual(), 1200)

    def test_marire_salariu(self):
        self.assertEqual(self.angajat.salariu_marire(), 110)


class TestCont(unittest.TestCase):
    def setUp(self):
        self.cont = Cont('RO12345', 'Pislea', 1000)

    def test_afisare_sold(self):
        self.assertEqual(self.cont.afisare_sold(),
                         'Titularul Pislea are in contul RO12345 suma de 1000 lei.')

    def test_debitare_cont(self):
        self.assertEqual(self.cont.debitare_cont(100), None)

    def test_creditare_cont(self):
        self.assertEqual(self.cont.creditare_cont(200), None)

# 3
    @pytest.mark.parametrize('n, expected', [
        (5, 78.5),

    ])
    def test_aria_cercului(n, expected):
        assert aria_cercului(n) == expected

    @pytest.mark.parametrize('n, expected',[
        (5, 10)
    ])
    def test_diametru(n, expected):
        assert diametru(n) == expected

    @pytest.mark.parametrize('n, expected',[
        (3, 18.84)
    ])
    def test_circumferinta(n, expected):
        assert circumferinta(n) == expected

# 4
class TestPatrat(unittest.TestCase):
    def setUp(self):
        self.patrat = Patrat(5)

    def test_aria(self):
        self.assertEqual(self.patrat.arie(), 25)

    def test_perimetru(self):
        self.assertEqual(self.patrat.perimetru(),20)

class TestDreptunghi(unittest.TestCase):
    def setUp(self):
        self.dreptunghi = Dreptunghi(5, 6)

    def test_aria(self):
        self.assertEqual(self.dreptunghi.arie(),30)

    def test_perimetru(self):
        self.assertEqual(self.dreptunghi.perimetru(),22)

class TestCerc(unittest.TestCase):
    def setUp(self):
        self.cerc = Cerc(5)

    def test_aria(self):
        self.assertEqual(self.cerc.arie(), 78.53981633974483)

    def test_perimetru(self):
        self.assertEqual(self.cerc.perimetru(), 31.41592653589793)
