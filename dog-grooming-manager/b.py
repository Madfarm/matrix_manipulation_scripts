class Appointment:
    def __init__(self, dog_name, date, time, price):
        self.dog_name = dog_name
        self.date = date
        self.time = time
        self.price = price

    def __str__(self):
        return f'{self.dog_name} - {self.date} - {self.time} - ${self.price}'

class DogGroomingBusiness:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, appointment):
        for existing_appointment in self.appointments:
            if (appointment.date == existing_appointment.date and
                abs(appointment.time - existing_appointment.time) < 60):
                print('Appointment is within an hour of another appointment.')
                return
        self.appointments.append(appointment)
        print('Appointment added.')

    def delete_appointment(self, dog_name, date, time):
        for appointment in self.appointments:
            if (appointment.dog_name == dog_name and
                appointment.date == date and
                appointment.time == time):
                self.appointments.remove(appointment)
                print('Appointment deleted.')
                return
        print('Appointment not found.')

    def sort_appointments(self):
        self.appointments.sort(key=lambda x: (x.date, x.time))

    def display_appointments(self):
        for appointment in self.appointments:
            print(appointment)

# Test the program
business = DogGroomingBusiness()

# Add appointments
business.add_appointment(Appointment('Fido', '2022-01-01', 900, 20))
business.add_appointment(Appointment('Buddy', '2022-01-01', 1000, 30))
business.add_appointment(Appointment('Max', '2022-01-01', 400, 40))

# Display appointments
business.display_appointments()

# Sort appointments
business.sort_appointments()

# Display sorted appointments
business.display_appointments()

# Delete appointment
business.delete_appointment('Buddy', '2022-01-01', 1000)

# Display appointments after deletion
business.display_appointments()