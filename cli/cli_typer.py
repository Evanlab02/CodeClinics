"""
CLI Typer
The file responsible for all CLI commands using typer
"""

# Import Statements
import typer

from checks.checker import do_checks
from commands.install_command import do_install

app = typer.Typer()

@app.command()
def install():
    """
    Install Command - Installs all files necessary to run code clinics
    """
    do_install()


@app.command()
def checks():
    """
    Checks Command - Checks all files necessary to run code clinics
    """
    do_checks()


def start_typer():
    """Starts the app"""
    app()
