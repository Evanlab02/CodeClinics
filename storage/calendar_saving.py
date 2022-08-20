"""
a Module containing the functions to save the events on the disk
"""

#File Helpers
from file_helpers.csv_helper import write_csv_file, generate_csv_row
from file_helpers.json_helper import load_json_file, overwrite_json_file

def save_events(storage_path:str, events: list):
    """
    Saves the events on the disk
    """
    save_json_events(storage_path, events)
    save_csv_events(storage_path, events)


def save_json_events(storage_path:str, events: list):
    """
    Saves the events on the disk in events.json file
    """
    try:
        disk_events = load_json_file(f"{storage_path}events.json")
        if disk_events != events: # If events are already up to date, do not overwrite
            overwrite_json_file(f"{storage_path}events.json", events)
    except FileNotFoundError:
        overwrite_json_file(f"{storage_path}events.json", events)


def save_csv_events(storage_path:str, events: list):
    """
    Saves the events on the disk in events.csv file
    """
    csv_list = [["ID","Title","Date","Start Time","End Time","Description","Meets Link"]]

    for event in events:
        csv_list.append(generate_csv_row(event))

    write_csv_file(f"{storage_path}events.csv", csv_list)
