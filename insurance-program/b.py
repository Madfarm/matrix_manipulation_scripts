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
        age_factor = 1 + (self.person.age // 10) * 0.1
        income_factor = 1 + (self.person.income // 10000) * 0.05
        deductible_factor = 1 + (self.deductible // 1000) * 0.02
        premium = (1000 * age_factor * income_factor * deductible_factor) / 1000
        return premium

# create a person
person = Person("John Doe", 30, 50000)

# create an insurance policy for the person
insurance = Insurance(person, 500, "health", 100000)

# print the person's details
print(f"Person: {person.name}, Age: {person.age}, Income: {person.income}")

# print the insurance policy details
print(f"Type: {insurance.type}, Premium: {insurance.premium}, Deductible: {insurance.deductible}, Limit: {insurance.limit}")