"""
Houses all logic for the second part of
the installation process
"""
from os import system

import inquirer

from installation.calendar_id import get_calendar_id
from output.rich_output import neat_print
from file_helpers.json_helper import load_json_file, overwrite_json_file

def continue_install(storage_path: str):
    """"Continues the program installation"""
    settings_json = {}
    settings_json["STORAGE PATH"] = storage_path
    settings_json["CALENDAR ID"] = get_calendar_id()
    settings_json["PERMISSIONS"] = ['https://www.googleapis.com/auth/calendar']
    settings_json["DATA SAVING FORMAT"] =  get_data_saving_format()
    settings_json["DATA DISPLAY FORMAT"] = get_data_display_format()
    display_all_selected_settings(settings_json)
    install_settings(settings_json)


def get_data_display_format():
    """
    Gets the data displaying format from the user
    """
    neat_print("[bold green]Select Data Display Format[/bold green]")
    neat_print("[bold green]-------------------------------------[/bold green]")
    questions = [
        inquirer.List('data display format',
            message="What data format would you like to use for display data (Rich = Default)?",
            choices=['Rich', 'CSV', 'Tabulate', 'JSON'],
            carousel=True,),
    ]
    answer = inquirer.prompt(questions)["data display format"]
    neat_print(f"[bold green]Selected Data Display Format {answer}[/bold green]")
    neat_print("[bold green]-------------------------------------[/bold green]")
    neat_print("[bold green]PRESS ENTER TO CONTINUE[/bold green]")
    input()
    system("clear")
    return answer


def get_data_saving_format():
    """Gets the data saving format"""
    neat_print("[bold green]Select Data Saving Format[/bold green]")
    neat_print("[bold green]-------------------------------------[/bold green]")
    questions = [
        inquirer.List(
            "data format",
            message="What data format would you like to use for saving data (JSON = Default)?",
            choices=["JSON", "CSV"],
            carousel=True),
    ]
    answer = inquirer.prompt(questions)["data format"]
    neat_print(f"[bold green]Selected Data Saving Format {answer}[/bold green]")
    neat_print("[bold green]-------------------------------------[/bold green]")
    neat_print("[bold green]PRESS ENTER TO CONTINUE[/bold green]")
    input()
    system("clear")
    return answer


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
    data_saving_format = settings_json.get("DATA SAVING FORMAT")
    neat_print(f"[cyan]DATA SAVING FORMAT: [/cyan][magenta]{data_saving_format}[/magenta]")
    data_display_format = settings_json.get("DATA DISPLAY FORMAT")
    neat_print(f"[cyan]DATA DISPLAY FORMAT: [/cyan][magenta]{data_display_format}[/magenta]")
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
