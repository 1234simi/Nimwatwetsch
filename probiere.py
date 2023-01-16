import pytest
import Taschenrechner_main as tr

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
    if (len(zeichen_liste_real) == 1):
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


def ditcty_zahlen_soll_int():
    return {48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7',
            56: '8', 57: '9', 46: '.', 45: '-'}

def ditcty_zahlen_soll_str():
    return {'48': '0', '49': '1', '50': '2', '51': '3', '52': '4', '53': '5', '54': '6', '55': '7',
            '56': '8', '57': '9', '46': '.', '45': '-'}




def dicty_operations_zeichen_soll_int():
    return {43: '+', 45: '-', 42: '*', 47: '/'}


if __name__ == '__main__':
    print()
    liste = ['.']
    for item in liste:
        print(f'{item} --> {ord(item)}')

    # coverage run --source =./Tests - m unittest discover -s Tests/ && coverage report



    # zahl_eingabe = '0'
    # zeichen_liste = []
    # for i in range(len(zahl_eingabe)):
    #     zahl_ascii = ord(zahl_eingabe[i])
    #     print(f'zahl_asci: {zahl_ascii}')
    #     if zahl_ascii in ditcty_zahlen_soll_int().keys():
    #         print('joo')
    #         zeichen_liste.append(zahl_ascii)
    #     else:
    #         print('exit')


    #
    # print(ditcty_zahlen().keys())
    # print(type(ditcty_zahlen()))
