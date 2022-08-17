"""
Houses all logic for loading and overwriting csv files.
"""
import csv

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
