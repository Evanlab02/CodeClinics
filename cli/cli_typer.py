"""
CLI Typer
The file responsible for all CLI commands using typer
"""

# Import Statements
from datetime import datetime

import typer

from checks.overall_checker import overall_checks

from commands.install_command import do_install
from commands.login_command import do_login
from commands.logout_command import do_logout
from commands.calendar_command import do_calendar
from commands.volunteer_command import do_volunteer
from commands.book_command import do_booking
from commands.cancel_command import cancel_volunteer_slot

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
    starting_time = datetime.now()
    storage_path = overall_checks()
    settings = load_json_file(f"{storage_path}settings.json")
    settings["STARTING TIME"] = starting_time
    do_calendar(settings)


@app.command()
def volunteer():
    """
    Volunteer Command - Adds a volunteer to the code clinic session
    """
    storage_path = overall_checks()
    settings = load_json_file(f"{storage_path}settings.json")
    do_volunteer(settings)


@app.command()
def book():
    """
    Book Command - Books a code clinic session
    """
    storage_path = overall_checks()
    settings = load_json_file(f"{storage_path}settings.json")
    do_booking(settings)


@app.command()
def cancel(
    member_type: str = \
        typer.Option("", help="Type of slot you are cancelling(Volunteering/Student).")
    ):
    """
    Cancel Command - Cancels a code clinic session
    """
    storage_path = overall_checks()
    settings = load_json_file(f"{storage_path}settings.json")
    if member_type.lower() == "volunteering":
        cancel_volunteer_slot(settings)
    else:
        print("Invalid member type")


def start_typer():
    """Starts the app"""
    app()
