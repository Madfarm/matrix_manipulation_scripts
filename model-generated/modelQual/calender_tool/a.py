import datetime

class Event:
    def __init__(self, id, name, date):
        self.id = id
        self.name = name
        self.date = date

    def __repr__(self):
        return f"Id: {self.id}\nName: {self.name}\nDate: {self.date}\n "

class Calendar:
    def __init__(self):
        self.events = []

    def create_event(self, name, date):
        id = len(self.events) + 1
        event = Event(id, name, date)
        self.events.append(event)
        return event

    def read_event(self, id):
        for event in self.events:
            if event.id == id:
                return event
        return None

    def update_event(self, id, name, date):
        event = self.read_event(id)
        if event:
            event.name = name
            event.date = date
            return event
        return None

    def delete_event(self, id):
        event = self.read_event(id)
        if event:
            self.events.remove(event)
            return event
        return None

    def get_future_events(self):
        current_date = datetime.datetime.now()
        future_events = [event for event in self.events if event.date > current_date]
        future_events.sort(key=lambda x: x.date)
        return future_events

def use_calendar(action=None, *args):
    if action == "CREATE":
        name, date = args
        event = calendar.create_event(name, date)
        return event
    elif action == "READ":
        id = args[0]
        event = calendar.read_event(id)
        return event
    elif action == "UPDATE":
        id, name, date = args
        event = calendar.update_event(id, name, date)
        return event
    elif action == "DELETE":
        id = args[0]
        event = calendar.delete_event(id)
        return event
    else:
        future_events = calendar.get_future_events()
        return future_events

# Example usage
# Create events
calendar = Calendar()
use_calendar("CREATE", "May-Retta Daze", datetime.datetime(2024, 5, 1))
use_calendar("CREATE", "Central Park Swedish Event", datetime.datetime(2024, 7, 11))
use_calendar("CREATE", "Eddie Montgomery's Woodstock Concert", datetime.datetime(2024, 8, 15))
use_calendar("CREATE", "Miami Event 1", datetime.datetime(2024, 3, 20))
use_calendar("CREATE", "Miami Event 2", datetime.datetime(2024, 4, 10))

# Read events
print(use_calendar("READ", 1))  # Output: Event(id=1, name='May-Retta Daze', date=datetime.datetime(2024, 5, 1, 0, 0))
print(use_calendar("READ", 2))  # Output: Event(id=2, name='Central Park Swedish Event', date=datetime.datetime(2024, 7, 11, 0, 0))

# Update events
use_calendar("UPDATE", 1, "May-Retta Daze 2024", datetime.datetime(2024, 5, 2))
print(use_calendar("READ", 1))  # Output: Event(id=1, name='May-Retta Daze 2024', date=datetime.datetime(2024, 5, 2, 0, 0))

# Delete events
use_calendar("DELETE", 2)
print(use_calendar("READ", 2))  # Output: None

# Get future events
future_events = use_calendar()
for event in future_events:
    print(event)