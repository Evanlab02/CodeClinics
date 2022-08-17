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
