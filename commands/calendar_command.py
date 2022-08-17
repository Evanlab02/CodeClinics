"""
Houses all the logic for the calendar command.
"""

#From Import statements
from os import system
from datetime import datetime
from api.google_api_helper import get_start_and_end_date, create_api_connection, download_all_events
from api.token import load_token, validate_token
from output.my_output import neat_print
from output.tabulate_output import display_tabulate_events
from output.csv_output import display_csv_events
from json_files.json_helper import save_json_events
from csv_files.csv_helper import save_csv_events

def save_events(calendar_settings: dict):
    """
    Saves the events on the disk
    """
    neat_print("[magenta]Saving events...[/magenta]")
    save_json_events(calendar_settings)
    save_csv_events(calendar_settings)


def download_and_aggregate_events(calendar_settings: dict):
    """
    Downloads and aggregates the events of the next 7 days
    """
    calendar_settings = download_all_events(calendar_settings)

    all_events = list(calendar_settings['events'])

    calendar_settings["calendar id"] = "primary"
    calendar_settings = download_all_events(calendar_settings)

    for event in calendar_settings['events']:
        all_events.append(event)

    calendar_settings["events"] = all_events
    return all_events


def do_calendar(settings: dict):
    """
    Downloads and prints the events of the next 7 days using the Google Calendar API.
    """
    storage_path = settings['STORAGE PATH']
    calendar_id = settings['CALENDAR ID']
    creds = load_token(settings)
    validate_token(creds)
    connection = create_api_connection(creds)
    dates = get_start_and_end_date(datetime.now())
    data_saving_format = settings['DATA SAVING FORMAT']
    data_display_format = settings['DATA DISPLAY FORMAT']

    calendar_settings = {
        'storage path': storage_path,
        'calendar id': calendar_id,
        'credentials': creds,
        'connection': connection,
        'dates': dates,
        'data saving format': data_saving_format
    }

    all_events = download_and_aggregate_events(calendar_settings)
    save_events(calendar_settings)
    system("clear")

    if data_display_format == 'JSON':
        neat_print(all_events)
    elif data_display_format == 'CSV':
        display_csv_events(calendar_settings)
    elif data_display_format == 'Tabulate':
        display_tabulate_events(calendar_settings)
    else:
        neat_print("[yellow]NO OUTPUT[/yellow]")
