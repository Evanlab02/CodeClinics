from rich.console import Console
from rich.table import Table

def display_installation(output: dict):
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
