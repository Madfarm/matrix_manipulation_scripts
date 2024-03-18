class Budget:
    def __init__(self):
        self.expenses = 0
        self.income = 0
        self.investments = 0

    def add_expenses(self, amount):
        self.expenses += amount

    def add_income(self, amount):
        self.income += amount

    def add_investment_growth(self):
        self.investments += self.investments * 0.07

    def get_balance(self):
        return self.income - self.expenses

    def get_investments(self):
        return self.investments


# create a new budget
my_budget = Budget()

# add some expenses
my_budget.add_expenses(100)
my_budget.add_expenses(200)

# add some income
my_budget.add_income(3000)
my_budget.add_income(5000)

# add some investments growth
my_budget.add_investment_growth()

# print the balance
print("Current Balance: ", my_budget.get_balance())

# print the investments
print("Current Investments: ", my_budget.get_investments())