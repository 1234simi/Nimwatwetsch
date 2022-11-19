import unittest
import history_File_funktionen as hff


class TestHistory(unittest.TestCase):

    def test_datenbank_laden(self, file_name='test_file_json.json'):
        inhalt = hff.datenbank_laden(file_name)
        assert len(inhalt) == 3
        assert inhalt["2022-11-19 20:24:32.277619"] == "1.0*6.0=6.0"
        assert inhalt["2022-11-19 20:28:57.181631"] == "3246.0-35467.0=-32221.0"
        assert inhalt["2022-11-19 20:29:10.037372"] == "1.0*5.0=5.0"

    ## Ein leeres .json laden
    def test_datenbank_laden(self, file_name='test_empty_file.json'):
        inhalt = hff.datenbank_laden(file_name)
        assert len(inhalt) == 0

    def test_display_timestamp(self):
        timestamp = "2022-11-19 20:29:10.037372"
        new_timestamp = hff.display_timestamp(timestamp)
        assert new_timestamp == "19. November 2022 20:29:10"

    def test_umwandeln_in_str(self):
        zahl_1_input = 1.0
        zeichen_input = 43
        zahl_2_input = 2.5
        resultat_input = 5.5

        zahl_1, zeichen, zahl_2, resultat = hff.umwandeln_in_str(zahl_1_input, zeichen_input, zahl_2_input,
                                                                 resultat_input)
        assert zahl_1 == '1.0'
        assert zahl_2 == '2.5'
        assert zeichen == '+'
        assert resultat == '5.5'
        assert not resultat == '3.5'
