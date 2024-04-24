import numpy as np
from decimal import Decimal


# Initialize account balances with 0.00
account_balances = np.array([Decimal(0.00), Decimal('0.00'), Decimal('0.00')])


def deposit(account_id, amount):
    global account_balances
    account_balances[account_id] += amount


def withdraw(account_id, amount):
    global account_balances
    if account_balances[account_id] >= amount:
        account_balances[account_id] -= amount
    else:
        print("Insufficient funds")


def calculate_total_balance():
    return np.sum(account_balances)


# Demonstration
withdraw(0, Decimal('231.45'))
print(account_balances[0] - 231.45)
assert account_balances[0] == Decimal('-231.45')
deposit(0, Decimal('12.45'))
assert account_balances[0] == Decimal('-219.00')
deposit(0, Decimal('65.00'))
assert account_balances[0] == Decimal('-154.00')
withdraw(0, Decimal('100.00'))
assert account_balances[0] == Decimal('-254.00')
withdraw(0, Decimal('50.00'))
assert account_balances[0] == Decimal('-304.00')
deposit(0, Decimal('543.98'))
assert account_balances[0] == Decimal('239.98')


print("Final balance:", calculate_total_balance())
assert calculate_total_balance() == Decimal('239.98')