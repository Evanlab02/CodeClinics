"""
Houses all logic to check that the settings file
is correct
"""

from installation.file_path_helper import path_exists

def does_settings_exist(storage_path: str):
    """
    Checks if settings.json exists
    """
    if path_exists(storage_path + "settings.json"):
        return "Yes"
    return "No"
