import pytest
from Taschenrechner import berechnungen_machen
print("pytest Version: ",pytest.__version__)
print(" ")
# =============================================================================
# Zum testen, ob die Funktion 'berechnungen_machen()' auch importiert wurde:
# =============================================================================


def test_falsches_Operations_zeichen():
    assert not berechnungen_machen('1', 'x', '2')
    assert not berechnungen_machen('1', '=', '2')


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

#
# if __name__ == '__main__':
#     pytest.main([ __file__, ])
#
#     # Warning: When pytest is invoked from test itself, all imports are done already,
#     # and, therefore, they are not counted as covered; so line 1 of is_prime is reported as 'missing'
#     pytest.main([ __file__, '--cov=prime', '--cov-report', 'term-missing', '--cov-branch'])
#
