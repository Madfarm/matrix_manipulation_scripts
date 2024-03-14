class CreditCardAccount:
    def __init__(self, apr, balance, min_payment_percent):
        self.apr = apr
        self.balance = balance
        self.min_payment_percent = min_payment_percent

    def calculate_interest(self):
        interest = (self.apr / 100) * self.balance
        return interest

    def calculate_min_payment(self):
        min_payment = (self.min_payment_percent / 100) * self.balance
        return min_payment

# create a new credit card account
account = CreditCardAccount(15, 5000, 2)

# calculate and print the interest
interest = account.calculate_interest()
print(f"The interest is: {interest}")

# calculate and print the minimum payment
min_payment = account.calculate_min_payment()
print(f"The minimum payment is: {min_payment}")