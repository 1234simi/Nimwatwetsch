#!/usr/bin/env python3
import unittest
import history_File_funktionen as hff
import coverage



class TestHistory(unittest.TestCase):
    """
    Diese Klasse testet die Funktionen, welche sich mit dem History-File beschäftigt.
    """
    # def test_datenbank_laden(self, file_name='test_file_json.json'):
    #     inhalt = hff.datenbank_laden(file_name)
    #     assert len(inhalt) == 4
    #     assert inhalt["27. December 2022 12:33:20"] == " -0.32 / 123.0 = -0.0026016260162601626"
    #     assert inhalt["27. December 2022 12:33:40"] == " -343.0 * 345.0 = -118335.0"
    #     assert inhalt["27. December 2022 12:34:04"] == " -123.0 // 234.0 = -1.0"
    #     assert inhalt["27. December 2022 12:36:44"] == " 3425.0 / -0.2345 = -14605.543710021322"

    def test_datenbank_laden_empty_file(self, file_name='test_empty_file.json'):
        """
        Ein leeres .json laden
        """
        inhalt = hff.datenbank_laden(file_name)
        assert len(inhalt) == 0

    def test_display_timestamp(self):
        timestamp = "2022-11-19 20:29:10.037372"
        new_timestamp = hff.display_timestamp(timestamp)
        assert new_timestamp == "19. November 2022 20:29:10"
        assert not new_timestamp == "2022-11-19 20:29:10.037372"

    def test_umwandeln_in_str(self):
        zahl_1_input = 1.0
        zeichen_input = 43
        zahl_2_input = 2.5
        resultat_input = 5.5

        zahl_1, zeichen, zahl_2, resultat = hff.umwandeln_in_str(zahl_1_input, zeichen_input, zahl_2_input,
                                                                 resultat_input)
        assert zahl_1 == ' 1.0'
        assert zahl_2 == '2.5 '
        assert zeichen == ' + '
        assert resultat == ' 5.5'
        assert not resultat == ' 3.5'

    def test_history_eintrag_erstellen(self):
        self.assertEqual(hff.history_eintrag_erstellen(12.1, 43, -0.1, 12.0, 'test_history_datenbank.json'), True)
        self.assertEqual(hff.history_eintrag_erstellen('aa', 43, -0.1, 12.0, 'test_history_datenbank.json'), False)
        self.assertEqual(hff.history_eintrag_erstellen(12.1, '+', -0.1, 12.0, 'test_history_datenbank.json'), False)
