"""Module containing helper functions to find paths to storage files"""

from os import mkdir
from os.path import expanduser, exists

def get_home_directory():
    """Gets the home directory of the device"""
    home_directory = expanduser("~")
    return home_directory


def get_storage_directory(home_directory: str):
    """Gets the storage directory for the program"""
    storage_directory = f"{home_directory}/.code_clinic/"
    return storage_directory


def path_exists(file_path: str):
    """Determines if the path exists"""
    is_path = exists(file_path)
    return is_path


def create_directory(file_path: str):
    """Creates a directory at specified path"""
    mkdir(file_path)
