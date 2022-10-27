import pytest
from Taschenrechner_main import berechnungen_machen
import random




def test_addition_richtig():
    random.seed(140)
    zahl_1 = random.randint(1, 100)
    random.seed(145571)
    zahl_2 = random.randint(1, 100)
    assert berechnungen_machen(zahl_1, '+', zahl_2) == zahl_1 + zahl_2
def test_addition_falsch():
    random.seed(1504)
    zahl_1 = random.randint(1, 100)
    random.seed(1401)
    zahl_2 = random.randint(1, 100)
    assert not berechnungen_machen(zahl_1, '+', zahl_2) == zahl_1 - zahl_2
def test_subtraktion_richtig():
    random.seed(8014)
    zahl_1 = random.randint(1, 100)
    random.seed(18741)
    zahl_2 = random.randint(1, 100)
    assert berechnungen_machen(zahl_1, '-', zahl_2) == zahl_1 - zahl_2
def test_subtraktion_falsch():
    random.seed(13454)
    zahl_1 = random.randint(1, 100)
    random.seed(11441)
    zahl_2 = random.randint(1, 100)
    assert not berechnungen_machen(zahl_1, '-', zahl_2) == zahl_1 + zahl_2
def test_multiplikatin_richtig():
    random.seed(14564)
    zahl_1 = random.randint(1, 100)
    random.seed(1445261)
    zahl_2 = random.randint(1, 100)
    assert berechnungen_machen(zahl_1, '*', zahl_2) == zahl_1 * zahl_2
def test_multiplikatin_falsch():
    random.seed(14266)
    zahl_1 = random.randint(1, 100)
    random.seed(12541)
    zahl_2 = random.randint(1, 100)
    assert not berechnungen_machen(zahl_1, '*', zahl_2) == zahl_1 + zahl_2
def test_division_richtig():
    random.seed(134)
    zahl_1 = random.randint(1, 100)
    random.seed(1451)
    zahl_2 = random.randint(1, 100)
    assert berechnungen_machen(zahl_1, '/', zahl_2) == zahl_1 / zahl_2
def test_division_falsch():
    random.seed(134)
    zahl_1 = random.randint(1, 100)
    random.seed(151)
    zahl_2 = random.randint(1, 100)
    assert not berechnungen_machen(zahl_1, '/', zahl_2) == zahl_1 - zahl_2




#
# def is_prime(n):
#     if n < 0:
#         raise Exception('Use is_prime only on non-negative numbers')
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if (n % 2) == 0:
#         return False
#     i = 3
#     while i * i <= n:
#         if (n % i) == 0:
#             return False
#         i += 2
#     return True

#
# def test_negative():
#     with pytest.raises(Exception):
#         is_prime(-3)
#
# def test_special_cases():
#     assert not is_prime(0)
#     assert not is_prime(1)
#
# def test_multiple_of_two():
#     assert is_prime(2)
#     assert not is_prime(4)
#     assert not is_prime(6)
#
# def test_multiple_of_three():
#     assert is_prime(3)
#     assert not is_prime(6)
#     assert not is_prime(9)
#     assert not is_prime(99)
#
# def test_large():
#     assert is_prime((1 << 31)-1)
#

