"""
Receive settings - Receives settings from user
"""

def receive_settings_from_user():
    """
    Receives settings from user
    """
    settings = {}
    settings["calendar_id"] = receive_calendar_id_from_user()
    return settings


def receive_calendar_id_from_user():
    """
    Receives calendar id from user
    """
    calendar_id = ""
    while calendar_id == "":
        calendar_id = input("Enter your calendar id: ")
        if calendar_id == "":
            print("[red]Calendar id cannot be empty[/red]")
    return calendar_id
