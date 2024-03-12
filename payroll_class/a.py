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

    def calculate_tax(self):
        return self.calculate_check() * 0.25


# Create an employee with a hourly pay of $20
employee = Employee(20)

# Add 40 hours of work
employee.add_hours(40)

# Calculate the check
check = employee.calculate_check()
print("Check: $", check)

# Calculate the tax
tax = employee.calculate_tax()
print("Tax: $", tax)

print(employee.vacation_days)