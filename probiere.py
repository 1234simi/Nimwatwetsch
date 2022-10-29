import random

def zahl_random_1():
    random.seed(1504)
    zahl_r_1 = random.randint(1, 100)
    return zahl_r_1

def zahl_random_2():
    random.seed(157)
    zahl_r_2 = random.randint(1, 100)
    return zahl_r_2

print(zahl_random_1())
print(zahl_random_2())

def addition(zahl_1, zahl_2):
    result = zahl_1 + zahl_2
    return result

print(addition(zahl_random_1(), zahl_random_2()))
