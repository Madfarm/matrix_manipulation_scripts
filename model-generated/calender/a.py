class Calendar:
    def __init__(self):
        self.events = {}


    def add_event(self, date, start_time, end_time, description):
        if date in self.events:
            for event in self.events[date]:
                if (start_time < event[1] and end_time > event[0]) or (start_time < event[1] and start_time >= event[0]) or (end_time > event[0] and end_time < event[1]):
                    print("This event overlaps with another event.")
                    return
        if date not in self.events:
            self.events[date] = []
        self.events[date].append((start_time, end_time, description))


    def delete_event(self, date, description):
        if date in self.events:
            self.events[date] = [event for event in self.events[date] if event[2] != description]


    def edit_event(self, date, old_description, new_description):
        if date in self.events:
            for event in self.events[date]:
                if event[2] == old_description:
                    event[2] = new_description


    def display_events(self, date):
        if date in self.events:
            for event in self.events[date]:
                print(f"From {event[0]} to {event[1]}: {event[2]}")
        else:
            print("No events on this date.")


# Demonstration
calendar = Calendar()
calendar.add_event("2024-03-28", "10:00", "11:00", "Meeting")
calendar.add_event("2024-03-28", "10:30", "11:30", "Lunch")
calendar.add_event("2024-03-28", "11:00", "12:00", "Meeting")  # This event overlaps with the first one
calendar.display_events("2024-03-28")
calendar.delete_event("2024-03-28", "Meeting")
calendar.edit_event("2024-03-28", "Lunch", "Dinner")
calendar.display_events("2024-03-28")