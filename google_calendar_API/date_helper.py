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


def get_rounded_time(given_time:datetime):
    """
    Rounds the given time to the nearest half hour
    """
    time_rounded = given_time
    time_rounded = time_rounded.replace(second=0, microsecond=0, minute=0, hour=time_rounded.hour)
    time_rounded = time_rounded+timedelta(hours=time_rounded.minute//30)
    return time_rounded


def generate_slots_template(today_datetime):
    """
    Generates a template for the slots for the next 7 days
    """
    slots = {}

    for k in range(8):
        day = today_datetime + timedelta(days=k)
        day = day.isoformat()
        day = day.split("T")[0]
        slots[day] = []

    return slots


def populate_template(template: dict, today_rounded: datetime):
    """
    Populates the template with the correct slots
    """
    slots = template.copy()
    template_copy = template.copy()

    for date in template_copy.keys():
        slots = create_day_slots(slots, today_rounded, date)

    return slots


def create_day_slots(slots: dict, today_rounded: datetime, looping_date: str):
    """
    Creates the slots for the given day
    """
    today_date = today_rounded.isoformat().split("T")[0]

    if today_rounded.hour >= 16 and today_date == looping_date:
        del slots[looping_date]
        return slots

    if today_date == looping_date:
        start_datetime = today_rounded + timedelta(minutes=30)
    else:
        start_datetime = today_rounded.replace(second=0, microsecond=0, minute=0, hour=8)

    start_time = start_datetime.isoformat()
    start_time = start_time.split("T")[1]

    time_slots = []

    while start_time != "16:00:00":
        time_slots.append(start_time)
        start_datetime = start_datetime + timedelta(minutes=30)
        start_time = start_datetime.isoformat()
        start_time = start_time.split("T")[1]

    slots[looping_date] = time_slots
    return slots


def generate_event_dates_and_times(events: list):
    """
    Generates the dates and times for the given events
    """
    event_data = []

    for event in events:
        event_datetime = event['start'].get('dateTime', event['start'].get('date'))
        event_date = event_datetime.split("T")[0]
        event_time = event_datetime.split("T")[1].split("+")[0]
        event_data.append([event_date, event_time])

    return event_data


def generate_available_slots(events: list, selected_day: str, selected_day_slots: list):
    """
    Generates the available slots for the given day
    """
    event_data = generate_event_dates_and_times(events)
    available_slots = selected_day_slots.copy()

    for event in event_data:
        if event[0] == selected_day:
            available_slots.remove(event[1])

    return available_slots


def generate_new_event_start_and_finish_time(selected_day: str, selected_slot: str):
    """
    Generates the new start and finish time for the event
    """
    selected_datetime = f"{selected_day} {selected_slot}"
    selected_datetime = datetime.strptime(selected_datetime, "%Y-%m-%d %H:%M:%S")
    selected_datetime = selected_datetime - timedelta(hours=2)

    start = selected_datetime.isoformat() + "Z"
    end = (selected_datetime + timedelta(minutes=30)).isoformat() + "Z"
    return start, end
