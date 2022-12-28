from datetime import datetime
import json


def history_eintrag_erstellen(zahl_1: float, zeichen: int, zahl_2: float, resultat: float, json_file_name: str):
    """
    Die beiden Zahlen, das Resultat und das Operationszeichen werden in (str) umgewandelt.
    Danach wird ein Zeitstempel generiert und diesen mit der Berechnung in das History-File gespeichert
        :param json_file_name: Name des datenbank-files, bez. absoluter Pfad (z.B: "history_datenbank.json")
        :param zahl_1: (float)
        :param zeichen: (ascii-int)
        :param zahl_2: (float)
        :param resultat: (float)
        :return: Eintrag in datenbank speichern
    """
    if type(zahl_1) == float and type(zahl_2) == float and type(resultat) == float and type(zeichen) == int:
        ## Umwandeln in str()
        zahl_1, zeichen, zahl_2, resultat = umwandeln_in_str(zahl_1, zeichen, zahl_2, resultat)
        ## Strings werden aneinander gehängt
        eintrag = zahl_1 + zeichen + zahl_2 + '=' + resultat
        # Der timestamp wird gespeichert
        timestamp = str(datetime.now())
        timestamp_eigenes_format = display_timestamp(timestamp)
        eintrag_dict = {
            timestamp_eigenes_format: eintrag
        }
        # Eintrag in Datenbank speichern
        in_datenbank_speichern(json_file_name, eintrag_dict)
        return True

    else:
        return False


# todo: Test schreiben
def in_datenbank_speichern(json_file_name: str, inhalt_neu: dict):
    """
    Der übergebene Dictionary wird in dem Datenbank-File gespeichert
    :param json_file_name: Name des datenbank-files, bez. absoluter Pfad (z.B: "history_datenbank.json")
    :param inhalt_neu: dictionary Eintrag
    """
    inhalt = datenbank_laden(json_file_name)
    inhalt.update(inhalt_neu)
    with open(json_file_name, "w") as offene_datei:
        # offene_datei.write(json.dumps(inhalt))
        json.dump(inhalt, offene_datei, indent=4)


# todo: Test schreiben
def inhalte_auflisten(json_file_name: str):
    """
    Diese Funktion listet den gesamten Inhalt vom .json File auf. Darstellung: 'Timestamp --> Eintrag'
    """
    eintrag = datenbank_laden(json_file_name)
    for timestamp, eintrag in eintrag.items():
        print(f"{timestamp} -> {eintrag}")



def umwandeln_in_str(zahl_1, zeichen, zahl_2, resultat):
    """
    Alle Zahlen und Werte werden in ein String umgewandelt, wird benötigt, um ein Eintag im History-File zu schreiben
        :param zahl_1: (float) zahl_1
        :param zeichen: (ascii_int) zeichen
        :param zahl_2: (float) zahl_2
        :param resultat: (float) resultat
        :return: zahl_1 (str), zeichen (str), zahl_2 (str), resultat (str)
    """
    zahl_1 = str(zahl_1)
    zahl_1 = ' ' + zahl_1
    zahl_2 = str(zahl_2)
    zahl_2 = zahl_2 + ' '
    resultat = str(resultat)
    resultat = ' ' + resultat

    if zeichen == 126:
        zeichen = ' // '
    else:
        zeichen = str(chr(zeichen))
        zeichen = ' ' + zeichen + ' '

    return zahl_1, zeichen, zahl_2, resultat


def datenbank_laden(json_file_name):
    """
    Die Datenbank wird geladen und zurückgegeben, um danach deren Inhalt auszugeben oder um etwas hinzuzufügen
    :param json_file_name: Name des datenbank-files, bez. absoluter Pfad (z.B: "history_datenbank.json")
    :return: Inhalt vom .json-File
    """
    try:
        with open(json_file_name) as offene_datei:
            datei_inhalt = offene_datei.read()
            inhalt = json.loads(datei_inhalt)
    except FileNotFoundError:
        inhalt = {}
    return inhalt


def display_timestamp(timestamp):
    """
    Das Format wird geändert. 'timestamp' kommt von der built in Funktion 'from datetime import datetime'
        :param timestamp: "2022-11-19 12:18:08.190088"
        :return: "19. November 2022 12:18:08"
    """
    timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
    eigenes_format = timestamp.strftime("%d. %B %Y %H:%M:%S")
    return eigenes_format
