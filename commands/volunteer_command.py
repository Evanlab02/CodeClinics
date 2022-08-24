"""
Module containing functions to create events for volunteering and add them to the calendar.
"""

from datetime import datetime

from google_calendar_API.date_helper import (
    get_dates,
    get_rounded_time,
    generate_slots_template,
    populate_template,
    generate_available_slots,
    generate_new_event_start_and_finish_time
)
from google_calendar_API.connection_helper import create_api_connection
from google_calendar_API.download_helper import download_multi_events
from google_calendar_API.token_helper import load_token, validate_token
from google_calendar_API.event_helper import create_volunteering_event

from input_helpers.inquirer_helper import get_selected_day, get_selected_slot

from storage.calendar_saving import save_events

def do_volunteer(settings: dict):
    """
    Command to volunteer for a shift.
    """
    calendar_id = settings['CALENDAR ID']
    storage_path = settings['STORAGE PATH']
    connection = create_connection(settings)
    events = get_events(connection, calendar_id)

    today_rounded = get_rounded_time(datetime.now())

    slots_template = generate_slots_template(today_rounded)
    slots = populate_template(slots_template, today_rounded)

    selected_day = get_selected_day(slots)
    selected_day_slots = slots[selected_day]
    available_slots = generate_available_slots(events, selected_day, selected_day_slots)
    selected_slot = get_selected_slot(available_slots)
    times_for_event = generate_new_event_start_and_finish_time(selected_day, selected_slot)

    event_data = {
        "calendar id": calendar_id,
        "selected day": selected_day,
        "selected slot": selected_slot,
        "start time": times_for_event[0],
        "end time": times_for_event[1]
    }

    create_volunteering_event(connection, event_data)
    events = get_events(connection, calendar_id)
    save_events(storage_path, events)


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
