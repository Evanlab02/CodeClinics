"""
Houses all logic for loading and overwriting csv files.
"""
import csv

from output.my_output import neat_print

def write_csv_file(file_path: str, arrays_of_events: list):
    """
    Writes a csv file with the given arrays of events.
    """
    with open(f'{file_path}', mode='w', encoding="UTF-8") as events_file:
        events_writer = csv.writer(
            events_file,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL
            )

        for event in arrays_of_events:
            events_writer.writerow(event)


def read_csv_file(file_path: str):
    """
    Reads a csv file and returns a dictionary containing arrays of events.
    """
    rows = []
    with open(f'{file_path}', mode='r', encoding="UTF-8") as events_file:
        events_reader = csv.reader(events_file, delimiter=',', quotechar='"')
        headers = next(events_reader)
        for row in events_reader:
            rows.append(row)

    return {
        "headers": headers,
        "rows": rows
    }


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
