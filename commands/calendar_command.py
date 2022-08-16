"""
Houses all the logic for the calendar command.
"""
#import statements
import sys

#From Import statements
from datetime import datetime
from api.google_api_helper import get_start_and_end_date, create_api_connection, download_events
from api.token import load_token, check_token
from output.my_output import neat_print
from json_files.json_helper import load_json_file, overwrite_json_file
from csv_files.csv_helper import write_csv_file

def validate_token(creds):
    """
    Validates the token.
    """
    token = check_token(creds)
    if not token:
        neat_print("[yellow]Please login using code_clinic login[/yellow]")
        sys.exit(1)


def get_dates(now: datetime):
    """
    Gets the starting and ending dates of the next 7 days
    """
    neat_print(now)
    today, seven_days = get_start_and_end_date(now)
    neat_print(today)
    neat_print(seven_days)
    return today, seven_days


def download_all_events(calendar_settings: dict):
    """
    Downloads and saves the events of the next 7 days using the Google Calendar API.
    """
    neat_print("[magenta]Downloading events...[/magenta]")
    events = download_events(
        calendar_settings["dates"],
        calendar_settings["connection"],
        calendar_settings["calendar id"]
    )
    neat_print("[green]Events downloaded![/green]")
    calendar_settings.update({"events": events})
    return calendar_settings


def save_json_events(calendar_settings: dict):
    """
    Saves the events on the disk in events.json file
    """
    storage_path = calendar_settings['storage path']
    memory_events = calendar_settings['events']

    try:
        disk_events = load_json_file(f"{storage_path}events.json")
        if disk_events == memory_events:
            neat_print("[green]Events are the same.[/green]")
            neat_print("[green]Skipping saving process.[/green]")
        else:
            overwrite_json_file(f"{storage_path}events.json", memory_events)
            neat_print("[green]Events saved![/green]")
    except FileNotFoundError:
        neat_print("[yellow]Could not find events.json[/yellow]")
        neat_print("[yellow]Creating events.json...[/yellow]")
        overwrite_json_file(f"{storage_path}events.json", memory_events)
        neat_print("[green]events.json created![/green]")
        neat_print("[green]Events saved![/green]")


def save_csv_events(calendar_settings: dict):
    """
    Saves the events on the disk in events.csv file
    """
    storage_path = calendar_settings['storage path']
    memory_events = calendar_settings['events']

    neat_print("[magenta]Converting events to CSV...[/magenta]")
    csv_list = [["ID","Title","Date","Start Time","End Time","Description","Meets Link"]]

    for event in memory_events:
        csv_list.append(generate_csv_row(event))
    neat_print("[green]Converted events to CSV![/green]")

    neat_print("[magenta]Saving events in CSV...[/magenta]")
    write_csv_file(f"{storage_path}events.csv", csv_list)
    neat_print("[green]Events saved in CSV![/green]")


def generate_csv_row(event: dict):
    """
    Generates a row for the events.csv file
    """
    event_id = event['id']
    title = event['summary']
    date = event['start']['dateTime'].split("T")[0]
    start_time = event['start']['dateTime'].split("T")[1].split("+")[0]
    end_time = event['end']['dateTime'].split("T")[1].split("+")[0]

    try:
        description = event["description"]
    except KeyError:
        description = "[No Description]"

    try:
        hangout_link = event["hangoutLink"]
    except KeyError:
        hangout_link = "[No Hangout Link]"

    return [event_id,title,date,start_time,end_time,description,hangout_link]


def save_events(calendar_settings: dict):
    """
    Saves the events on the disk
    """
    neat_print("[magenta]Saving events...[/magenta]")
    data_saving_format = calendar_settings['data saving format']
    save_json_events(calendar_settings)

    if data_saving_format == 'CSV':
        save_csv_events(calendar_settings)


def do_calendar(settings: dict):
    """
    Downloads and prints the events of the next 7 days using the Google Calendar API.
    """
    storage_path = settings['STORAGE PATH']
    calendar_id = settings['CALENDAR ID']
    creds = load_token(settings)
    validate_token(creds)
    connection = create_api_connection(creds)
    dates = get_dates(datetime.now())
    data_saving_format = settings['DATA SAVING FORMAT']
    data_display_format = settings['DATA DISPLAY FORMAT']

    calendar_settings = {
        'storage path': storage_path,
        'calendar id': calendar_id,
        'credentials': creds,
        'connection': connection,
        'dates': dates,
        'data saving format': data_saving_format
    }

    calendar_settings = download_all_events(calendar_settings)
    
    all_events = [event for event in calendar_settings['events']]

    calendar_settings["calendar id"] = "primary"
    calendar_settings = download_all_events(calendar_settings)

    for event in calendar_settings['events']:
        all_events.append(event)

    calendar_settings["events"] = all_events
    save_events(calendar_settings)

    if data_display_format == 'JSON':
        neat_print(all_events)
    else:
        neat_print("[yellow]NO OUTPUT[/yellow]")
