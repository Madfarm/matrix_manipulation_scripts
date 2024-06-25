import datetime

class Event:
    def __init__(self, id, name, date):
        self.id = id
        self.name = name
        self.date = date

class Calendar:
    def __init__(self):
        self.events = []

    def create_event(self, id, name, date):
        self.events.append(Event(id, name, date))

    def read_event(self, id):
        for event in self.events:
            if event.id == id:
                return event
        return None

    def update_event(self, id, name, date):
        for event in self.events:
            if event.id == id:
                event.name = name
                event.date = date
                return True
        return False

    def delete_event(self, id):
        for event in self.events:
            if event.id == id:
                self.events.remove(event)
                return True
        return False

    def get_all_events(self):
        return self.events

def use_calendar(action=None, *args):
    
    if action == "CREATE":
        id, name, date = args
        calendar.create_event(id, name, date)
    elif action == "READ":
        id = args[0]
        event = calendar.read_event(id)
        if event:
            return event.name, event.date
        else:
            return "Event not found"
    elif action == "UPDATE":
        id, name, date = args
        if calendar.update_event(id, name, date):
            return "Event updated successfully"
        else:
            return "Event not found"
    elif action == "DELETE":
        id = args[0]
        if calendar.delete_event(id):
            return "Event deleted successfully"
        else:
            return "Event not found"
    else:
        # No action passed, return all future events
        events = calendar.get_all_events()
        future_events = [event for event in events if event.date > datetime.datetime.now()]
        future_events.sort(key=lambda x: x.date)
        return [(event.name, event.date) for event in future_events]

# Example usage
calendar = Calendar()
print(use_calendar("CREATE", 1, "May-Retta Daze", datetime.datetime(2024, 5, 1)))

# print(use_calendar("CREATE", 2, "Central Park Swedish Event", datetime.datetime(2024, 7, 11)))
# print(use_calendar("CREATE", 3, "Eddie Montgomery's Woodstock Concert", datetime.datetime(2024, 8, 15)))
# print(use_calendar("CREATE", 4, "Miami Event 1", datetime.datetime(2024, 3, 20)))
# print(use_calendar("CREATE", 5, "Miami Event 2", datetime.datetime(2024, 6, 25)))

# print(use_calendar("READ", 1))
# print(use_calendar("READ", 2))
# print(use_calendar("READ", 3))

# print(use_calendar("UPDATE", 1, "New Name", datetime.datetime(2024, 5, 10)))
# print(use_calendar("UPDATE", 2, "New Name", datetime.datetime(2024, 7, 12)))

# print(use_calendar("DELETE", 3))

print(use_calendar())