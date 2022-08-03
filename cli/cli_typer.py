"""
CLI Typer
The file responsible for all CLI commands using typer
"""

# Import Statements
import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    """
    Hello Command - Displays a welcome message to user
    """
    print(f"Hello {name}, welcome to Code Clinics")


@app.command()
def hello_world():
    """
    Hello World Command - Displays a welcome message to the world
    """
    print("Hello world, welcome to Code Clinics")


def start_typer():
    """Starts the app"""
    app()
