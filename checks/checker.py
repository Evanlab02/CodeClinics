"""Houses all logic to check that all installation checks pass"""
import sys

from time import sleep
from os import system
from json_files.json_helper import load_json_file
from installation.file_path_helper import get_home_directory, get_storage_directory, path_exists
from checks.setting_checker import does_settings_exist
from checks.credential_checker import does_credentials_exist
from output.my_output import neat_print

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


def do_checks():
    """Runs all checks and returns a list of all failed checks"""
    system("clear")
    output = "[bold cyan]Running Checks[/bold cyan]\n"
    output += "[bold cyan]-------------------------------------[/bold cyan]\n"
    neat_print(output)
    sleep(1)

    neat_print("[magenta]Getting Storage Path...[/magenta]")
    sleep(1)
    storage_path = get_storage_directory(get_home_directory())
    output += f"[magenta]Storage path: [/magenta][bold green]{storage_path}[/bold green]\n"
    system("clear")
    neat_print(output)

    neat_print("[magenta]Looking For Settings File...[/magenta]")
    sleep(1)
    try:
        settings_file = load_json_file(f"{storage_path}settings.json")
        output += "[magenta]Settings file exists: [/magenta][bold green]Yes[/bold green]\n"
        system("clear")
        neat_print(output)
    except FileNotFoundError:
        output += "[magenta]Settings file exists: [/magenta][bold red]No[/bold red]\n"
        output += "[red]Please reinstall the program[/red]\n"
        system("clear")
        neat_print(output)
        sys.exit(1)

    neat_print("[magenta]Looking For Credentials File...[/magenta]")
    sleep(1)
    if path_exists(f"{storage_path}credentials.json"):
        output += "[magenta]Credentials file exists: [/magenta][bold green]Yes[/bold green]\n"
        system("clear")
        neat_print(output)
    else:
        output += "[magenta]Credentials file exists: [/magenta][/bold red]No[/bold red]\n"
        system("clear")
        neat_print(output)

    neat_print("[magenta]Reading Settings File...[/magenta]")
    sleep(1)
    setting_checks = {
        "STORAGE PATH": "NO",
        "CALENDAR ID": "NO"}

    for key in settings_file:
        if key in setting_checks:
            setting_checks[key] = "YES"

    for key, value in setting_checks.items():
        if value == "YES":
            output += f"[magenta]{key} IS SET: [/magenta][bold green]Yes[/bold green]\n"
        else:
            output += f"[magenta]{key} IS SET: [/magenta][bold red]No[/bold red]\n"

    system("clear")
    neat_print(output)
    neat_print("[bold cyan]-------------------------------------[/bold cyan]\n")
