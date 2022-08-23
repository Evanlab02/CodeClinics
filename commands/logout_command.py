"""
Houses all logic to logout the user
"""

# From Import Statements
from output.rich_output import neat_print
from file_helpers.json_helper import overwrite_json_file
from google_calendar_API.token_helper import remove_token


def do_logout(settings: dict):
    """
    Logout Command - Logs out the user
    """
    neat_print("[magenta]Logging out...[/magenta]")

    storage_directory = settings["STORAGE PATH"]
    removed_token = remove_token(storage_directory)

    if removed_token:
        neat_print("[green]Logged out successfully[/green]")
    else:
        neat_print("[yellow]No user to logout[/yellow]")
