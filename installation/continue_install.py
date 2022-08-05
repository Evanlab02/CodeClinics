"""
Houses all logic for the second part of
the installation process
"""

from os import system
from installation.calendar_id import get_calendar_id
from output.my_output import neat_print
from json_files.json_helper import load_json_file, overwrite_json_file

def continue_install(storage_path: str):
    """"Continues the program installation"""
    settings_json = {}
    settings_json["STORAGE PATH"] = storage_path
    settings_json["CALENDAR ID"] = get_calendar_id()
    display_all_selected_settings(settings_json)
    install_settings(settings_json)


def install_settings(settings_json: dict):
    """Installs the settings"""
    neat_print("[bold green]Installing Settings[/bold green]")
    neat_print("[bold green]-------------------------------------[/bold green]")

    storage_directory = settings_json.get("STORAGE PATH")
    settings_path = f"{storage_directory}settings.json"
    neat_print(f"[cyan]SETTINGS PATH: [/cyan][magenta]{settings_path}[/magenta]")

    disk_settings = load_settings_on_disk(settings_path)


    if disk_settings == settings_json:
        neat_print("[bold green]Settings match[/bold green]")
        neat_print("[bold green]Skipping install[/bold green]")
        return

    neat_print("[bold green]Overwriting Settings...[/bold green]")
    overwrite_json_file(settings_path, settings_json)
    neat_print("[bold green]Settings overwritten![/bold green]")
    neat_print("[bold green]-------------------------------------[/bold green]")
    neat_print("[bold green]PRESS ENTER TO CONTINUE[/bold green]")
    input()
    system("clear")


def display_all_selected_settings(settings_json: dict):
    """Displays all selected settings"""
    neat_print("[bold green]Selected Settings[/bold green]")
    neat_print("[bold green]-------------------------------------[/bold green]")
    storage_path = settings_json.get("STORAGE PATH")
    neat_print(f"[cyan]STORAGE PATH: [/cyan][magenta]{storage_path}[/magenta]")
    calendar_id = settings_json.get("CALENDAR ID")
    neat_print(f"[cyan]CALENDAR ID: [/cyan][magenta]{calendar_id}[/magenta]")
    neat_print("[bold green]-------------------------------------[/bold green]")
    neat_print("[bold green]PRESS ENTER TO CONTINUE[/bold green]")
    input()
    system("clear")


def load_settings_on_disk(settings_path: str):
    """Loads the settings on disk"""
    neat_print("[cyan]Loading Settings...[/cyan]")
    disk_settings = load_json_file(settings_path)
    neat_print("[cyan]Settings Loaded![/cyan]")
    neat_print(f"[cyan]DISK SETTINGS: [/cyan][magenta]{disk_settings}[/magenta]")
    return disk_settings
