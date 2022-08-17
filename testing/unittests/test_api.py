"""
Tests the api modules
"""

#Import Statements
import unittest

#From Import Statements
from os import system
from os.path import exists
from unittest.mock import patch
from io import StringIO
from google_calendar_API import token_helper as token

class MyTestCase(unittest.TestCase):
    """
    Just a class to contain tests
    """

    @patch("sys.stdout", StringIO())
    def test_token_removal(self):
        """Tests token removal"""
        storage_directory = "testing/unittests/resources/"

        self.assertTrue(exists(f"{storage_directory}token.json"))

        removed_token = token.remove_token(storage_directory)
        self.assertTrue(removed_token)
        self.assertFalse(exists(f"{storage_directory}token.json"))

        removed_token = token.remove_token(storage_directory)
        self.assertFalse(removed_token)

        system("touch testing/unittests/resources/token.json")
