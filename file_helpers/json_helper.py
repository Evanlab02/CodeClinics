"""
json helper - Houses logic for loading and overwriting json files.
"""

import json

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
