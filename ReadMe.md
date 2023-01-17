## How to use?
Im `Taschenrechner_main.py` findet die ganze Magie statt. In den anderen `.py`-Files sind die geschriebenen 
Funktionen zu Hause:
- Alles was mit der Zahlen-Eingabe zu tun hat im `alle_Zahlen_funktionen.py`
- Die Berechnungs-Funktionen sowie die *Operations-Zeichen-Eingabe-Und-Validierung* sind im
`alle_Berechnungs_funktionen.py` zu finden 
- Wenn es um das History-File geht, bitte im `history_File_funktionen.py` nachlesen bez. im `history_datenbank.json` nachschauen
- Die geschriebenen Tests sind im Ordner `Tests` hinterlegt

Es wurde auch mit Docstrings gearbeitet, was das einlesen und das Nachvollziehen des Programmes,
hoffentlich, etwas vereinfachen wird :-)

Das ganze Projekt wurde in PyCharm erstellt.

## Important
Es wurde viel mit ASCII gearbeitet, folgenden Tabelle listet die häufig-verwendeten ASCII Zahlen auf:
````python
42 -->  *
43 -->  +
45 -->  -
47 -->  /
126 --> ~

48 -->  0
49 -->  1
50 -->  2
51 -->  3
52 -->  4
53 -->  5
54 -->  6
55 -->  7
56 -->  8
57 -->  9
46 -->  .
45 -->  -
````

## Workflow (short)
Die nachfolgende Nummerierung ist im `Taschenrechner_main.py @ if __name__ == '__main__':` ebenfalls aufgeführt:
1. Benutzer Eingabe von `Zahl_1`, `Operations-Zeichen` und `Zahl_2`
2. Es wird versucht, die jeweilige Berechnung durchzuführen (z.B. wenn durch 0 geteilt wird, wird eine Exception geworfen)
3. Falls die Berechnung gültig war, wird die Berechnung inklusive Resultat ausgegeben. Als optische Abrundung 
 wird oberhalb und unterhalb vom Resultat jeweils eine Kette von den jeweiligen `Operations-Zeichen` ausgegeben.
4. Zum Schluss wird das ganze (`Zahl_1`, `Operations-Zeichen`, `Zahl_2` und das Resultat) in einem Dictionary gespeichert.
 Dies dient als History-File, der **key** ist der jeweilige timestamp und das **value** die ganze Berechnung.


## Workflow (long)
### 1. Benutzer Eingabe von `Zahl_1`, `Operations-Zeichen` und `Zahl_2`
- *Zahl_1 eingeben:*
  - Zuerst erfolgt die Eingabe der Zahl mit Hilfe von `input()`
  - Die eingegebenen Ziffern werden alle einzeln geprüft, ob sie gültig sind.
    - Dies wird mit den Keys eines Dictionarys bewerkstelligt, welche in ASCII-Int umgewandelt werden.
    - Gültig sind die Ziffern `0` bis und mit `9` sowie die Zeichen `.` und `-` :
      - `{48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7',
           56: '8', 57: '9', 46: '.', 45: '-'}`
    - Da es vorkommen kann, dass zu viele `'.'` oder mehrere `'-'` eingegeben werden,
    wird die Funktion `zahl_eingabe_valid_to_float()` dies korrigieren und nimmt jeweils nur den Ersten `'.'` oder das Erste `'-'`
  - Falls alle Ziffern gültig waren, werden sie in eine float Zahl umgewandelt
    - Sonderfall bei der Eingabe `0.0`: hier konnte die `while` Schleife nicht verlassen werden(`0 = False`),
    deshalb kommt die `null_flag` zum Einsatz, welche auf `True` gesetzt wird, wenn der Wert der Zahl `0.0` ist
  - Sobald die Eingabe gültig ist, wird die Zahl_1 zurückgegeben

- *Operations-Zeichen eingeben:*
  - Dies erfolgt im gleichen Schema wie die Eingabe der Zahlen.
  - Auch hier wurde ein Dictionary benutzt, um die jeweilig-gültigen Operations-Zeichen zu finden:
    - `{43: '+', 45: '-', 42: '*', 47: '/'}`
    - Die obigen Operationen sind erlaubt, hinzu kommt noch die Ganzzahl-Division: `'//'`
    - Die Funktion `operations_zeichen_auswertung()` erkennt unter anderem,
    wenn zu viele Leerzeichen eingegeben wurden und löscht diese automatisch aus der Eingabe heraus.
    Ebenfalls wird in dieser Funktion die Gazzahl-Division mit Hilfe der `len()` Funktion der Eingabe 'erkannt'
  - Auch bei dieser Eingabe-Aufforderung wird erst weitergemacht, wenn das Operations-Zeichen valide ist,
  ansonsten bleibt man in der `while()` Schleife
- *Zahl_2 eingeben:*
  - Erfolgt analog zu *Zahl_1 eingeben:*

### 2. Es wird versucht, die jeweilige Berechnung durchzuführen...
- Hierfür wird das gültige Operations-Zeichen von ASCII-Int in einen String umgewandelt.
- Danach wird die jeweilige Berechnung durchgeführt
  - Das `'~'` bez. ASCII-Int `126` steht für die Ganzzahl-Division
- Die Berechnungs-Funktion liefert gerade das Resultat zurück, falls die Rechenoperation nicht möglich sein sollte,
wird ein 'NaN' als Resultat zurückgegeben
- Falls es bei einer der beiden Divisions-Funktionen zu der Durch-Null-Teilen-Situation kommen sollte, wird
die `ZeroDivisionError` Exception geworfen und das Programm beendet sich, ohne abzustürzen



### 3. Falls die Berechnung gültig war, wird die Berechnung inkl. Resultat ausgegeben...
- Hier wird zuerst der jeweilige *trenner* ausgewertet.
    - Dies geschieht in der Funktion `ausgabe_trenner()`, welche zu dem jeweiligen Operations-Zeichen,
  folgende *trenner* zurückgibt:
```python
...
if zeichen == '+':
    trenner = "++"
elif zeichen == '-':
    trenner = "--"
elif zeichen == '*':
    trenner = "**"
elif zeichen == '/':
    trenner = "/_"
elif zeichen == '~':
    trenner = "//"
else:
    trenner = "%%"
return trenner
```
  - Diese *trenner* werden, bei der Ausgabe, um die Berechnung gelegt:
````python
+++++++++++++++++++++++++++++++++++++
Das Resultat lautet: -1.0 + 1.0 = 0.0
+++++++++++++++++++++++++++++++++++++
````

### 4. Zum Schluss wird das ganze (`Zahl_1`, `Operations-Zeichen`, `Zahl_2` und das Resultat) in einem Dictionary gespeichert...
- In der Funktion `history_eintrag_erstellen()` werden die beiden eingegebenen Zahlen, das Operstions-Zeichen und das Resultat
in ein String umgewandelt und danach in der richtigen Reihenfolge platziert.
- Die built-in Funktion `datetime.now()` liefert das aktuelle Datum und die exakte Uhrzeit.
- Das Format ist jedoch nicht sehr angenehm zu lesen, daher wird es noch umgewandelt:
````python
default --> "2022-11-19 12:18:08.190088"
nach der Umwandlung --> "19. November 2022 12:18:08"
````
- Nach dieser Umwandlung wird ein Dictionary angelegt: `{timestamp: Ganze-Rechnung-Als-String}` und im .json-File gespeichert
- Alle Einträge vom history-File werden auch ausgegeben, dies sieht dann in etwa so aus:
````python
27. December 2022 12:33:20 ->  -0.32 / 123.0 = -0.0026016260162601626
27. December 2022 12:33:40 ->  -343.0 * 345.0 = -118335.0
27. December 2022 12:34:04 ->  -123.0 // 234.0 = -1.0
27. December 2022 12:36:44 ->  3425.0 / -0.2345 = -14605.543710021322
````


## Testing
- `python3 -m coverage run -m unittest`
- `python3 -m coverage report`

```commandline
simi@ssd180:~/Dokumente/python/PyCharm/Nimwatwetsch$ python3 -m coverage run -m unittest
.
++++++++++++++++++++++++++++++
Das Resultat lautet: 6 + 6 = 12
++++++++++++++++++++++++++++++

////////////////////////////////
Das Resultat lautet: 6 // 6 = 12 
////////////////////////////////
.Fehler bei der Funktion "ausgabe_trenner"!
Fehler bei der Funktion "ausgabe_trenner"!
Fehler bei der Funktion "ausgabe_trenner"!
Fehler bei der Funktion "ausgabe_trenner"!
.Keine Rechenoperation möglich
Keine Rechenoperation möglich
..........	Operations-Zeichen --> +
	Operations-Zeichen --> -
	Operations-Zeichen --> *
	Operations-Zeichen --> /
	Operations-Zeichen --> /
.	Operations-Zeichen --> +
	Operations-Zeichen --> -
	Operations-Zeichen --> *
	Operations-Zeichen --> /
	Operations-Zeichen --> 
.	Operations-Zeichen --> //
....ValueError, converting to (float) not valid
ValueError, converting to (float) not valid
ValueError, converting to (float) not valid
.....
----------------------------------------------------------------------
Ran 24 tests in 0.005s

OK
simi@ssd180:~/Dokumente/python/PyCharm/Nimwatwetsch$ python3 -m coverage report
Name                                                   Stmts   Miss  Cover
--------------------------------------------------------------------------
/usr/lib/python3/dist-packages/attr/__init__.py           22      0   100%
/usr/lib/python3/dist-packages/attr/_compat.py            82     41    50%
/usr/lib/python3/dist-packages/attr/_config.py             9      4    56%
/usr/lib/python3/dist-packages/attr/_funcs.py             79     68    14%
/usr/lib/python3/dist-packages/attr/_make.py             694    207    70%
/usr/lib/python3/dist-packages/attr/_version_info.py      37     17    54%
/usr/lib/python3/dist-packages/attr/converters.py         27     23    15%
/usr/lib/python3/dist-packages/attr/exceptions.py         16      4    75%
/usr/lib/python3/dist-packages/attr/filters.py            15      9    40%
/usr/lib/python3/dist-packages/attr/validators.py        116     56    52%
Tests/__init__.py                                          0      0   100%
Tests/test_Taschenrechner_berechnungen_machen.py          63      1    98%
Tests/test_Taschenrechner_eingabe_machen.py               84      0   100%
Tests/test_history_file.py                                27      0   100%
alle_Berechnungs_funktionen.py                            98      3    97%
alle_Zahlen_funktionen.py                                 69     27    61%
history_File_funktionen.py                                45      4    91%
--------------------------------------------------------------------------
TOTAL                                                   1483    464    69%
simi@ssd180:~/Dokumente/python/PyCharm/Nimwatwetsch$ python3 -m coverage html 
Wrote HTML report to htmlcov/index.html
simi@ssd180:~/Dokumente/python/PyCharm/Nimwatwetsch$ 
```



And again..

```commandline
Name                                                   Stmts   Miss  Cover
--------------------------------------------------------------------------
/usr/lib/python3/dist-packages/attr/__init__.py           22      0   100%
/usr/lib/python3/dist-packages/attr/_compat.py            82     41    50%
/usr/lib/python3/dist-packages/attr/_config.py             9      4    56%
/usr/lib/python3/dist-packages/attr/_funcs.py             79     68    14%
/usr/lib/python3/dist-packages/attr/_make.py             694    207    70%
/usr/lib/python3/dist-packages/attr/_version_info.py      37     17    54%
/usr/lib/python3/dist-packages/attr/converters.py         27     23    15%
/usr/lib/python3/dist-packages/attr/exceptions.py         16      4    75%
/usr/lib/python3/dist-packages/attr/filters.py            15      9    40%
/usr/lib/python3/dist-packages/attr/validators.py        116     56    52%
Tests/__init__.py                                          0      0   100%
Tests/test_Taschenrechner_berechnungen_machen.py          89      0   100%
Tests/test_Taschenrechner_eingabe_machen.py               88      0   100%
Tests/test_history_file.py                                27      0   100%
alle_Berechnungs_funktionen.py                            99      3    97%
alle_Zahlen_funktionen.py                                 73     22    70%
history_File_funktionen.py                                45      4    91%
--------------------------------------------------------------------------
TOTAL                                                   1518    458    70%
```

