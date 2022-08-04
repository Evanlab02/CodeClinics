"""
Install command - Installs all files necessary to run code clinics
"""

import sys

#from import statements
from installation.directory_install import start_directory_installation
from installation.settings_install import install_settings
from installation.receive_settings import receive_settings_from_user
from json_files.json_helper import load_json_file, overwrite_json_file
from checks.checker import run_checks
from output.my_output import neat_print

def do_install():
    """
    Install Command - Installs all files necessary to run code clinics
    """
    check_and_installation_resources = {}
    start_directory_installation(check_and_installation_resources)
    install_settings(check_and_installation_resources)

    storage_directory = check_and_installation_resources["STORAGE DIRECTORY"]
    neat_print(storage_directory)
    settings_file_path = f"{storage_directory}settings.json"
    neat_print(settings_file_path)
    user_settings = receive_settings_from_user()
    neat_print(user_settings)

    try:
        disk_settings = load_json_file(settings_file_path)
        neat_print(disk_settings)
    except FileNotFoundError as exception:
        neat_print(f"[cyan]Settings file not found[/cyan]: [red]{exception}[/red]")
        sys.exit(1)

    if disk_settings == user_settings:
        neat_print("[green]Settings do not need to be updated[/green]")
    else:
        try:
            neat_print("[yellow]User Settings need to be updated[/yellow]")
            neat_print("[cyan]User Settings[/cyan]:")
            neat_print(user_settings)
            neat_print("[magenta]Disk Settings[/magenta]:")
            neat_print(disk_settings)
            overwrite_json_file(settings_file_path, user_settings)
        except FileNotFoundError as exception:
            neat_print(f"[cyan]Settings file not found[/cyan]: [red]{exception}[/red]")
            sys.exit(1)
        except TypeError as exception:
            neat_print(f"[cyan]Hidden Type Error[/cyan]: [red]{exception}[/red]")
            sys.exit(1)

    if False in run_checks(check_and_installation_resources):
        neat_print("[red]Installation Failed[/red]")
    else:
        neat_print("[green]Installation Successful[/green]")
