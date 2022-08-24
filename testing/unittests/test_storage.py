"""
Tests the storage module
"""


#Testing
import unittest
from unittest.mock import patch
from io import StringIO

#File Helpers
from file_helpers.json_helper import load_json_file
from file_helpers.csv_helper import read_csv_file


#Storage
from storage.calendar_saving import save_json_events, save_csv_events, save_events


class MyTestCase(unittest.TestCase):
    """
    Just a class to contain tests
    """

    @patch("sys.stdout", StringIO())
    def test_save_json_events(self):
        """
        Tests the save_json_events function
        """
        events = [
            {
                "id": "1",
                "summary": "Event 1",
                "start": {
                    "dateTime": "2019-01-01T00:00:00+00:00"
                },
                "end": {
                    "dateTime": "2019-01-01T00:00:00+00:00"
                }
            },
            {
                "id": "2",
                "summary": "Event 2",
                "start": {
                    "dateTime": "2019-01-01T00:00:00+00:00"
                },
                "end": {
                    "dateTime": "2019-01-01T00:00:00+00:00"
                }
            }
        ]

        save_json_events("testing/unittests/resources/", events)
        self.assertEqual(load_json_file("testing/unittests/resources/events.json"), events)

        save_json_events("testing/unittests/resources/", {})
        self.assertEqual(load_json_file("testing/unittests/resources/events.json"), {})


    @patch("sys.stdout", StringIO())
    def test_save_csv_events(self):
        """
        Tests the save_json_events function
        """
        events = [
            {
                "id": 1,
                "summary":
                "Event 1",
                "start": {
                    "dateTime": "2022-08-19T13:00:00+02:00"
                },
                "end": {
                    "dateTime": "2022-08-19T14:00:00+02:00"
                },
                "description":"This is a tester event",
                "hangoutLink": "https://meet.google.com/abc"
            }
        ]

        save_csv_events("testing/unittests/resources/", events)
        csv_list = read_csv_file("testing/unittests/resources/events.csv")
        expected_list = {
            "headers": ["Title","Date","Start Time","End Time","Description","Meets Link"],
            "rows": [
                [
                    "Event 1",
                    "2022-08-19",
                    "13:00:00",
                    "14:00:00",
                    "This is a tester event",
                    "https://meet.google.com/abc"
                ]
            ]
        }
        self.assertEqual(csv_list, expected_list)
        save_csv_events("testing/unittests/resources/", [])
        csv_list = read_csv_file("testing/unittests/resources/events.csv")
        expected_list = {
            "headers": ["Title","Date","Start Time","End Time","Description","Meets Link"],
            "rows": []
        }
        self.assertEqual(csv_list, expected_list)


    @patch("sys.stdout", StringIO())
    def test_save_events(self):
        """
        Tests the save_events function
        """
        events = [
            {
                "id": 1,
                "summary":
                "Event 1",
                "start": {
                    "dateTime": "2022-08-19T13:00:00+02:00"
                },
                "end": {
                    "dateTime": "2022-08-19T14:00:00+02:00"
                },
                "description":"This is a tester event",
                "hangoutLink": "https://meet.google.com/abc"
            }
        ]

        save_events("testing/unittests/resources/", events)

        self.assertEqual(load_json_file("testing/unittests/resources/events.json"), events)
        csv_list = read_csv_file("testing/unittests/resources/events.csv")
        expected_list = {
            "headers": ["Title","Date","Start Time","End Time","Description","Meets Link"],
            "rows": [
                [
                    "Event 1",
                    "2022-08-19",
                    "13:00:00",
                    "14:00:00",
                    "This is a tester event",
                    "https://meet.google.com/abc"
                ]
            ]
        }
        self.assertEqual(csv_list, expected_list)


        save_events("testing/unittests/resources/", {})
        self.assertEqual(load_json_file("testing/unittests/resources/events.json"), {})

        csv_list = read_csv_file("testing/unittests/resources/events.csv")
        expected_list = {
            "headers": ["Title","Date","Start Time","End Time","Description","Meets Link"],
            "rows": []
        }
        self.assertEqual(csv_list, expected_list)
