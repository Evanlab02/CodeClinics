import csv

def write_csv_file(file_path: str, arrays_of_events: list):
    with open(f'{file_path}', mode='w') as events_file:
        events_writer = csv.writer(events_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for event in arrays_of_events:
            events_writer.writerow(event)
    
    