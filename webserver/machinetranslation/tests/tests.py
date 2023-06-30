import unittest
from translator import en_to_fr, fr_to_en
"""
Translation functions testing that uses watson api to translate
"""
class TestEnToFr(unittest.TestCase):
    """
    Translation functions test EN to FR
    """
    def test(self):
        self.assertEqual(en_to_fr("Hello"), "Bonjour")
        self.assertNotEqual(fr_to_en("toilette"), "toilette") 
        self.assertEqual(en_to_fr(" "), ' ')


class TestFrToEn(unittest.TestCase):
    """
    Translation functions test FR to EN
    """
    def test(self):
        self.assertNotEqual(fr_to_en("home"), "home") 
        self.assertEqual(fr_to_en("Bonjour"), "Hello")
        self.assertEqual(fr_to_en(" "), ' ')
unittest.main()
