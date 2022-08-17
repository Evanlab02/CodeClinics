"""Houses all logic to check that all installation checks pass"""
import sys

from os import system
from file_helpers.json_helper import load_json_file
from installation.file_path_helper import get_home_directory, get_storage_directory, path_exists
from checks.setting_checker import does_settings_exist
from checks.credential_checker import does_credentials_exist
from output.rich_output import neat_print

def run_first_checks(program_details: dict):
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


def run_second_checks(storage_path: str):
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


def overall_checks():
    """Runs all checks and returns a list of all failed checks"""
    system("clear") #Replace with os helper
    storage_path = get_storage_directory(get_home_directory())

    try:
        settings_file = load_json_file(f"{storage_path}settings.json")
    except FileNotFoundError:
        neat_print("[magenta]Settings file exists: [/magenta][bold red]No[/bold red]")
        neat_print("[red]Please reinstall the program[/red]")
        # Add Error Logging
        sys.exit(2)

    if not path_exists(f"{storage_path}credentials.json"):
        neat_print("[magenta]Credentials file exists: [/magenta][/bold red]No[/bold red]")
        # Add Error Logging
        sys.exit(3)

    setting_checks = {
        "STORAGE PATH": "NO",
        "CALENDAR ID": "NO",
        "PERMISSIONS": "NO",
        "DATA SAVING FORMAT": "NO",
        "DATA DISPLAY FORMAT": "NO",
    }

    for key in settings_file:
        if key in setting_checks:
            setting_checks[key] = "YES"

    valid = True
    for key, value in setting_checks.items():
        if value != "YES":
            valid = False

    if not valid:
        neat_print("[red]Checks failed[/red]\n")
        # Add Error Logging
        sys.exit(4)

    return storage_path
