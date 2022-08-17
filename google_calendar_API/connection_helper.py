"""
a Module containing helper functions to
create the connection to the Google Calendar API
"""
import sys

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from output.rich_output import neat_print

def create_api_connection(creds):
    """Creates a connection to the Google API"""
    connection = None
    try:
        connection = build('calendar', 'v3', credentials=creds, static_discovery=False)
    except HttpError:
        neat_print("[red]Connection Failed[/red]")
        # Add Error Logging
        sys.exit(1)
    return connection
