# =============================================================================
# Taschenrechner Main Programm
# Software-Entwicklung
# Dominic Moser & Simon Steigmeier
# Mobile-Robotics

# Weitere Informationen im 'ReadMe.md'

# =============================================================================
from alle_Zahlen_funktionen import zahl_eingabe_real
import alle_Berechnungs_funktionen as aBf

from history_File_funktionen import history_eintrag_erstellen, inhalte_auflisten


def eingaben_machen():
    """
    Eingabe Aufforderung um die 1.Zahl, das Operationszeichen und die 2.Zahl einzugeben.
    Die jeweilige Eingabe wird auf ihre Gültigkeit überprüft. Falls die Eingabe ungültig sein sollte,
    wird die Eingabe wiederholt.
        :return: zahl_1 (float), zeichen (ascii_int) -> 42, 43, 45, 47, 126, zahl_2 (float)
    """
    ### Die Zahlen und das Operations-Zeichen wird eingegeben.
    # Zahl 1 eingeben
    zahl_1 = zahl_eingabe_real()

    # Eingabe Aufforderung für das Operations-Zeichen
    zeichen_input = aBf.operations_zeichen_eingabe()
    ## Die Eingabe wird verarbeitet
    zeichen = aBf.operations_zeichen_auswertung(zeichen_input)
    ## Es wird geprüft, ob das Operations-Zeichen valid ist
    zeichen = aBf.operations_zeichen_valid(zeichen)
    while zeichen == -1:
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

################################################################### ReadMe, Workflow (short) 1.
    # Zuerst wird die Eingabe gemacht
    zahl_1, zeichen, zahl_2 = eingaben_machen()

################################################################### ReadMe, Workflow (short) 2.
    # Danach werden die Berechnungen durchgeführt
    try:
        resultat = aBf.berechnungen_machen(zahl_1, zeichen, zahl_2)
    except ZeroDivisionError:
        print('En Gruess vom Marc: "Durch Null Teilen ist nicht erlaubt"')
    else:
################################################################### ReadMe, Workflow (short) 3.
        # Je nach Operations-Zeichen wird die Ausgaben anderst sein
        trenner = aBf.ausgabe_trenner(zeichen)

        ## Das Resultat mit dem jeweiligen Trenner wird ausgegeben
        aBf.ausgabe_resultat(resultat, trenner, zeichen, zahl_1, zahl_2)

################################################################### ReadMe, Workflow (short) 4.
        ### Make History File
        history_eintrag_erstellen(zahl_1, zeichen, zahl_2, resultat, 'history_datenbank.json')

    ## History file wird ausgegeben
    print(' ')
    print('\t--> History <--')
    print(' ')
    inhalte_auflisten('history_datenbank.json')


