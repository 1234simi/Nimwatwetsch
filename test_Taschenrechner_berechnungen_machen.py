import pytest
from Taschenrechner_main import berechnungen_machen
import random


@pytest.fixture
def zahl_1():
    random.seed(1504)
    zahl_r_1 = random.randint(1, 100)
    print("\nZahl 1 = ", zahl_r_1)
    return zahl_r_1


@pytest.fixture
def zahl_2():
    random.seed(157)
    zahl_r_2 = random.randint(1, 100)
    print("Zahl 2 = ", zahl_r_2)
    return zahl_r_2


def test_addition_richtig(zahl_1, zahl_2):
    assert berechnungen_machen(zahl_1, '+', zahl_2) == zahl_1 + zahl_2


def test_addition_falsch(zahl_1, zahl_2):
    assert not berechnungen_machen(zahl_1, '+', zahl_2) == zahl_1 - zahl_2


def test_subtraktion_richtig(zahl_1, zahl_2):
    assert berechnungen_machen(zahl_1, '-', zahl_2) == zahl_1 - zahl_2


def test_subtraktion_falsch(zahl_1, zahl_2):
    assert not berechnungen_machen(zahl_1, '-', zahl_2) == zahl_1 + zahl_2


def test_multiplikation_richtig(zahl_1, zahl_2):
    assert berechnungen_machen(zahl_1, '*', zahl_2) == zahl_1 * zahl_2


def test_multiplikation_falsch(zahl_1, zahl_2):
    assert not berechnungen_machen(zahl_1, '*', zahl_2) == zahl_1 + zahl_2


def test_division_richtig(zahl_1, zahl_2):
    assert berechnungen_machen(zahl_1, '/', zahl_2) == zahl_1 / zahl_2


def test_division_falsch(zahl_1, zahl_2):
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
