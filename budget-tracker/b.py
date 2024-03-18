class BudgetTracker:
    def __init__(self):
        self.expenses = 0
        self.income = 0
        self.investments = 0

    def add_expense(self, amount):
        self.expenses += amount

    def add_income(self, amount):
        self.income += amount

    def add_investment_growth(self):
        self.investments += self.investments * 0.07

# Create a new budget tracker
tracker = BudgetTracker()
tracker.investments = 855

# Add some expenses
tracker.add_expense(1000)
tracker.add_expense(200)

# Add some income
tracker.add_income(3000)
tracker.add_income(1000)

# Add growth to investments
tracker.add_investment_growth()

# Print the results
print(f'Expenses: {tracker.expenses}')
print(f'Income: {tracker.income}')
print(f'Investments: {tracker.investments}')