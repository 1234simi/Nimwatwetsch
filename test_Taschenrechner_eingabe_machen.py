import pytest
from Taschenrechner_main import operations_zeichen_valid
from Taschenrechner_main import zahl_1_valid

import unittest


class TestEingabe(unittest.TestCase):

    def test_opz_valid_one_char(self):
        zeichen = [43]
        assert operations_zeichen_valid(zeichen) == 43
        zeichen = [45]
        assert operations_zeichen_valid(zeichen) == 45
        zeichen = [42]
        assert operations_zeichen_valid(zeichen) == 42
        zeichen = [47]
        assert operations_zeichen_valid(zeichen) == 47


# ascii()
#     +    -   *   /
#     43, 45, 42, 47



    def test_opz_invalid_one_char(self):
        zeichen = [43]
        assert not operations_zeichen_valid(zeichen) == 42
        zeichen = [45]
        assert not operations_zeichen_valid(zeichen) == 47
        zeichen = [42]
        assert not operations_zeichen_valid(zeichen) == 45
        zeichen = [47]
        assert not operations_zeichen_valid(zeichen) == 126

    def test_opz_valide_two_char(selfself):




def test_num_1_valid():
    zahl1 = '46'
    assert zahl_1_valid(zahl1) == '46'
    zahl1 = "067489367"
    assert zahl_1_valid(zahl1) == '067489367'
    zahl1 = '00000000000'
    assert zahl_1_valid(zahl1) == '00000000000'
def test_num_1_invalid():
    zahl1 = 'gh'
    assert not zahl_1_valid(zahl1) == '2'