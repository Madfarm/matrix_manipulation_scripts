class Person:
    def __init__(self, name, age, income):
        self.name = name
        self.age = age
        self.income = income

class Insurance:
    def __init__(self, person, deductible, type, limit):
        self.person = person
        self.deductible = deductible
        self.type = type
        self.limit = limit
        self.premium = self.calculate_premium()

    def calculate_premium(self):
        age_factor = 1
        if self.person.age < 25:
            age_factor = 1.2
        elif self.person.age < 30:
            age_factor = 1.1
        elif self.person.age < 35:
            age_factor = 1.0
        else:
            age_factor = 0.9

        income_factor = 1
        if self.person.income < 50000:
            income_factor = 1.2
        elif self.person.income < 75000:
            income_factor = 1.1
        elif self.person.income < 100000:
            income_factor = 1.0
        else:
            income_factor = 0.9

        premium = (self.person.income * income_factor) + (self.person.age * age_factor)
        return premium

# Create a person and an insurance
person = Person("John Doe", 35, 75000)
insurance = Insurance(person, 500, "Health", 100000)

# Print the person's details
print("Person's Details:")
print("Name:", person.name)
print("Age:", person.age)
print("Income:", person.income)

# Print the insurance details
print("\nInsurance Details:")
print("Deductible:", insurance.deductible)
print("Type:", insurance.type)
print("Limit:", insurance.limit)
print("Premium:", insurance.premium)