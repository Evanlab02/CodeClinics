"""
Houses all the functions used to cancel a code clinic session
"""
import sys

from commands.command_helper import (
    create_connection,
    get_events,
    filter_events_to_open_events_only,
    filter_events_based_on_email
)

from input_helpers.inquirer_helper import get_selected_event

from google_calendar_API.event_helper import delete_event

def cancel_volunteer_slot(settings: dict):
    """
    Cancel Volunteer Slot - Cancels a volunteer slot
    """
    calendar_id = settings['CALENDAR ID']
    connection = create_connection(settings)
    events = get_events(connection, calendar_id)
    events = filter_events_to_open_events_only(events)

    user_email = input('Enter your email: ')
    events = filter_events_based_on_email(events, user_email)

    if len(events)==0:
        print('No events to cancel.')
        sys.exit(0)

    selected_event_formatted = get_selected_event(
        events,
        "What event would you like to cancel?"
    )
    selected_id = selected_event_formatted.split(" - ")[0]
    delete_event(connection, calendar_id, selected_id)
