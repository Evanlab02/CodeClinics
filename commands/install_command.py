"""
Install command - Installs all files necessary to run code clinics
"""

import sys

#from import statements
from installation.directory_install import start_directory_installation
from installation.settings_install import install_settings
from installation.describe_install import describe_install
from checks.overall_checker import run_first_checks
from output.rich_output import neat_print

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

    if False in run_first_checks(check_and_installation_resources):
        neat_print("[red]Installation Failed[/red]")
        sys.exit(1)
    else:
        neat_print("[green]Initial Installation Successful[/green]")

    neat_print("[cyan]Continue Installation Process...[/cyan]")
    describe_install()
    neat_print("[green]Installation Complete[/green]")
