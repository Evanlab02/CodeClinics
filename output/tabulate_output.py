"""
Houses all the logic for output using tabulate
"""
from tabulate import tabulate
from csv_files.csv_helper import read_csv_file
from output.my_output import neat_print

def display_tabulate_events(calendar_settings: dict):
    """
    Displays the events in the console using tabulate
    """
    storage_path = calendar_settings['storage path']
    csv_file_events = read_csv_file(f"{storage_path}events.csv")
    neat_print(tabulate(csv_file_events["rows"], headers=csv_file_events["headers"]))
