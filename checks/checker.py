"""Houses all logic to check that all installation checks pass"""

from checks.setting_checker import does_settings_exist
from checks.credential_checker import does_credentials_exist

def run_checks(program_details: dict):
    """Runs all checks and returns a list of all failed checks"""
    program_details.update({"CREDENTIALS EXIST": does_credentials_exist(program_details)})

    failed_checks = [
        program_details.get(key)
        for key in program_details
        if program_details.get(key) is False and
        key != "INSTALLED" and
        key != "EXISTS"
    ]

    return failed_checks


def get_initial_continued_checks(storage_path: str):
    """Returns a dictionary of all checks results"""
    settings_exist = does_settings_exist(storage_path)

    credentials_exist = does_credentials_exist({"STORAGE DIRECTORY": storage_path})

    if credentials_exist:
        credentials_exist = "Yes"
    else:
        credentials_exist = "No"

    return {
        "SETTINGS EXIST": settings_exist,
        "CREDENTIALS EXIST": credentials_exist
    }
