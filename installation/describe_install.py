"""
This file was created to continue the installation process
and to make the installation process easier to read. This is improvement
for both users and developers.
"""

from os import system
import sys
from output.my_output import neat_print
from checks.checker import get_initial_continued_checks
from installation.file_path_helper import get_home_directory, get_storage_directory
from installation.continue_install import continue_install

def describe_install():
    """Continues the installation process."""
    clean_up_terminal()
    welcome_message()
    storage_path = get_storage()
    file_checks = get_initial_continued_checks(storage_path)
    files_installed = read_file_checks(file_checks)

    if not files_installed:
        neat_print("[red]Installation Failed[/red]")
        neat_print("[red]Please check the above messages for more information.[/red]")
        sys.exit(1)

    display_credentials_description_to_user(storage_path)
    display_settings_description_to_user(storage_path)
    continue_install(storage_path)


def display_settings_description_to_user(storage_path: str):
    """Displays the settings description to the user."""
    neat_print("[bold green]-------------------------------------[/bold green]")
    neat_print("[bold green]DISPLAYING SETTINGS[/bold green]")
    neat_print("[bold green]-------------------------------------[/bold green]")
    neat_print(f"{storage_path}settings.json")
    neat_print("[green]The settings are used to configure the code clinics \
software.[/green]")
    neat_print("[green]The settings are stored in the settings file in the \
storage directory.[/green]")
    neat_print("[bold green]-------------------------------------[/bold green]")
    neat_print("[bold green]PRESS ENTER TO CONTINUE[/bold green]")
    input()
    system("clear")


def display_credentials_description_to_user(storage_path: str):
    """Displays the credentials description to the user."""
    neat_print("[bold green]-------------------------------------[/bold green]")
    neat_print("[bold green]DISPLAYING CREDENTIALS[/bold green]")
    neat_print("[bold green]-------------------------------------[/bold green]")
    neat_print(f"{storage_path}credentials.json")
    neat_print("[green]The credentials are used to connect to the API \
and to authenticate the user.[/green]")
    neat_print("[green]The credentials are stored in the credentials file \
in the storage directory.[/green]")
    neat_print("[bold red]Never share your credentials with anyone![/bold red]")
    neat_print("[bold green]-------------------------------------[/bold green]")
    neat_print("[bold green]PRESS ENTER TO CONTINUE[/bold green]")
    input()
    system("clear")


def read_file_checks(file_checks: dict):
    """Reads the file checks."""
    valid = True
    neat_print("[bold green]-------------------------------------[/bold green]")
    neat_print("[bold green]CHECKING FILE STATUS[/bold green]")
    neat_print("[bold green]-------------------------------------[/bold green]")

    for key in file_checks:
        neat_print(f"[cyan]{key}[/cyan]: {file_checks[key]}")
        if file_checks[key] == "No":
            valid = False

    neat_print("[bold green]-------------------------------------[/bold green]")
    neat_print("[bold green]PRESS ENTER TO CONTINUE[/bold green]")
    input()
    system("clear")
    return valid


def welcome_message():
    """Prints the welcome message."""
    neat_print("[bold green]WELCOME TO CODE CLINICS INSTALLER 2.0[/bold green]")
    neat_print("[bold green]-------------------------------------[/bold green]")
    neat_print("[bold green]Press ENTER to continue[/bold green]")
    input()
    system("clear")


def get_storage():
    """Gets the storage path."""
    storage_path = get_storage_directory(get_home_directory())
    neat_print(f"[cyan]Storage Path[/cyan]: {storage_path}")
    neat_print("[green]The storage path is where all config files, logs, and \
other files will be stored.[/green]")
    neat_print("[green]These files might be useful if you want to run code \
clinics in conjunction with other software.[/green]")
    neat_print("[bold green]-------------------------------------[/bold green]")
    neat_print("[bold green]PRESS ENTER TO CONTINUE[/bold green]")
    input()
    system("clear")
    return storage_path


def clean_up_terminal():
    """Cleans up the terminal."""
    system("clear")
