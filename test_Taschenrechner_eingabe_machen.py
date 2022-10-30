import pytest
from Taschenrechner_main import operations_zeichen_valid

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
