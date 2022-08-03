"""
CLI Typer
The file responsible for all CLI commands using typer
"""

# Import Statements
import typer

#from import statements
from installation.directory_install import start_directory_installation
from installation.settings_install import install_settings
from checks.checker import run_checks
from output.my_output import neat_print

app = typer.Typer()

@app.command()
def install():
    """
    Install Command - Installs all files necessary to run code clinics
    """
    check_and_installation_resources = {}
    start_directory_installation(check_and_installation_resources)
    install_settings(check_and_installation_resources)
    if False in run_checks(check_and_installation_resources):
        neat_print("[red]Installation Failed[/red]")
    else:
        neat_print("[green]Installation Successful[/green]")


def start_typer():
    """Starts the app"""
    app()
