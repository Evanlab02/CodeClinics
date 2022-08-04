"""
Tests intallation files
"""

#Import Statements
import unittest

#From Import Statements
from os import system
from os.path import expanduser, exists
from unittest.mock import patch
from io import StringIO
from installation import file_path_helper

class MyTestCase(unittest.TestCase):
    """
    Just a class to contain tests
    """


    @patch("sys.stdout", StringIO())
    def test_get_home_dir(self):
        """Tests get home directory of device"""
        expected = expanduser("~")
        self.assertEqual(expected, file_path_helper.get_home_directory())


    @patch("sys.stdout", StringIO())
    def test_get_storage_directory(self):
        """Tests get storage directory of program"""
        home_dir = expanduser("~")
        expected = f"{home_dir}/.code_clinic/"
        self.assertEqual(expected, file_path_helper.get_storage_directory(home_dir))


    @patch("sys.stdout", StringIO())
    def test_valid_path_exists(self):
        """Tests that path exist"""
        self.assertEqual(True, file_path_helper.path_exists("testing/unittests/"))


    @patch("sys.stdout", StringIO())
    def test_invalid_path_exists(self):
        """Tests that path does not exist"""
        self.assertEqual(False, file_path_helper.path_exists("testing/unittests/fisher/"))


    @patch("sys.stdout", StringIO())
    def test_create_directory(self):
        """Tests creating directory"""
        file_path_helper.create_directory("fisher/")
        self.assertTrue(exists("fisher/"))
        system("rm -rf fisher/")
