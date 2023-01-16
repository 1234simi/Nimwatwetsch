#!/usr/bin/env python3
import alle_Berechnungs_funktionen as aBf
import alle_Zahlen_funktionen as azf

import unittest
from _pytest.monkeypatch import MonkeyPatch

import coverage


class TestEingabe(unittest.TestCase):
    """
    Diese Klasse testet die Funktionen, welche sich mit den Eingaben beschäftigt.
    """

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

    def test_zahl_eingabe_real(self):
        self.monkeypatch.setattr('builtins.input', lambda _: 1.23)
        assert aBf.operations_zeichen_eingabe() == 1.23
        assert not aBf.operations_zeichen_eingabe() == 0.123

        self.monkeypatch.setattr('builtins.input', lambda _: -1.23)
        assert aBf.operations_zeichen_eingabe() == -1.23

        self.monkeypatch.setattr('builtins.input', lambda _: ---.232546)
        assert aBf.operations_zeichen_eingabe() == -0.232546

        self.monkeypatch.setattr('builtins.input', lambda _: -.12)
        assert aBf.operations_zeichen_eingabe() == -0.12

    def test_zahl_eingabe_valid_to_float(self):
        """
        {48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7',
        56: '8', 57: '9', 46: '.', 45: '-'}
        :return:
        """
        self.assertEqual(azf.zahl_eingabe_valid_to_float([45, 45]), (False, False))
        self.assertEqual(azf.zahl_eingabe_valid_to_float([46, 46]), (False, False))
        self.assertEqual(azf.zahl_eingabe_valid_to_float([45, 45, 46, 45, 45, 45, 46]), (False, False))
        self.assertEqual(azf.zahl_eingabe_valid_to_float([45, 46, 53, 54]), (-0.56, False))
        self.assertEqual(azf.zahl_eingabe_valid_to_float([45, 46, 48]), (-0.0, True))
        self.assertEqual(azf.zahl_eingabe_valid_to_float([48]), (0.0, True))
        self.assertEqual(azf.zahl_eingabe_valid_to_float([45, 45, 45, 45, 48, 46, 57]), (-0.9, False))
        self.assertEqual(azf.zahl_eingabe_valid_to_float([45, 46, 46, 46, 46, 46, 57]), (-0.9, False))

    def test_zahl_eingabe_valid(self):
        self.assertEqual(azf.zahl_eingabe_valid('12.1'), [49, 50, 46, 49])
        self.assertEqual(azf.zahl_eingabe_valid('-0.1'), [45, 48, 46, 49])
        self.assertEqual(azf.zahl_eingabe_valid('-a.1'), False)
        self.assertEqual(azf.zahl_eingabe_valid('123.x'), False)
        self.assertEqual(azf.zahl_eingabe_valid('--0.1'), [45, 45, 48, 46, 49])
        self.assertEqual(azf.zahl_eingabe_valid('--..'), [45, 45, 46, 46])

    def test_zahl_eingabe(self):
        self.monkeypatch.setattr('builtins.input', lambda _: 1.23)
        assert azf.zahl_eingabe() == 1.23

        self.monkeypatch.setattr('builtins.input', lambda _: .1)
        assert azf.zahl_eingabe() == .1

        self.monkeypatch.setattr('builtins.input', lambda _: --.1)
        assert azf.zahl_eingabe() == --.1

        self.monkeypatch.setattr('builtins.input', lambda _: 'absl-1.0')
        assert azf.zahl_eingabe() == 'absl-1.0'
        assert not azf.zahl_eingabe() == False

    # ascii()
    #     +    -   *   /   ~
    #     43, 45, 42, 47, 126

# if __name__ == '__main__':
#     TestEingabe(unittest.TestCase)
