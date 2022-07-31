"""
CLI Typer
The file responsible for all CLI commands using typer
"""

# Import Statements
import typer

#from import statements
from installation.directory_install import start_directory_installation
from output.my_output import display_installation

app = typer.Typer()

@app.command()
def install():
    """
    Install Command - Installs all files necessary to run code clinics
    """
    installation_details = {}
    start_directory_installation(installation_details)


def start_typer():
    """Starts the app"""
    app()
