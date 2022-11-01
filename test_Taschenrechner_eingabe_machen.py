import pytest
from Taschenrechner_main import operations_zeichen_valid
from Taschenrechner_main import zahl_1_valid
import io
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



<<<<<<< HEAD

=======
>>>>>>> 84f0f5580ab44e712461c6fb16303fe6b48f67f8
    def test_opz_invalid(self):
        zeichen = [43]
        assert not operations_zeichen_valid(zeichen) == '*'
        zeichen = [45]
        assert not operations_zeichen_valid(zeichen) == '/'
        zeichen = [42]
        assert not operations_zeichen_valid(zeichen) == '-'
        zeichen = [47]
        assert not operations_zeichen_valid(zeichen) == '='
<<<<<<< HEAD






=======
>>>>>>> 84f0f5580ab44e712461c6fb16303fe6b48f67f8
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
