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
from installation import (
    file_path_helper,
    calendar_id,
    continue_install,
    describe_install)

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

    @patch("sys.stdin", StringIO("ABCD\n\n"))
    @patch("sys.stdout", StringIO())
    def test_get_calendar_id(self):
        """Tests getting calendar id"""
        expected = "ABCD"
        self.assertEqual(expected, calendar_id.get_calendar_id())


    @patch("sys.stdout", StringIO())
    def test_load_settings(self):
        """Tests loading settings"""
        expected = {"SETTINGS": "THIS IS A TEST"}
        self.assertEqual(expected, continue_install.\
            load_settings_on_disk("testing/unittests/resources/settings.json"))


    @patch("sys.stdout", StringIO())
    def test_load_settings_invalid(self):
        """Tests loading settings"""
        try:
            expected = {"SETTINGS": "THIS IS A TEST"}
            self.assertEqual(expected, continue_install.\
                load_settings_on_disk("testing/unittests/settings.json"))
        except FileNotFoundError:
            print("TEST PASSED")

    @patch("sys.stdin", StringIO("\n"))
    @patch("sys.stdout", StringIO())
    def test_read_file_checks_valid(self):
        """Tests reading file"""
        mock_value = {"EXISTS": "Yes"}
        self.assertTrue(describe_install.read_file_checks(mock_value))


    @patch("sys.stdin", StringIO("\n"))
    @patch("sys.stdout", StringIO())
    def test_read_file_checks_invalid(self):
        """Tests reading file"""
        mock_value = {"EXISTS": "No"}
        self.assertFalse(describe_install.read_file_checks(mock_value))
