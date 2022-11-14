import pytest
import Taschenrechner_main as tr
from Taschenrechner_main import zahl_1_valid
import io
import unittest


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

def zahl_1_valid(zahl):
    valid_zahl_bool = isinstance(zahl, float)
    while valid_zahl_bool != True:
        print(f"\tDie erste Zahl ist falsch --> {zahl} <-- ist nicht valide!")
        print("\tBitte die Eingabe Wiederholen!")
        zahl = input("Bitte gib die erste Zahl noch einmal ein: ")
        valid_zahl_bool = isinstance(zahl, float)
        print(valid_zahl_bool)
    return zahl




def zahl_eingabe():
    zahl_eingabe = input("Zahl eingeben: ")
    return zahl_eingabe


def zahl_eingabe_valid(zahl_eingabe):
    ## Die Eingabe wird in eine Liste abgefüllt und in ascii umgewandelt
    zeichen_liste = []
    for i in range(len(zahl_eingabe)):
        zahl_ascii = ord(zahl_eingabe[i])

        if (zahl_ascii >= 48 and zahl_ascii <= 57 or zahl_ascii == 46):
            zeichen_liste.append(zahl_ascii)
        else:
            return False

    return zeichen_liste

def zahl_eingabe_valid_to_float(zeichen_liste):
    zeichen_liste_real = []
    flag_punkt = False
    for i in range(len(zeichen_liste)):
         ## Falls mehrere '.' nach einander folgen wird nur der Erste genommen
        if (flag_punkt == False or zeichen_liste[i] != 46):
            zeichen_liste_real.append(chr(zeichen_liste[i]))

        ## Nur der Erste '.' wird übernommen
        if (zeichen_liste[i] == 46):
            flag_punkt = True

    ##Die Listen Elemente werden zusammengefügt
    trenner = ""
    zeichen_liste_real_str = trenner.join(zeichen_liste_real)

    ##string to float
    zahl_eingabe_float = float(zeichen_liste_real_str)

    # Die Zahl wird als float zurückgegeben
    return zahl_eingabe_float


if __name__ == '__main__':

    z = zahl_eingabe()
    y = zahl_eingabe_valid(z)
    while y == False:
        z = zahl_eingabe()
        y = zahl_eingabe_valid(z)

    eingabe = zahl_eingabe_valid_to_float(y)
    print(f'\t eingabe = {eingabe}')







# x = chr(46)
# print(x)
# print(f'type char(): {type(x)}')
# y = float(x)
# print(y)
# print(type(y))







    #
    #
    # valid_zahl1 = zahl_e.isnumeric()
    # print(f'Eingabe numeric: {valid_zahl1}')
    #
    # print(isinstance(zahl_e, float))
    # # print(zahl_1_valid(zahl_e))




    # num = 0.0001
    # valid_zahl = isinstance(num, float)
    # print(valid_zahl)
    #
    # # print(isinstance(num, float))


