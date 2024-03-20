import datetime


def time_travel_path(events, start_date=None, end_date=None):
    # Convert string dates to datetime objects
    for event in events:
        event['date'] = datetime.strptime(event['date'], '%d-%m-%Y')

    # Sort events by date
    events.sort(key=lambda x: x['date'])

    # Filter events by start and end date if provided
    if start_date is not None and end_date is not None:
        start_date = datetime.strptime(start_date, '%d-%m-%Y')
        end_date = datetime.strptime(end_date, '%d-%m-%Y')
        events = [event for event in events if start_date <= event['date'] <= end_date]

    # Print travel itinerary
    for event in events:
        print(f"Date: {event['date'].strftime('%d-%m-%Y')}, Event: {event['name']}, Location: {event['location']}")


# Example usage
events = [
    {'name': 'Event 1', 'date': '01-01-2000', 'location': 'Location 1'},
    {'name': 'Event 2', 'date': '01-01-2001', 'location': 'Location 2'},
    {'name': 'Event 3', 'date': '01-01-2002', 'location': 'Location 3'},
    {'name': 'Event 4', 'date': '01-01-2003', 'location': 'Location 4'},
    {'name': 'Event 5', 'date': '01-01-2004', 'location': 'Location 5'},
]

time_travel_path(events, '01-01-2001', '01-01-2003')