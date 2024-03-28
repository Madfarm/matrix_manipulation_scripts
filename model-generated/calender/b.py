class Calendar:
    def __init__(self):
        self.events = {}


    def add_event(self, date, start_time, end_time, description):
        if date not in self.events:
            self.events[date] = []


        for event in self.events[date]:
            if start_time < event[1] and end_time > event[0]:
                return "Overlapping event already exists on this date."


        self.events[date].append((start_time, end_time, description))
        self.events[date].sort()


    def delete_event(self, date, event_index):
        del self.events[date][event_index]


    def edit_event(self, date, event_index, description):
        self.events[date][event_index] = (self.events[date][event_index][0], self.events[date][event_index][1], description)


    def display_events(self, date):
        if date not in self.events:
            return "No events on this date."
        else:
            for i, event in enumerate(self.events[date]):
                print(f"Event {i}: {event[0]} - {event[1]}, {event[2]}")


# Demonstration
calendar = Calendar()
calendar.add_event("2024-03-28", "10:00", "12:00", "Meeting")
calendar.add_event("2024-03-28", "13:00", "15:00", "Lunch")
calendar.add_event("2024-03-28", "11:00", "13:00", "Email")
calendar.display_events("2024-03-28")
calendar.delete_event("2024-03-28", 2)
calendar.display_events("2024-03-28")
calendar.edit_event("2024-03-28", 1, "Dinner")
calendar.display_events("2024-03-28")