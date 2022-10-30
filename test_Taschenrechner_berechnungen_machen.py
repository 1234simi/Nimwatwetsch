import unittest

import pytest
from Taschenrechner_main import berechnungen_machen
import Taschenrechner_main as tr
import random


class TestBerechnungen(unittest.TestCase):
    @pytest.fixture
    def zahl_1(self):
        random.seed(1504)
        zahl_r_1 = random.randint(1, 100)
        print("\nZahl 1 = ", zahl_r_1)
        return zahl_r_1

    @pytest.fixture
    def zahl_2(self):
        random.seed(157)
        zahl_r_2 = random.randint(1, 100)
        print("Zahl 2 = ", zahl_r_2)
        return zahl_r_2

    def test_addition(self):
        self.assertEqual(tr.addition(2089, 1), 2090)
        self.assertEqual(tr.addition(-1, 1), 0)
        self.assertEqual(tr.addition(-1, -1), -2)

    def test_subtraktion(self):
        self.assertEqual(tr.subtraktion(34, 10), 24)
        self.assertEqual(tr.subtraktion(-1, 1), -2)
        self.assertEqual(tr.subtraktion(-1, -1), 0)

    def test_multiplikation(self):
        self.assertEqual(tr.multiplikation(5, 2), 10)
        self.assertEqual(tr.multiplikation(-1, 1), -1)
        self.assertEqual(tr.multiplikation(-1, -1), 1)

    def test_division(self):
        self.assertEqual(tr.division(40, 10), 4)
        self.assertEqual(tr.division(-1, 1), -1)
        self.assertEqual(tr.division(-1, -1), 1)
        self.assertEqual(tr.division(9, 4), 2.25)
        with self.assertRaises(ZeroDivisionError):
            tr.division(123, 0)
        with pytest.raises(ZeroDivisionError):
            tr.division(123, 0)


    def test_berechnungen_machen(self):
        self.assertEqual(tr.berechnungen_machen(1, '+', 2), (3, '+'))
        self.assertEqual(tr.berechnungen_machen(1, '-', 2), (-1, '-'))
        self.assertEqual(tr.berechnungen_machen(1, '*', 2), (2, '*'))
        self.assertEqual(tr.berechnungen_machen(1, '/', 2), (0.5, '/'))
        with pytest.raises(ZeroDivisionError):
            tr.berechnungen_machen(1, '/', 0)

    def test_ausgabe_trenner(self):
        self.assertEqual(tr.ausgabe_trenner('+'), '++')
        self.assertEqual(tr.ausgabe_trenner('-'), '--')
        self.assertEqual(tr.ausgabe_trenner('*'), '**')
        self.assertEqual(tr.ausgabe_trenner('/'), '//')
        self.assertEqual(tr.ausgabe_trenner('('), '%%')


if __name__ == '__main__':
    TestBerechnungen(unittest.TestCase)

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
