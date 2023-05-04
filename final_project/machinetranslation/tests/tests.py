from unittest import TestCase
import unittest

from translator import english_to_french, french_to_english


class TestEnglishToFrench(TestCase):
    def test_null_input(self):
        self.assertEqual(english_to_french(None), '')

    def test_input(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")


class TestFrenchToEnglish(TestCase):
    def test_null_input(self):
        self.assertEqual(french_to_english(None), '')

    def test_input(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")


unittest.main()
