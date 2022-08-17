"""
Houses all the logic for output using csv
"""
from output.rich_output import neat_print
from file_helpers.csv_helper import read_csv_file

def display_csv_events(storage_path: str):
    """
    Displays the events in the console
    """
    csv_file_events = read_csv_file(f"{storage_path}events.csv")
    output = ""

    for header in csv_file_events["headers"]:
        if header == csv_file_events["headers"][-1]:
            output+=f"{header}\n"
        else:
            output+=f"{header},"

    for row in csv_file_events["rows"]:
        for field in row:
            if field == row[-1]:
                output+=f"{field}\n"
            else:
                output+=f"{field},"

    neat_print(output)
