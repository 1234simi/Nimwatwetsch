import unittest
import pytest
import alle_Berechnungs_funktionen as aBf
import coverage

class TestBerechnungen(unittest.TestCase):
    """
    Diese Klasse testet die Funktionen, welche sich mit Berechnungen beschäftigt.
    """
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

    # ascii()
    #     +    -   *   /   ~
    #     43, 45, 42, 47, 126
    def test_berechnungen_machen(self):
        self.assertEqual(aBf.berechnungen_machen(1, '!', 2), 'NaN')
        self.assertEqual(aBf.berechnungen_machen(1.234, 72, -2.2345), 'NaN')
        self.assertEqual(aBf.berechnungen_machen(1, 43, 2), 3)
        self.assertEqual(aBf.berechnungen_machen(0.1, 45, -1.101), 1.201)
        self.assertEqual(aBf.berechnungen_machen(1.5, 45, 2.5), -1)
        self.assertEqual(aBf.berechnungen_machen(1, 42, 2), 2)
        self.assertEqual(aBf.berechnungen_machen(1, 47, 2), 0.5)
        with pytest.raises(ZeroDivisionError):
            aBf.berechnungen_machen(1, 47, 0)
        with pytest.raises(ZeroDivisionError):
            aBf.berechnungen_machen(1, 126, 0)
        with pytest.raises(ZeroDivisionError):
            aBf.berechnungen_machen(1, 126, 0)

    def test_ausgabe_trenner(self):
        self.assertEqual(aBf.ausgabe_trenner('+'), '%%')
        self.assertEqual(aBf.ausgabe_trenner(43), '++')
        self.assertEqual(aBf.ausgabe_trenner('-'), '%%')
        self.assertEqual(aBf.ausgabe_trenner(45), '--')
        self.assertEqual(aBf.ausgabe_trenner('*'), '%%')
        self.assertEqual(aBf.ausgabe_trenner(42), '**')
        self.assertEqual(aBf.ausgabe_trenner('/'), '%%')
        self.assertEqual(aBf.ausgabe_trenner(47), '/_')
        self.assertEqual(aBf.ausgabe_trenner(12), '%%')
        self.assertEqual(aBf.ausgabe_trenner(126), '//')

    # ascii()
    #     +    -   *   /   ~
    #     43, 45, 42, 47, 126
    def test_ausgabe_resultat(self):
        """
        Die Berechnug an sich wird nicht auf ihre Richtigkeit geprüft, nur die Ausgabe
        """
        self.assertEqual(aBf.ausgabe_resultat(12, '++', 43, 6, 6), True)
        self.assertEqual(aBf.ausgabe_resultat(12, '++', 41, 6, 6), False)
        self.assertEqual(aBf.ausgabe_resultat(12, '//', 126, 6, 6), True)


if __name__ == '__main__':
    TestBerechnungen(unittest.TestCase)

# ascii()
#     +    -   *   /   ~
#     43, 45, 42, 47, 126
