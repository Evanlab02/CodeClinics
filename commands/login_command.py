"""Houses all logic to login a user in with their gmail account"""

from google_calendar_API.token_helper import create_token, load_token, check_token
from file_helpers.json_helper import overwrite_json_file
from output.rich_output import neat_print

def do_login(settings: dict):
    """
    Login Command - Logs into the code clinic
    """
    storage_path = settings["STORAGE PATH"]
    permission = settings["PERMISSIONS"]
    neat_print("[magenta]Logging in...[/magenta]")
    creds = load_token(storage_path, permission)

    if check_token(creds):
        neat_print("[green]a User is logged in[/green]")
    else:
        create_token(storage_path, permission)
        neat_print("[green]Logged in![/green]")
    
