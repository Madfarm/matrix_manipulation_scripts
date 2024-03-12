import datetime

class Person:
    def __init__(self, name):
        self.name = name
        self.meetings = []

    def __str__(self):
        return self.name

    def add_meeting(self, other_person, date):
        self.meetings.append((other_person, date))
        other_person.meetings.append((self, date))

class Scheduler:
    def __init__(self):
        self.meetings = []

    def create_meeting(self, person1, person2, date):
        if not isinstance(date, datetime.date):
            raise ValueError("Date must be a datetime.date object")
        person1.add_meeting(person2, date)
        person2.add_meeting(person1, date)
        self.meetings.append((person1, person2, date))

# Create some Person instances
p1 = Person("Alice")
p2 = Person("Bob")
p3 = Person("Charlie")

# Create a Scheduler instance
scheduler = Scheduler()

# Create some meetings
scheduler.create_meeting(p1, p2, datetime.date(2022, 1, 1))
scheduler.create_meeting(p2, p3, datetime.date(2022, 2, 1))
scheduler.create_meeting(p1, p3, datetime.date(2022, 3, 1))

# Print all meetings
for meeting in scheduler.meetings:
    print(f"Meeting between {meeting[0]} and {meeting[1]} on {meeting[2]}")

# Print all meetings for each person
for person in [p1, p2, p3]:
    print(f"{person}'s meetings:")
    for meeting in person.meetings:
        print(f"Meeting with {meeting[0]} on {meeting[1]}")