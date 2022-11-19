import unittest
import pytest

import alle_Berechnungs_funktionen as aBf

from _pytest.monkeypatch import MonkeyPatch


class TestBerechnungen(unittest.TestCase):
    # @pytest.fixture
    # def zahl_1(self):
    #     random.seed(1504)
    #     zahl_r_1 = random.randint(1, 100)
    #     print("\nZahl 1 = ", zahl_r_1)
    #     return zahl_r_1

    def test_addition(self):
        self.assertEqual(aBf.addition(2089, 1), 2090)
        self.assertEqual(aBf.addition(-1, 1), 0)
        self.assertEqual(aBf.addition(-1, -1), -2)

    def test_subtraktion(self):
        self.assertEqual(aBf.subtraktion(34, 10), 24)
        self.assertEqual(aBf.subtraktion(-1, 1), -2)
        self.assertEqual(aBf.subtraktion(-1, -1), 0)

    def test_multiplikation(self):
        self.assertEqual(aBf.multiplikation(5, 2), 10)
        self.assertEqual(aBf.multiplikation(-1, 1), -1)
        self.assertEqual(aBf.multiplikation(-1, -1), 1)

    def test_division(self):
        self.assertEqual(aBf.division(40, 10), 4)
        self.assertEqual(aBf.division(-1, 1), -1)
        self.assertEqual(aBf.division(-1, -1), 1)
        self.assertEqual(aBf.division(9, 4), 2.25)
        with self.assertRaises(ZeroDivisionError):
            aBf.division(123, 0)
        with pytest.raises(ZeroDivisionError):
            aBf.division(123, 0)

    def test_ganzzahl_division(self):
        self.assertEqual(aBf.ganzzahl_division(40, 3), 13)
        self.assertEqual(aBf.ganzzahl_division(40, -3), -14)
        self.assertEqual(aBf.ganzzahl_division(-40, 3), -14)
        with self.assertRaises(ZeroDivisionError):
            aBf.ganzzahl_division(123, 0)


    def test_berechnungen_machen(self):
        self.assertEqual(aBf.berechnungen_machen(1, '+', 2), 3)
        self.assertEqual(aBf.berechnungen_machen(1, '-', 2), -1)
        self.assertEqual(aBf.berechnungen_machen(1, '*', 2), 2)
        self.assertEqual(aBf.berechnungen_machen(1, '/', 2), 0.5)
        with pytest.raises(ZeroDivisionError):
            aBf.berechnungen_machen(1, '/', 0)
        with pytest.raises(ZeroDivisionError):
            aBf.berechnungen_machen(1, '~', 0)
        with pytest.raises(ZeroDivisionError):
            aBf.berechnungen_machen(1, 126, 0)

    def test_ausgabe_trenner(self):
        self.assertEqual(aBf.ausgabe_trenner('+'), '++')
        self.assertEqual(aBf.ausgabe_trenner(43), '++')
        self.assertEqual(aBf.ausgabe_trenner('-'), '--')
        self.assertEqual(aBf.ausgabe_trenner('*'), '**')
        self.assertEqual(aBf.ausgabe_trenner('/'), '/_')
        self.assertEqual(aBf.ausgabe_trenner('('), '%%')
        self.assertEqual(aBf.ausgabe_trenner('~'), '//')


if __name__ == '__main__':
    TestBerechnungen(unittest.TestCase)

# ascii()
#     +    -   *   /   ~
#     43, 45, 42, 47, 126