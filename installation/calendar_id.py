"""
Houses all logic to get and validate the calendar ID
"""

from os import system
from output.my_output import neat_print


def get_calendar_id():
    """Gets the calendar ID from the user"""
    neat_print("[bold green]Calendar ID[/bold green]")
    neat_print("[bold green]-------------------------------------[/bold green]")
    neat_print("[green]The calendar ID is used to retrieve and \
create events on the central Google calendar. This id represents the main code \
clinics calendar.[/green]")
    neat_print("[green]Please enter the calendar id[/green]")
    calendar_id = input("--> ")
    neat_print(f"[cyan]Received Calendar ID: [/cyan][magenta]{calendar_id}[/magenta]")
    neat_print("[bold green]-------------------------------------[/bold green]")
    neat_print("[bold green]PRESS ENTER TO CONTINUE[/bold green]")
    input()
    system("clear")
    return calendar_id
