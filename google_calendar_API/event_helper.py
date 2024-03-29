"""
Module containing helper functions to create events.
"""

from googleapiclient.errors import HttpError
from output.rich_output import neat_print


def create_volunteering_event(connection, event_data: dict):
    """
    Creates a volunteering event based on the event data.
    """
    calendar_id = event_data["calendar id"]
    selected_day = event_data["selected day"]
    selected_slot = event_data["selected slot"]
    start_time = event_data["start time"]
    end_time = event_data["end time"]
    user_email = input("Enter your email: ")
    user_name = input("Enter your full name and surname: ")

    try:
        event_result = connection.events().insert(calendarId=calendar_id,
            body={
            "summary": f'Code_Clinic for {selected_day} at {selected_slot}',
            "description": 'STUDENT MUST SPECIFY WHAT THEY ARE STRUGGLING WITH',
            "start": {"dateTime": start_time},
            "end": {"dateTime": end_time},
            "attendees": [
                {
                    "email": user_email,
                    "displayName": user_name,
                    "organizer": True
                }
            ]
            }
        ).execute()

        neat_print("[green]Created Event[/green]")
        neat_print(f"[green]Event: {event_result['summary']}[/green]")
        neat_print("\n[bold green]Please be respectful of others time"\
        +" and be on time for this Code Clinic.[/bold green]")
    except HttpError as error:
        neat_print("[bold red]Event Creation Failed[/bold red]")
        neat_print(f"[red]Unexpected Error: {error}[/red]")


def attend_event(connection, calendar_id: str, event: dict):
    """
    Creates a volunteering event based on the event data.
    """
    user_email = input("Enter your email: ")
    user_name = input("Enter your full name and surname: ")
    description = input("Please explain what you are struggling with: ")
    event["attendees"].append({
        "email": user_email,
        "displayName": user_name,
        "organizer": False
    })
    event["description"] = description

    try:
        event_result = connection.events().update(calendarId=calendar_id, eventId=event["id"],
            body=event
        ).execute()

        neat_print("[green]Updated Event[/green]")
        neat_print(f"[green]Event: {event_result['summary']}[/green]")
        neat_print("\n[bold green]Please be respectful of others time"\
        +" and be on time for this Code Clinic.[/bold green]")
    except HttpError as error:
        neat_print("[bold red]Event Creation Failed[/bold red]")
        neat_print(f"[red]Unexpected Error: {error}[/red]")



def remove_attendance_from_event(
    connection,
    calendar_id: str,
    event: dict,
    user_email: str
    ):
    """
    Removes an attendance from an event.
    """
    attendee = event["attendees"][1]

    if attendee["email"] == user_email:
        event["attendees"].pop(1)

    try:
        connection.events().update(calendarId=calendar_id, eventId=event["id"],
            body=event
        ).execute()

        neat_print("[green]Updated Event[/green]")
    except HttpError as error:
        neat_print("[bold red]Event Creation Failed[/bold red]")
        neat_print(f"[red]Unexpected Error: {error}[/red]")



def delete_event(connection, calendar_id: str, event_id: str):
    """
    Deletes an event.
    """
    try:
        connection.events().delete(calendarId=calendar_id, eventId=event_id).execute()
        neat_print("[green]Deleted Event[/green]")
    except HttpError as error:
        neat_print("[bold red]Event Deletion Failed[/bold red]")
        neat_print(f"[red]Unexpected Error: {error}[/red]")
