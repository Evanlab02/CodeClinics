"""Contains all logic for creating the storage directory"""

from output.rich_output import display_basic_table
from installation.file_path_helper import (get_home_directory,
    get_storage_directory,
    path_exists,
    create_directory)

def start_directory_installation(installation_details: dict):
    """Installs the storage directory if it does not exist on this device"""
    installation_details["HOME"] = get_home_directory()
    installation_details["STORAGE DIRECTORY"] = get_storage_directory(installation_details["HOME"])
    installation_details["EXISTS"] = path_exists(installation_details["STORAGE DIRECTORY"])

    if installation_details["EXISTS"]:
        installation_details["INSTALLED"] = False
    else:
        create_directory(installation_details["STORAGE DIRECTORY"])
        installation_details["INSTALLED"] = True

    output = {}
    output["title"] = "Directory Installation"
    output["columns"] = ["Key", "Value"]
    output["rows"] = [
        ["Home", installation_details["HOME"]],
        ["Storage Directory", installation_details["STORAGE DIRECTORY"]],
        ["Directory already exists", str(installation_details["EXISTS"])],
        ["Installed Directory", str(installation_details["INSTALLED"])]
    ]

    display_basic_table(output)
    