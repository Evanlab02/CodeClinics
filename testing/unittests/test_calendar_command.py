"""
Tests the calendar command
"""

#Import Statements
from datetime import datetime
import unittest

#From Import Statements
from unittest.mock import patch
from io import StringIO
from commands import calendar_command

class MyTestCase(unittest.TestCase):
    """
    Just a class to contain tests
    """
    @patch("sys.stdout", StringIO())
    def test_get_dates(self):
        """Tests get dates"""
        mock_now = datetime(2022, 8, 13, 14, 23, 18, 140878)
        dates = calendar_command.get_dates(mock_now)
        start_date_time = str(dates[0])
        start_date_time = start_date_time.split("+", maxsplit=1)[0]
        self.assertEqual(start_date_time, "2022-08-13T14:23:18.140878")
        end_date_time = str(dates[1])
        end_date_time = end_date_time.split("+", maxsplit=1)[0]
        self.assertEqual(end_date_time, "2022-08-20T14:23:18.140878")
