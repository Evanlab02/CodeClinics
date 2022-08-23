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
    user_email = event_data["user email"]

    try:
        event_result = connection.events().insert(calendarId=calendar_id,
            body={
            "summary": f'Code_Clinic for {selected_day} at {selected_slot}',
            "description": 'STUDENT MUST SPECIFY WHAT THEY ARE STRUGGLING WITH',
            "start": {"dateTime": start_time},
            "end": {"dateTime": end_time},
            }
        ).execute()

        neat_print("[green]Created Event[/green]")
        neat_print(f"[green]Event: {event_result['summary']}[/green]")
        neat_print("\n[bold green]Please be respectful of others time"\
        +" and be on time for this Code Clinic.[/bold green]")
    except HttpError as error:
        neat_print("[bold red]Event Creation Failed[/bold red]")
        neat_print(f"[red]Unexpected Error: {error}[/red]")
