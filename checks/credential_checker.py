"""
Houses all logic to check that the credentials file does exist
"""
from installation.file_path_helper import path_exists
from output.my_output import neat_print

def does_credentials_exist(program_details: dict):
    """Checks that the credentials file exists at the program
    storage directory"""
    storage_directory = program_details["STORAGE DIRECTORY"]
    file_name = "credentials.json"
    file_path = f"{storage_directory}{file_name}"
    file_exists = path_exists(file_path)

    if not file_exists:
        neat_print("[red]Credentials file not found[/red]")

    return file_exists
