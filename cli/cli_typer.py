"""
CLI Typer
The file responsible for all CLI commands using typer
"""

# Import Statements
import typer

from checks.overall_checker import overall_checks
from commands.install_command import do_install
from commands.login_command import do_login
from commands.logout_command import do_logout
from commands.calendar_command import do_calendar
from installation.describe_install import describe_install
from output.rich_output import neat_print
from file_helpers.json_helper import load_json_file

app = typer.Typer()

@app.command()
def install():
    """
    Install Command - Installs all files necessary to run code clinics
    """
    do_install()


@app.command()
def setup():
    """
    Setup Command - Sets up the code clinic
    """
    neat_print("[magenta]Setting up code clinic...[/magenta]")
    describe_install()
    neat_print("[green]Setup complete![/green]")


@app.command()
def checks():
    """
    Checks Command - Checks all files necessary to run code clinics
    """
    overall_checks()


@app.command()
def login():
    """
    Login Command - Logs into the code clinic
    """
    storage_path = overall_checks()
    settings = load_json_file(f"{storage_path}settings.json")
    do_login(settings)


@app.command()
def logout():
    """
    Logout Command - Logs out of the code clinic
    """
    storage_path = overall_checks()
    settings = load_json_file(f"{storage_path}settings.json")
    do_logout(settings)


@app.command()
def calendar():
    """
    Calendar Command - Downloads, saves and displays events on calendars
    """
    storage_path = overall_checks()
    settings = load_json_file(f"{storage_path}settings.json")
    do_calendar(settings)


def start_typer():
    """Starts the app"""
    app()
