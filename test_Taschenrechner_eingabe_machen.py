import pytest
from Taschenrechner_main import operations_zeichen_valid


def test_opz_valid():
    zeichen = '+'
    assert operations_zeichen_valid(zeichen) == '+'


def test_opz_invalid():
    zeichen = '+'
    assert not operations_zeichen_valid(zeichen) == '*'

# def operations_zeichen_valid(zeichen):
#     ### Prüfen, ob das Operations-Zeichen valid ist
#     ascii_zeichen = ord(zeichen)
#     # print(ascii_zeichen)
#     if (ascii_zeichen == 42 or ascii_zeichen == 43 or ascii_zeichen == 45 or ascii_zeichen == 47):
#         print("Das Operations-Zeichen ist valide!")
#         print("Das Operations-Zeichen ist: ", zeichen)
#     else:
#         print("Das Operations-Zeichen ist nicht valide!")
#         return False
#
#     print("Datentyp zahl_1:", type(zahl_1))
#     return zeichen
