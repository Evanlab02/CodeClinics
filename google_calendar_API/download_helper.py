"""
a Module containing helper functions to
download the events from the Google Calendar API
"""

def download_events(connection, dates:tuple, calendar_id="primary"):
    """Download events into memory from the api"""
    seven_day_calendar = connection.events().list(
        calendarId=calendar_id,
        timeMin = dates[0],
        timeMax = dates[1],
        singleEvents=True,
        orderBy='startTime').execute()

    events = seven_day_calendar.get('items', [])
    return events


def download_multi_events(connection, dates:tuple, calendar_id: str):
    """
    Downloads and aggregates the events of the next 7 days from all the central
    and primary calendar
    """
    primary_events = download_events(connection, dates)
    central_events = download_events(connection, dates, calendar_id)

    all_events = []
    all_ids = []

    for event in primary_events:
        if event['id'] not in all_ids:
            all_events.append(event)
            all_ids.append(event['id'])

    for event in central_events:
        if event['id'] not in all_ids:
            all_events.append(event)
            all_ids.append(event['id'])

    return all_events
