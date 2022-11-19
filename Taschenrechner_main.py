# =============================================================================
# Taschenrechner Main Programm
# =============================================================================
from alle_Zahlen_funktionen import zahl_eingabe_real
import alle_Berechnungs_funktionen as aBf


def eingaben_machen():
    ### Die Zahlen und das Operations-Zeichen wird eingegeben
    # Zahl 1 eingeben
    zahl_1 = zahl_eingabe_real()

    ## Eingabe Aufforderung Operations-Zeichen
    zeichen_input = aBf.operations_zeichen_eingabe()
    ## Die Eingabe wird verarbeitet
    zeichen = aBf.operations_zeichen_auswertung(zeichen_input)
    ## Es wird geprüft, ob das Operations-Zeichen valid ist
    zeichen = aBf.operations_zeichen_valid(zeichen)
    print(f'zeichen lautet: {zeichen}')
    while (zeichen == -1):
        print(f"\tDas Operations-Zeichen ist nicht valide!")
        print("\tBitte die Eingabe Wiederholen!")
        ## Eingabe Aufforderung
        zeichen_input = aBf.operations_zeichen_eingabe()
        ## Die Eingabe wird verarbeitet
        zeichen = aBf.operations_zeichen_auswertung(zeichen_input)
        zeichen = aBf.operations_zeichen_valid(zeichen)

    # Zahl 2 eingeben
    zahl_2 = zahl_eingabe_real()

    # Die beiden Zahlen und das Operations_Symbol werden zurückgegeben
    return zahl_1, zeichen, zahl_2




# =============================================================================
# Main Programm beginnt:
# =============================================================================
if __name__ == '__main__':
    # Zuerst wird die Eingabe gemacht
    zahl_1, zeichen, zahl_2 = eingaben_machen()

    # Danach werden die Berechnungen durchgeführt
    resultat = aBf.berechnungen_machen(zahl_1, zeichen, zahl_2)

    # Je nach Operations-Zeichen wird die Ausgaben andest sein
    trenner = aBf.ausgabe_trenner(zeichen)

    ## Das Resultat mit dem jeweiligen Trenner wird ausgegeben
    aBf.ausgabe_resultat(resultat, trenner, zeichen, zahl_1, zahl_2)

    ### Make History File
    #todo: History-File erstellen


    print()
    print(f'type result {type(resultat)} ')
    print(f'type trenner {type(trenner)} ')
    print(f'type zeichen {type(zeichen)} ')
    print(f'Zeichen = {zeichen}')
    print(f'Zeichen: {chr(zeichen)}')
    print(f'type zahl_1 {type(zahl_1)} ')
    print(f'type zahl_2 {type(zahl_2)} ')

