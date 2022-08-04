import json

from output.my_output import neat_print

def load_json_file(file_path:str):
    """
    Loads a json file and returns the json object.
    """
    json_object = None
    try:
        with open(file_path, 'r', encoding="UTF-8") as f:
            json_object = json.load(f)
    except FileNotFoundError as exception:
        raise exception
    return json_object


def overwrite_json_file(file_path:str, new_value):
    """
    Overwrites a json file with the new value.
    """
    if type(new_value) != dict and type(new_value) != list:
        raise TypeError("new_value must be a dictionary or list")

    try:
        with open(file_path, 'w', encoding="UTF-8") as f:
            json.dump(new_value, f, indent=4)
    except FileNotFoundError as exception:
        raise exception
