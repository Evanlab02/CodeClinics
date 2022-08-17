"""
Houses all logic to check that the credentials file does exist
"""
from installation.file_path_helper import path_exists
from output.rich_output import neat_print

def does_credentials_exist(program_details: dict):
    """Checks that the credentials file exists at the program
    storage directory"""
    input_message = "Please paste the credentials file into the storage "+\
        "directory and press enter to continue..."

    storage_directory = program_details["STORAGE DIRECTORY"]
    file_name = "credentials.json"
    file_path = f"{storage_directory}{file_name}"
    file_exists = path_exists(file_path)

    if not file_exists:
        neat_print("[red]Credentials file not found[/red]")
        input(input_message)
        file_exists = path_exists(file_path)

    return file_exists
