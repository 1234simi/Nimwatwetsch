
#todo: Test schreiben
def zahl_eingabe():
    zahl_eingabe = input("Zahl eingeben: ")
    return zahl_eingabe

#todo: Test schreiben
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


#todo: Test schreiben
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

#todo: Test schreiben
def zahl_eingabe_real():
    """
    Zusammenfassung von allen Zahlen-Funktionen, von der Eingabe über die validierung bis zur Rückgabe
        :return: (float) zahl
    """
    z_1 = zahl_eingabe()
    y_1 = zahl_eingabe_valid(z_1)
    while y_1 == False:
        z_1 = zahl_eingabe()
        y_1 = zahl_eingabe_valid(z_1)

    zahl_1 = zahl_eingabe_valid_to_float(y_1)
    print(f'\t eingabe = {zahl_1}')
    return zahl_1
