"""
Houses all logic in regards to the token.json file
"""

from google_auth_oauthlib.flow import InstalledAppFlow
from output.my_output import neat_print

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
