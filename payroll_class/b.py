class Employee:
    def __init__(self, hourly_pay):
        self.hourly_pay = hourly_pay
        self.hours_worked = 0
        self.vacation_days = 0

    def calculate_check(self):
        return self.hourly_pay * self.hours_worked

    def add_hours(self, hours):
        self.hours_worked += hours
        self.vacation_days += hours // 8

    def calculate_taxes(self):
        return self.hourly_pay * self.hours_worked * 0.25


# Testing the class
emp = Employee(20)  # Creating an employee with hourly pay of 20
emp.add_hours(8)  # Adding 8 hours to the employee's hours worked
print(emp.calculate_check())  # Calculating and printing the employee's check
print(emp.vacation_days)  # Printing the employee's accumulated vacation days
print(emp.calculate_taxes())  # Calculating and printing the taxes to be withheld