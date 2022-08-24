

from google_calendar_API.date_helper import get_dates
from google_calendar_API.connection_helper import create_api_connection
from google_calendar_API.download_helper import download_multi_events
from google_calendar_API.token_helper import load_token, validate_token
from google_calendar_API.event_helper import attend_event

from input_helpers.inquirer_helper import get_selected_event

def do_booking(settings: dict):
    """
    This function is used to book a code clinic session
    """
    calendar_id = settings['CALENDAR ID']
    connection = create_connection(settings)
    events = get_events(connection, calendar_id)
    selected_event_formatted = get_selected_event(events)
    selected_id = selected_event_formatted.split(" - ")[0]
    event = get_event_specifics(events, selected_id)
    attend_event(connection, calendar_id, event)

    
def get_event_specifics(events: list, selected_id: str):
    """
    Gets the specifics of the selected event.
    """
    for event in events:
        if event['id'] == selected_id:
            return event


def create_connection(settings: dict):
    """
    Creates a connection to the calendar.
    """
    storage_path = settings['STORAGE PATH']
    permission = settings['PERMISSIONS']

    creds = load_token(storage_path, permission)
    validate_token(creds)
    connection = create_api_connection(creds)
    return connection


def get_events(connection, calendar_id: str):
    """
    Gets events from the calendar.
    """
    dates = get_dates()

    events = download_multi_events(connection, dates, calendar_id)
    return events