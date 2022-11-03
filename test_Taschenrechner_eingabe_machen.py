import pytest
import Taschenrechner_main as tr
from Taschenrechner_main import zahl_1_valid
import io
import unittest


class TestEingabe(unittest.TestCase):
    def test_opz_valid_one_char(self):
        self.assertEqual(tr.operations_zeichen_valid([43]), 43)
        self.assertEqual(tr.operations_zeichen_valid([45]), 45)
        self.assertEqual(tr.operations_zeichen_valid([42]), 42)
        self.assertEqual(tr.operations_zeichen_valid([47]), 47)
        self.assertEqual(tr.operations_zeichen_valid([1]), -1)

    def test_opz_invalid_one_char(self):
        self.assertNotEqual(tr.operations_zeichen_valid([43]), 42)
        self.assertNotEqual(tr.operations_zeichen_valid([45]), 47)
        self.assertNotEqual(tr.operations_zeichen_valid([42]), 45)
        self.assertNotEqual(tr.operations_zeichen_valid([47]), 126)
        self.assertNotEqual(tr.operations_zeichen_valid([47]), -1)
    def test_opz_valide_two_char(self):
        self.assertEqual(tr.operations_zeichen_valid([47, 47]), 126)
        self.assertEqual(tr.operations_zeichen_valid([48, 48]), -1)



# operations_zeichen_valid(zeichen_liste_real)


# ascii()
#     +    -   *   /
#     43, 45, 42, 47




def test_num_1_valid():
    zahl1 = '46'
    assert zahl_1_valid(zahl1) == '46'
    zahl1 = "067489367"
    assert zahl_1_valid(zahl1) == '067489367'
    zahl1 = '00000000000'
    assert zahl_1_valid(zahl1) == '00000000000'

def read_two_strings():
    str1 = input('abd')
    str2 = input('234')
    return str1, str2
def test_read_two_strings_valid(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('first\nsecond'))
    str1,str2 = read_two_strings()
    assert str1 == 'first'
    assert str2 == 'second'
