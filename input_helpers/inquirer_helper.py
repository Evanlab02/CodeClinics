"""
Module containing helper functions to get input from the user using inquirer.
"""

import inquirer

def get_selected_day(slots):
    """
    Gets the selected day from the user.
    """
    volunteer_slots = [
    inquirer.List('Volunteer Days',
                message="What day do you wish to volunteer?",
                choices=slots.keys(),
            ),
    ]

    selected_day = inquirer.prompt(volunteer_slots)["Volunteer Days"]
    return selected_day


def get_selected_slot(slots):
    """
    Gets the selected slot from the user.
    """
    volunteer_slots = [
    inquirer.List('Volunteer Slots',
                message="What slot do you wish to volunteer?",
                choices=slots,
            ),
    ]
    selected_slot = inquirer.prompt(volunteer_slots)["Volunteer Slots"]
    return selected_slot


def get_selected_event(events: list):
    """
    Gets the selected event from the user.
    """
    event_list = [f"{event['id']} - {event['summary']}" for event in events]
    event_slots = [
    inquirer.List('Events',
                message="What event do you wish to attend?",
                choices=event_list,
            ),
    ]
    selected_event = inquirer.prompt(event_slots)["Events"]
    return selected_event
