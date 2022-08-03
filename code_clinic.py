"""
code_clinic.py
This module is the main entry module for the code_clinic program.
It will get the command and its arguments (that were passed) in using
sys.argv and then send it to be processed.
"""
# From Import Statements
from cli.cli_typer import start_typer


def main():
    """Main function of the code_clinic program"""
    start_typer()


if __name__ == "__main__":
    main()
