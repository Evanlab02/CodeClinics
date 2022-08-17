"""
Tests the checks modules
"""

#Import Statements
import unittest

#From Import Statements
from unittest.mock import patch
from io import StringIO
from checks import overall_checker

class MyTestCase(unittest.TestCase):
    """
    Just a class to contain tests
    """

    @patch("sys.stdout", StringIO())
    def test_initial_checks_valid(self):
        """Tests initial checks"""
        checks = overall_checker.run_second_checks("testing/unittests/resources/")
        self.assertEqual(checks, {"SETTINGS EXIST": "Yes", "CREDENTIALS EXIST": "Yes"})


    @patch("sys.stdin", StringIO("\n"))
    @patch("sys.stdout", StringIO())
    def test_initial_checks_invalid(self):
        """Tests initial checks"""
        checks = overall_checker.run_second_checks("testing/unittests/")
        self.assertEqual(checks, {"SETTINGS EXIST": "No", "CREDENTIALS EXIST": "No"})
