#!/usr/bin/env python3
import unittest
import pytest
import alle_Berechnungs_funktionen as aBf
import coverage
from _pytest.monkeypatch import MonkeyPatch

import alle_Zahlen_funktionen as aZf


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

    def test_zahl_eingabe_valid_to_float(self):
        # Ungültige Zeichenliste
        self.assertEqual(aZf.zahl_eingabe_valid_to_float([42, 33]), (False, False))
        # 0.0
        self.assertEqual(aZf.zahl_eingabe_valid_to_float([48, 46, 48]), (0.0, True))
        # -1
        self.assertEqual(aZf.zahl_eingabe_valid_to_float([45, 49]), (-1.0, False))

    def test_zahl_eingabe_valid(self):
        # Gültige Zahl
        self.assertEqual(aZf.zahl_eingabe_valid('-12.9'), [45, 49, 50, 46, 57])
        self.assertEqual(aZf.zahl_eingabe_valid('-'), [45])
        self.assertEqual(aZf.zahl_eingabe_valid('.'), [46])
        self.assertEqual(aZf.zahl_eingabe_valid('12345678910'), [49, 50, 51, 52, 53, 54, 55, 56, 57, 49, 48])
        # Ungültige Zahl
        self.assertEqual(aZf.zahl_eingabe_valid('-a12.9'), False)
        self.assertEqual(aZf.zahl_eingabe_valid(' '), False)
        self.assertEqual(aZf.zahl_eingabe_valid(','), False)
        self.assertEqual(aZf.zahl_eingabe_valid('+'), False)
        self.assertEqual(aZf.zahl_eingabe_valid('zwei'), False)
        self.assertEqual(aZf.zahl_eingabe_valid('0.0000000000000000000000000000000000000000000000000000000009'), False)
        self.assertEqual(aZf.zahl_eingabe_valid('123456789101'), False)

    def setUp(self):
        self.monkeypatch = MonkeyPatch()

    def test_zahl_eingabe_real(self):
        # Gültige Eingabe
        self.monkeypatch.setattr('builtins.input', lambda _: '1.35')
        assert aZf.zahl_eingabe_real() == 1.35
        assert not aZf.zahl_eingabe_real == 0.123

        self.monkeypatch.setattr('builtins.input', lambda _: '-12....2..')
        assert aZf.zahl_eingabe_real() == -12.2

        self.monkeypatch.setattr('builtins.input', lambda _: '12345678910')
        assert aZf.zahl_eingabe_real() == 12345678910






# if __name__ == '__main__':
# TestBerechnungen(unittest.TestCase)

# ascii()
#     +    -   *   /   ~
#     43, 45, 42, 47, 126
