"""
json helper - Houses logic for loading and overwriting json files.
"""

import json

from output.my_output import neat_print

def load_json_file(file_path:str):
    """
    Loads a json file and returns the json object.
    """
    json_object = None
    try:
        with open(file_path, 'r', encoding="UTF-8") as read_file:
            json_object = json.load(read_file)
    except FileNotFoundError as exception:
        raise exception
    return json_object


def overwrite_json_file(file_path:str, new_value):
    """
    Overwrites a json file with the new value.
    """

    if not isinstance(new_value, dict) and not isinstance(new_value, list):
        raise TypeError("new_value must be a dictionary or list")

    try:
        with open(file_path, 'w', encoding="UTF-8") as write_file:
            json.dump(new_value, write_file, indent=4)
    except FileNotFoundError as exception:
        raise exception


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
