import pytest
from Taschenrechner_main import operations_zeichen_valid
from Taschenrechner_main import zahl_1_valid

def test_opz_valid():
    zeichen = '+'
    assert operations_zeichen_valid(zeichen) == '+'
    zeichen = '-'
    assert operations_zeichen_valid(zeichen) == '-'
    zeichen = '*'
    assert operations_zeichen_valid(zeichen) == '*'
    zeichen = '/'
    assert operations_zeichen_valid(zeichen) == '/'
def test_opz_invalid():
    zeichen = '+'
    assert not operations_zeichen_valid(zeichen) == '*'
    zeichen = '+'
    assert not operations_zeichen_valid(zeichen) == '/'
    zeichen = '+'
    assert not operations_zeichen_valid(zeichen) == '-'
    zeichen = '+'
    assert not operations_zeichen_valid(zeichen) == '='
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
    monkeypatch.setattr('zahl_1_valid',io.StringIO('first\nsecond'))
    str1,str2 = read_two_strings()
    assert str1 == 'first'
    assert str2 == 'second'
