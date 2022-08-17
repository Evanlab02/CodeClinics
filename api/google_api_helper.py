"""
Houses all the functions for the Google API
"""

import sys

from datetime import datetime, timedelta
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_start_and_end_date(now: datetime):
    """Gets today and 7 days later date and returns it in isoformat"""
    today = now.astimezone()
    seven_days = today+timedelta(7)
    today = today.isoformat()
    seven_days = seven_days.isoformat()
    return today, seven_days


def create_api_connection(creds):
    """Creates a connection to the Google API"""
    connection = None
    try:
        connection = build('calendar', 'v3', credentials=creds, static_discovery=False)
    except HttpError as error:
        print(f'An error occurred: {error}')
        sys.exit("Connection Failed.")
    return connection


def download_events(dates:tuple, connection, calendar_id: str):
    """Download events into memory from the api"""
    seven_day_calendar = connection.events().list(
        calendarId=calendar_id,
        timeMin = dates[0],
        timeMax = dates[1],
        singleEvents=True,
        orderBy='startTime').execute()

    events = seven_day_calendar.get('items', [])
    return events
