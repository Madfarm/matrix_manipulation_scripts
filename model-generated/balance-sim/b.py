import numpy as np
from decimal import Decimal, getcontext


# Set the precision for Decimal
getcontext().prec = 6


# Initial account balances
account_balances = np.array([Decimal('1000.00'), Decimal('2000.00'), Decimal('3000.00')])


def deposit(account_id, amount):
    global account_balances
    account_balances[account_id] += Decimal(amount)


def withdraw(account_id, amount):
    global account_balances
    if account_balances[account_id] >= Decimal(amount):
        account_balances[account_id] -= Decimal(amount)
    else:
        print("Insufficient funds")


def calculate_total_balance():
    return np.sum(account_balances)


# Test the functions
withdraw(0, '231.45')
assert account_balances[0] == Decimal('768.55')


deposit(1, '12.45')
assert account_balances[1] == Decimal('2012.45')


deposit(2, '65.00')
assert account_balances[2] == Decimal('3065.00')


withdraw(0, '100.00')
assert account_balances[0] == Decimal('668.55')


withdraw(0, '50.00')
assert account_balances[0] == Decimal('618.55')


deposit(0, '543.98')
assert account_balances[0] == Decimal('1162.53')


# Check the final total balance
assert calculate_total_balance() == Decimal('6239.98')