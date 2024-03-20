def time_travel_path(events, start_date, end_date):
    # Check for valid start and end dates
    if start_date > end_date:
        return "Start date cannot be later than end date."

    # Create a list to store events within the given time frame
    time_frame_events = []

    # Go through each event
    for event in events:
        # Parse the date from the string
        event_date = event['date']

        # Check if the event is within the given time frame
        if start_date <= event_date <= end_date:
            time_frame_events.append(event)

    # Sort the events in chronological order
    time_frame_events.sort(key=lambda x: x['date'])

    # Create the travel itinerary
    itinerary = []
    for event in time_frame_events:
        itinerary.append({'event': event['name'], 'location': event['location'], 'date': event['date']})

    return itinerary

# Test the function
events = [
    {'name': 'The Battle of Gettysburg', 'date': '1863-07-01', 'location': 'Gettysburg, Pennsylvania'},
    {'name': 'The First Manned Spaceflight', 'date': '1961-04-12', 'location': 'Baikonur Cosmodrome, Kazakhstan'},
    {'name': 'The Fall of the Berlin Wall', 'date': '1989-11-09', 'location': 'Berlin, Germany'},
    {'name': 'The First Transatlantic Flight', 'date': '1910-06-14', 'location': 'Baddeck, Nova Scotia, Canada'},
    {'name': 'The First Powered Airplane Flight', 'date': '1903-12-17', 'location': 'Kitty Hawk, North Carolina, USA'},
    {'name': 'The First Telephone Call', 'date': '1876-03-10', 'location': 'New Haven, Connecticut, USA'},
]

# Set start and end dates
start_date = '1900-01-01'
end_date = '2000-01-01'

# Print the travel itinerary
itinerary = time_travel_path(events, start_date, end_date)
for event in itinerary:
    print(f"Event: {event['event']}")
    print(f"Location: {event['location']}")
    print(f"Date: {event['date']}")
    print()