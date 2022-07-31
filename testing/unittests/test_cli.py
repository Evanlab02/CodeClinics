"""
Tests cli_typer
"""

#Import Statements
import unittest

#From Import Statements
from os import system
from os.path import expanduser, exists
from unittest.mock import patch
from io import StringIO
from cli import cli_typer

class MyTestCase(unittest.TestCase):
    """
    Just a class to contain tests
    """

    @patch("sys.stdout", StringIO())
    def test_install_command(self):
        """Tests install command"""
        cli_typer.install()
        home_directory = expanduser("~")
        storage_directory = f"{home_directory}/.code_clinic/"
        self.assertTrue(exists(storage_directory))
        system(f"rm -rf {storage_directory}")
