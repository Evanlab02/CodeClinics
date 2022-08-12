"""
Houses all the logic for the calendar command.
"""
#import statements
import sys

#From Import statements
from datetime import datetime
from api.google_api_helper import get_start_and_end_date, create_api_connection, download_events
from api.token import load_token, check_token
from output.my_output import neat_print
from json_files.json_helper import load_json_file, overwrite_json_file

def get_storage_path(settings: dict):
    """
    Returns the storage path of the settings.
    """
    storage_path = settings['STORAGE PATH']
    neat_print(f"[magenta]STORAGE PATH[/magenta] = [cyan]{storage_path}[/cyan]")
    return storage_path


def get_calendar_id(settings: dict):
    """
    Returns the calendar id of the settings.
    """
    neat_print("[magenta]Retrieving calendar ID...[/magenta]")
    calendar_id = settings['CALENDAR ID']
    neat_print(f"[magenta]CALENDAR ID[/magenta] = [cyan]{calendar_id}[/cyan]")
    return calendar_id


def retrieve_creds(settings: dict):
    """
    Retrieves the credentials from the settings.
    """
    neat_print("[magenta]Retrieving credentials...[/magenta]")
    creds = load_token(settings)
    neat_print("[green]Credentials loaded.[/green]")
    return creds


def validate_token(creds):
    """
    Validates the token.
    """
    neat_print("[magenta]Validating token...[/magenta]")
    token = check_token(creds)
    if token:
        neat_print("[green]Token is valid.[/green]")
    else:
        neat_print("[red]Token is invalid.[/red]")
        neat_print("[yellow]Please login using code_clinic login[/yellow]")
        sys.exit("Token is invalid.")


def get_connection(creds):
    """
    Creates a connection to the Google API.
    """
    neat_print("[magenta]Creating API connection...[/magenta]")
    connection = create_api_connection(creds)
    neat_print("[green]Connected![/green]")
    return connection


def get_dates():
    """
    Gets the starting and ending dates of the next 7 days
    """
    neat_print("Retrieving start and end date...")
    today, seven_days = get_start_and_end_date(datetime.now())
    neat_print(f"[cyan]START DATE[/cyan] = [magenta]{today}[/magenta]")
    neat_print(f"[cyan]END DATE[/cyan] = [magenta]{seven_days}[/magenta]")
    return today, seven_days


def download_and_save_events(calendar_settings: dict):
    """
    Downloads and saves the events of the next 7 days using the Google Calendar API.
    """
    neat_print("[magenta]Downloading events...[/magenta]")
    events = download_events(
        calendar_settings["dates"],
        calendar_settings["connection"],
        calendar_settings["calendar id"]
    )
    neat_print("[green]Events downloaded![/green]")

    neat_print("[magenta]Saving events...[/magenta]")
    calendar_settings.update({"events": events})
    save_events(calendar_settings)
    return events


def save_events(calendar_settings: dict):
    """
    Saves the events on the disk in settings.json file
    """
    storage_path = calendar_settings['storage path']
    memory_events = calendar_settings['events']

    try:
        disk_events = load_json_file(f"{storage_path}events.json")
        if disk_events == memory_events:
            neat_print("[green]Events are the same.[/green]")
            neat_print("[green]Skipping saving process.[/green]")
        else:
            overwrite_json_file(f"{storage_path}events.json", memory_events)
            neat_print("[green]Events saved![/green]")
    except FileNotFoundError:
        neat_print("[yellow]Could not find events.json[/yellow]")
        neat_print("[yellow]Creating events.json...[/yellow]")
        overwrite_json_file(f"{storage_path}events.json", memory_events)
        neat_print("[green]events.json created![/green]")
        neat_print("[green]Events saved![/green]")


def do_calendar(settings: dict):
    """
    Downloads and prints the events of the next 7 days using the Google Calendar API.
    """
    storage_path = get_storage_path(settings)
    calendar_id = get_calendar_id(settings)
    creds = retrieve_creds(settings)
    validate_token(creds)
    connection = get_connection(creds)
    dates = get_dates()

    calendar_settings = {
        'storage path': storage_path,
        'calendar id': calendar_id,
        'credentials': creds,
        'connection': connection,
        'dates': dates
    }

    events = download_and_save_events(calendar_settings)
    neat_print(events)
