class CreditCard:
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

# create a credit card object
card = CreditCard(15, 5000, 2)

# calculate and print the interest
interest = card.calculate_interest()
print("Interest: $", interest)

# calculate and print the minimum payment
min_payment = card.calculate_min_payment()
print("Minimum Payment: $", min_payment)