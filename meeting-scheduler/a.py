import datetime

class Person:
    def __init__(self, name):
        self.name = name
        self.meetings = []

    def add_meeting(self, other_person, date):
        self.meetings.append({'with': other_person, 'date': date})

class Scheduler:
    def __init__(self):
        self.meetings = []

    def create_meeting(self, person1, person2, date):
        person1.add_meeting(person2, date)
        person2.add_meeting(person1, date)
        self.meetings.append({'between': [person1, person2], 'date': date})

# Create some Person instances
person1 = Person('Alice')
person2 = Person('Bob')
person3 = Person('Charlie')

# Create a Scheduler instance
scheduler = Scheduler()

# Create some meetings
scheduler.create_meeting(person1, person2, datetime.date(2024, 3, 15))
scheduler.create_meeting(person1, person3, datetime.date(2024, 3, 17))

# Print out all the meetings
for meeting in scheduler.meetings:
    print(f"Meeting between {meeting['between'][0].name} and {meeting['between'][1].name} on {meeting['date']}")

# Print out all the meetings for each person
for person in [person1, person2, person3]:
    print(f"{person.name}'s meetings:")
    for meeting in person.meetings:
        print(f"With {meeting['with'].name} on {meeting['date']}")