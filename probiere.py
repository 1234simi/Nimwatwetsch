import random



def operations_zeichen_eingabe():
    zeichen = input("Bitte gib das Operations-Zeichen ein: ")
    zeichen_liste = []
    for i in range(len(zeichen)):
        # print(ord(zeichen[i]))
        zeichen_liste.append(ord(zeichen[i]))

    zeichen_liste_real = []
    for j in range(len(zeichen_liste)):
        if (zeichen_liste[j] != 32):
            zeichen_liste_real.append(zeichen_liste[j])
    print(f"Zeichen_liste_real: {zeichen_liste_real}")
    return zeichen_liste_real


def operations_zeichen_valid(zeichen_liste_real):
    if(len(zeichen_liste_real) == 1):
        ### Prüfen, ob das Operations-Zeichen valid ist
        ## Zeichen in ASCII-Code umwandeln
        ascii_zeichen = int(zeichen_liste_real[0])
        if ascii_zeichen == 42 or ascii_zeichen == 43 or ascii_zeichen == 45 or ascii_zeichen == 47:
            zeichen = int(zeichen_liste_real[0])
            return zeichen
        else:
            print(f"\tDas Operations-Zeichen ist nicht valide!")
            print("\tBitte die Eingabe Wiederholen!")
            zeichen = operations_zeichen_eingabe()
            zeichen = operations_zeichen_valid(zeichen)
            return zeichen

    if (len(zeichen_liste_real) >= 1):
        ganzzahl_division_true = []
        counter = 0
        for i in range(len(zeichen_liste_real)):
            if (zeichen_liste_real[i] == 47):
                ganzzahl_division_true.append("True")
                counter += 1

        if len(zeichen_liste_real) == 2 and counter == 2:
            print("Ganzzahldivision")
            return 99
        else:
            print("Bitte die Eingabe Wiederholen!")
            zeichen_liste_real = operations_zeichen_eingabe()
            ganzzahl_division_true = operations_zeichen_valid(zeichen_liste_real)
            return ganzzahl_division_true



if __name__ == '__main__':
    # zeichen_liste_real = operations_zeichen_eingabe()
    # x = operations_zeichen_valid(zeichen_liste_real)
    # print(f"Ausgabe = {x}")

    print(chr(126))

    print(40//-3)
    print(40 / -3)

    print(-40 // 3)
    print(-40 / 3)




    # zeichen_liste_real = operations_zeichen_eingabe()
    # print(f"Zeichenliste real = {zeichen_liste_real}")
    # # print(int(zeichen_liste_real[0]))
    # zeichen_valide = operations_zeichen_valid(zeichen_liste_real)
    # print(f"Zeichen schluss: {zeichen_valide}")
    #


#
# result = 12.0
# titel = f"Das Resultat lautet {float(result)} "
#
# trenner ="++"
# ## // = Nur durch eine Ganzzahl teilen
# trenner_length = len(titel) // len(trenner)
# print(f"\n{trenner_length * trenner}\n{titel}\n{trenner_length * trenner}")
#






#
# def zahl_random_1():
#     random.seed(1504)
#     zahl_r_1 = random.randint(1, 100)
#     return zahl_r_1
#
# def zahl_random_2():
#     random.seed(157)
#     zahl_r_2 = random.randint(1, 100)
#     return zahl_r_2
#
# print(zahl_random_1())
# print(zahl_random_2())
#
# def addition(zahl_1, zahl_2):
#     result = zahl_1 + zahl_2
#     return result
#
# print(addition(zahl_random_1(), zahl_random_2()))
#
#
#
#
#
# import pytest
# import unittest
# import Taschenrechner_main as tr
#
# class TestEingabe(unittest.TestCase):
#
#     def test_opz_valid_one_char(self):
#         self.assertEqual(tr.operations_zeichen_valid([43]), 43)
#         self.assertEqual(tr.operations_zeichen_valid([45]), 45)
#         self.assertEqual(tr.operations_zeichen_valid([42]), 42)
#         self.assertEqual(tr.operations_zeichen_valid([47]), 47)
#     def test_opz_invalid_one_char(self):
#         self.assertNotEqual(tr.operations_zeichen_valid([43]), 42)
#         self.assertNotEqual(tr.operations_zeichen_valid([45]), 47)
#         self.assertNotEqual(tr.operations_zeichen_valid([42]), 45)
#         self.assertNotEqual(tr.operations_zeichen_valid([47]), 126)
#     def test_opz_valide_two_char(self):
#         zeichen = [47, 47]
#         assert operations_zeichen_valid(zeichen) == 126
#         zeichen = [43]
#         assert operations_zeichen_valid(zeichen) == 43
#         zeichen = [45]
#         assert operations_zeichen_valid(zeichen) == 45
#         zeichen = [42]
#         assert operations_zeichen_valid(zeichen) == 42
#         zeichen = [47]
#         assert operations_zeichen_valid(zeichen) == 47
#
