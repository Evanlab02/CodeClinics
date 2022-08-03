"""Contains all the logic for installing the settings file"""

from installation.file_path_helper import path_exists
from output.my_output import neat_print

def install_settings(installation_resources: dict):
    """Installs the settings file if it does not exist on this device"""
    storage_directory = installation_resources.get('STORAGE DIRECTORY')
    file_name = "settings.json"
    file_path = storage_directory + file_name

    if not path_exists(file_path):
        neat_print("[green]Installing Settings File[/green]")
        with open(file_path, 'w', encoding="UTF-8") as settings_file:
            settings_file.write("{}")
        neat_print("[green]Settings File Installed[/green]")
    else:
        neat_print("[green]Settings file already exists[/green]")
