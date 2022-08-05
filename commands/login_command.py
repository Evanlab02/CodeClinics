"""Houses all logic to login a user in with their gmail account"""

from api.token import create_token
from output.my_output import neat_print

def do_login(settings: dict):
    """
    Login Command - Logs into the code clinic
    """
    neat_print("[magenta]Logging in...[/magenta]")
    create_token(settings)
    neat_print("[green]Logged in![/green]")
