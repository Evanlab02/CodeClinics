"""
Tests the checks modules
"""

#Import Statements
import unittest

#From Import Statements
from unittest.mock import patch
from io import StringIO
from checks import checker

class MyTestCase(unittest.TestCase):
    """
    Just a class to contain tests
    """

    @patch("sys.stdout", StringIO())
    def test_run_checks_valid(self):
        """Tests run checks valid"""
        failed_checks = checker.run_checks({"STORAGE DIRECTORY": "testing/unittests/resources/"})
        self.assertEqual(failed_checks, [])
        self.assertEqual(len(failed_checks), 0)


    @patch("sys.stdin", StringIO("\n"))
    @patch("sys.stdout", StringIO())
    def test_run_checks_invalid(self):
        """Tests run checks invalid"""
        failed_checks = checker.run_checks({"STORAGE DIRECTORY": "testing/unittests/"})
        self.assertEqual(failed_checks, [False])
        self.assertEqual(len(failed_checks), 1)


    @patch("sys.stdout", StringIO())
    def test_initial_checks_valid(self):
        """Tests initial checks"""
        checks = checker.get_initial_continued_checks("testing/unittests/resources/")
        self.assertEqual(checks, {"SETTINGS EXIST": "Yes", "CREDENTIALS EXIST": "Yes"})


    @patch("sys.stdin", StringIO("\n"))
    @patch("sys.stdout", StringIO())
    def test_initial_checks_invalid(self):
        """Tests initial checks"""
        checks = checker.get_initial_continued_checks("testing/unittests/")
        self.assertEqual(checks, {"SETTINGS EXIST": "No", "CREDENTIALS EXIST": "No"})
