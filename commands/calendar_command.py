"""
Houses all the logic for the calendar command.
"""

#From Import statements
from google_calendar_API.date_helper import get_dates
from google_calendar_API.connection_helper import create_api_connection
from google_calendar_API.download_helper import download_events, download_multi_events
from google_calendar_API.token_helper import load_token, validate_token

from output.csv_output import display_csv_events
from output.tabulate_output import display_tabulate_events
from output.rich_output import neat_print, calendar_print

from storage.calendar_saving import save_events

def do_calendar(settings: dict):
    """
    Downloads and prints the events of the next 7 days using the Google Calendar API.
    """
    storage_path = settings['STORAGE PATH']
    calendar_id = settings['CALENDAR ID']
    permission = settings['PERMISSIONS']
    creds = load_token(storage_path, permission)
    validate_token(creds)
    connection = create_api_connection(creds)
    dates = get_dates()
    data_display_format = settings['DATA DISPLAY FORMAT']
    starting_time = settings['STARTING TIME']

    events = download_events(connection, dates)

    if data_display_format == 'JSON':
        neat_print(events)
    elif data_display_format == 'CSV':
        display_csv_events(storage_path)
    elif data_display_format == 'Tabulate':
        display_tabulate_events(storage_path)
    else:
        calendar_print(events, starting_time)

    events = download_multi_events(connection, dates, calendar_id)
    save_events(storage_path, events)
