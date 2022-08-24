"""
Houses functions that are commonly used accross the commands package.
"""

from google_calendar_API.date_helper import get_dates
from google_calendar_API.connection_helper import create_api_connection
from google_calendar_API.download_helper import download_events
from google_calendar_API.token_helper import load_token, validate_token


def get_event_specifics(events: list, selected_id: str):
    """
    Gets the specifics of the selected event.
    """
    event_specifics = {}
    for event in events:
        if event['id'] == selected_id:
            event_specifics = event
    return event_specifics


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

    events = download_events(connection, dates, calendar_id)
    return events


def filter_events_to_open_events_only(events: list):
    """
    Filters the events to only open events.
    """
    open_events = []
    for event in events:
        if not len(event['attendees']) > 1:
            open_events.append(event)
    return open_events
