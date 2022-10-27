# =============================================================================
# Taschenrechner
# =============================================================================


def eingaben_machen():
    ### Die Zahlen und das Operations-Zeichen wird eingegeben
    zahl_1 = input("Bitte gib die Erste Zahl ein: ")
    zeichen = input("Bitte gib das Operations-Zeichen ein: ")
    zahl_2 = input("Bitte gib die Zweite Zahl ein: ")
    print(" ")

    ### Die Eingaben werden ausgegeben
    print("Zahl 1: ", zahl_1)

    print("Zahl 2: ", zahl_2)


    ### Prüfen, ob das Operations-Zeichen valid ist
    ascii_zeichen = ord(zeichen)
    #print(ascii_zeichen)
    if (ascii_zeichen == 42 or ascii_zeichen == 43 or ascii_zeichen == 45 or ascii_zeichen == 47):
        print("Das Operations-Zeichen ist valide!")
        print("Das Operations-Zeichen ist: ", zeichen)
    else:
        print("Das Operations-Zeichen ist nicht valide!")
        return 1

    print("Datentyp zahl_1:", type(zahl_1))
    # Die beiden Zahlen und das Operations_Symbol werden zurückgegeben
    return float(zahl_1), zeichen, float(zahl_2)





def berechnungen_machen (zahl_1, zeichen, zahl_2):
    print(" ")
    print("Die Berechnungen werden durchgeführt!")
    
    ### Operstionen auswählen:
    if (ord(zeichen) == 42):
        print("Multiplikation")
        result = zahl_1 * zahl_2

    elif (ord(zeichen) == 43):
        print("Addition")
        result = zahl_1 + zahl_2

    elif (ord(zeichen) == 45):
        print("Subtraktion")
        result = zahl_1 - zahl_2

    elif (ord(zeichen) == 47):
        print("Division")
        result = zahl_1 / zahl_2

    else:
        print("Keine Rechenoperation möglich")
        result = 'NaN'

    print("Das Resultat lautet: ", result)


# =============================================================================
# Main Programm beginnt:
# =============================================================================
if __name__ == '__main__':

    #Zuerst wird die Eingabe gemacht
    zahl_1, zeichen, zahl_2 = eingaben_machen()
    
    #Danach werden die Berecunungne durchgeführt
    berechnungen_machen(zahl_1, zeichen, zahl_2)






