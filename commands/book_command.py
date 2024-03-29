"""
Houses all the functions used to book a code clinic session
"""

from commands.command_helper import (
    create_connection,
    get_all_events,
    get_events,
    get_event_specifics,
    filter_events_to_open_events_only
)
from google_calendar_API.event_helper import attend_event

from input_helpers.inquirer_helper import get_selected_event

from storage.calendar_saving import save_events

def do_booking(settings: dict):
    """
    This function is used to book a code clinic session
    """
    calendar_id = settings['CALENDAR ID']
    storage_path = settings['STORAGE PATH']
    connection = create_connection(settings)
    events = get_events(connection, calendar_id)
    events = filter_events_to_open_events_only(events)
    selected_event_formatted = get_selected_event(events)
    selected_id = selected_event_formatted.split(" - ")[0]
    event = get_event_specifics(events, selected_id)
    attend_event(connection, calendar_id, event)
    events = get_all_events(connection, calendar_id)
    save_events(storage_path, events)
