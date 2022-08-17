"""
Houses all the logic for output using tabulate
"""
from tabulate import tabulate
from file_helpers.csv_helper import read_csv_file
from output.rich_output import neat_print

def display_tabulate_events(storage_path: str):
    """
    Displays the events in the console using tabulate
    """
    csv_file_events = read_csv_file(f"{storage_path}events.csv")
    neat_print(tabulate(csv_file_events["rows"], headers=csv_file_events["headers"]))
