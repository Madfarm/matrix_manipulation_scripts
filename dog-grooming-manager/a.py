class Appointment:
    def __init__(self, name, date, time, price):
        self.name = name
        self.date = date
        self.time = time
        self.price = price

class DogGroomingBusiness:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, name, date, time, price):
        for appointment in self.appointments:
            if date == appointment.date:
                if abs(time - appointment.time) < 60:
                    print("Cannot create appointment within an hour of another")
                    return
        self.appointments.append(Appointment(name, date, time, price))
        self.sort_appointments()

    def delete_appointment(self, name, date, time):
        self.appointments = [appointment for appointment in self.appointments if not (appointment.name == name and appointment.date == date and appointment.time == time)]

    def sort_appointments(self):
        self.appointments.sort(key=lambda x: (x.date, x.time))

    def display_appointments(self):
        for appointment in self.appointments:
            print(f'Dog: {appointment.name}, Date: {appointment.date}, Time: {appointment.time}, Price: {appointment.price}')

business = DogGroomingBusiness()
business.add_appointment('Fido', '2024-03-18', 900, 20)
business.add_appointment('Buddy', '2024-03-18', 1000, 25)
# business.display_appointments()
business.delete_appointment('Fido', '2024-03-18', 900)
business.display_appointments()