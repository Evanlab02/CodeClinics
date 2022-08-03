"""Houses all logic to check that all installation checks pass"""

from checks.credential_checker import does_credentials_exist

def run_checks(program_details: dict):
    """Runs all checks and returns a list of all failed checks"""
    program_details.update({"CREDENTIALS EXIST": does_credentials_exist(program_details)})

    failed_checks = [
        program_details.get(key)
        for key in program_details
        if program_details.get(key) is False and
        key != "INSTALLED" and
        key != "EXISTS"
    ]

    return failed_checks
