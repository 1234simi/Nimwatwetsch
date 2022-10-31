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
def test_num_1_invalid():
    zahl1 = 'gh'
    assert not zahl_1_valid(zahl1) == '2'