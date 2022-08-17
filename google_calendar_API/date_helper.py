"""
a Module containing helper functions to
get dates in the correct format for the
Google Calendar API
"""

from datetime import datetime, timedelta

def get_start_date(today: datetime):
    """Gets the start date for the next 7 days"""
    return today.astimezone().isoformat()


def get_end_date(today: datetime):
    """Gets the end date for the next 7 days"""
    return (today+timedelta(7)).astimezone().isoformat()


def get_dates():
    """Gets the start and end date for the next 7 days"""
    now = datetime.now()
    today = get_start_date(now)
    final_date = get_end_date(now)
    return today, final_date
