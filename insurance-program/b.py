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
        premium = (10000 * age_factor * income_factor * deductible_factor) / 1000
        return premium

# Test the code
person = Person('John Doe', 35, 50000)
insurance = Insurance(person, 500, 'medical', 100000)
print(insurance.premium)