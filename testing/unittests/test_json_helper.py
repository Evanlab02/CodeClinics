"""
Tests json helper functions
"""

#Import Statements
import unittest

#From Import Statements
from unittest.mock import patch
from io import StringIO
from file_helpers.json_helper import load_json_file, overwrite_json_file

class MyTestCase(unittest.TestCase):
    """
    Just a class to contain tests
    """

    @patch("sys.stdout", StringIO())
    def test_read_write_json(self):
        """Tests get home directory of device"""
        expected = {}
        data = load_json_file("testing/unittests/resources/read_write.json")
        self.assertEqual(expected, data)
        overwrite_json_file("testing/unittests/resources/read_write.json",\
        {"This is a test": "This is a test"})
        data = load_json_file("testing/unittests/resources/read_write.json")
        self.assertEqual({"This is a test": "This is a test"}, data)
        overwrite_json_file("testing/unittests/resources/read_write.json", {})
        data = load_json_file("testing/unittests/resources/read_write.json")
        self.assertEqual(expected, data)
