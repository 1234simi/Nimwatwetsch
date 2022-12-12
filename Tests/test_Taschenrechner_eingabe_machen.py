import pytest

import alle_Berechnungs_funktionen as aBf
import alle_Zahlen_funktionen as azf

import unittest
from _pytest.monkeypatch import MonkeyPatch

class TestEingabe(unittest.TestCase):
    def setUp(self):
        self.monkeypatch = MonkeyPatch()
    def test_opz_valid_one_char(self):
        self.assertEqual(aBf.operations_zeichen_valid([43]), 43)
        self.assertEqual(aBf.operations_zeichen_valid([45]), 45)
        self.assertEqual(aBf.operations_zeichen_valid([42]), 42)
        self.assertEqual(aBf.operations_zeichen_valid([47]), 47)
        self.assertEqual(aBf.operations_zeichen_valid([1]), -1)

    def test_opz_invalid_one_char(self):
        self.assertNotEqual(aBf.operations_zeichen_valid([43]), 42)
        self.assertNotEqual(aBf.operations_zeichen_valid([45]), 47)
        self.assertNotEqual(aBf.operations_zeichen_valid([42]), 45)
        self.assertNotEqual(aBf.operations_zeichen_valid([47]), 126)
        self.assertNotEqual(aBf.operations_zeichen_valid([47]), -1)

    def test_opz_valide_two_char(self):
        self.assertEqual(aBf.operations_zeichen_valid([47, 47]), 126)
        self.assertEqual(aBf.operations_zeichen_valid([48, 48]), -1)

    def test_opz_auswertung(self):
        self.assertEqual(aBf.operations_zeichen_auswertung('+'), [43])
        self.assertEqual(aBf.operations_zeichen_auswertung('  +'), [43])
        self.assertEqual(aBf.operations_zeichen_auswertung('     +      '), [43])
        self.assertEqual(aBf.operations_zeichen_auswertung('  /    /  '), [47, 47])
        self.assertEqual(aBf.operations_zeichen_auswertung('ab  /    /  c'), [97, 98, 47, 47, 99])
        self.assertNotEqual(aBf.operations_zeichen_auswertung('ab  /    /  c'), [47, 47])
        self.assertEqual(aBf.operations_zeichen_auswertung(' '), [])

    def test_operations_zeichen_eingabe(self):
        ## Simuliert den input()
        self.monkeypatch.setattr('builtins.input', lambda _: "1")
        # Die Funktion wird aufgerufen
        zeichen = aBf.operations_zeichen_eingabe()
        assert zeichen == "1"
        assert not zeichen == "2"
    def test_eingabe_operationszeichen_1x(self):
        self.monkeypatch.setattr('builtins.input', lambda _: "1x")
        assert aBf.operations_zeichen_eingabe() == "1x"
        assert not aBf.operations_zeichen_eingabe() == "x1"

    def test_eingabe_operationszeichen_plus(self):
        self.monkeypatch.setattr('builtins.input', lambda _: "+")
        assert aBf.operations_zeichen_eingabe() == "+"
        assert not aBf.operations_zeichen_eingabe() == "x"

    def test_eingabe_operationszeichen_x(self):
        self.monkeypatch.setattr('builtins.input', lambda _: "x")
        assert aBf.operations_zeichen_eingabe() == "x"
        assert not aBf.operations_zeichen_eingabe() == "+"


    # ascii()
    #     +    -   *   /   ~
    #     43, 45, 42, 47, 126

# if __name__ == '__main__':
#     TestEingabe(unittest.TestCase)


