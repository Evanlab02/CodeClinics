"""Module responsible for all output"""

from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import print as rprint

# File helpers
from file_helpers.csv_helper import generate_csv_row

def display_basic_table(output: dict):
    """Displays basic table based on dictionary received"""
    console = Console()
    table = Table(show_footer=False)

    table.title = output["title"]

    for index, column in enumerate(output["columns"]):
        table.add_column(column)
        table.columns[index].header_style = "green"
        table.columns[index].style = "yellow"

    for index, row in enumerate(output["rows"]):
        table.add_row(*row)

    console.print(table)


def neat_print(message: str):
    """Prints message using rich print to add extra formatting when required"""
    rprint(message)


def calendar_print(events: list, starting_time="NA"):
    """Displays a table of events based on the events list"""
    header_style = "bold magenta"
    header_enabled = True
    footer_enabled = False
    columns = ["Title", "Date", "Start Time", "End Time", "Description", "Hangout Link"]
    rows = []

    for event in events:
        rows.append(generate_csv_row(event))

    console = Console()
    table = Table(show_header=header_enabled, show_footer=footer_enabled, header_style=header_style)
    table.title = "Calendar Events"

    for column in columns:
        table.add_column(column)

    table.columns[0].header_style = "bold magenta"
    table.columns[0].style = "magenta"
    table.columns[1].header_style = "bold cyan"
    table.columns[1].style = "cyan"
    table.columns[2].header_style = "bold cyan"
    table.columns[2].style = "cyan"
    table.columns[3].header_style = "bold cyan"
    table.columns[3].style = "cyan"
    table.columns[4].header_style = "bold yellow"
    table.columns[4].style = "yellow"
    table.columns[5].header_style = "bold green"
    table.columns[5].style = "green"

    if starting_time != "NA":
        query_time = datetime.now()-starting_time
        table.caption = f"Query Time: {query_time}"

    for row in rows:
        table.add_row(*row)

    console.print(table)
    return table
