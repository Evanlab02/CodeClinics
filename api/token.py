"""
Houses all logic in regards to the token.json file
"""
import sys
from os import system
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from output.my_output import neat_print
from installation.file_path_helper import path_exists

def create_token(settings: dict):
    """Creates a token (token.json) using oauth to login
    a user in with their gmail account, it will use the storage
    directory to find the client_secret(credentials.json) and the permission
    to determine what permissions the user should have, when the user
    goes through the oauth process, it will create a token.json
    meaning the user is signed in"""
    storage_directory = settings["STORAGE PATH"]
    permission = settings["PERMISSIONS"]

    flow = InstalledAppFlow.from_client_secrets_file(
        f'{storage_directory}credentials.json', permission)

    creds = flow.run_local_server(port=0)

    neat_print(f"[magenta]Writing token at {storage_directory}token.json...[/magenta]")
    with open(f'{storage_directory}token.json', 'w', encoding="utf-8") as token:
        token.write(creds.to_json())
    neat_print("[green]Token created![/green]")


def load_token(settings: dict):
    """
    Will load the token off of the token.json file, if
    there is nothing to load, it will return None
    """
    storage_directory = settings["STORAGE PATH"]
    permission = settings["PERMISSIONS"]
    creds = None
    if path_exists(f'{storage_directory}token.json'):
        creds = Credentials.from_authorized_user_file(f'{storage_directory}token.json', permission)
    return creds


def token_valid(creds):
    """
    Checks that the token exists and is valid
    """
    return creds and creds.valid


def token_expired(creds):
    """
    Checks that the token exists and is expired or needs to be refreshed
    """
    return creds and creds.expired and creds.refresh_token


def check_token(creds):
    """
    Checks that the token is valid and not expired, if it
    meets both these conditions will return True, otherwise False
    """
    return token_valid(creds) and not token_expired(creds)


def remove_token(storage_directory: str):
    """Will delete the token.json at the storage directory"""
    token_exists = False
    if path_exists(f"{storage_directory}token.json"):
        system(f"rm {storage_directory}token.json")
        token_exists = True
    return token_exists


def validate_token(creds):
    """
    Validates the token.
    """
    token = check_token(creds)
    if not token:
        neat_print("[yellow]Please login using code_clinic login[/yellow]")
        sys.exit(1)
