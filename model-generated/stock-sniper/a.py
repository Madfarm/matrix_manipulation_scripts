import random

class Stock:
    def __init__(self, symbol, name, opening_price):
        self.symbol = symbol
        self.name = name
        self.opening_price = opening_price
        self.low_price = opening_price
        self.high_price = opening_price
        self.closing_price = opening_price

    def update_prices(self):
        # Generate random price changes between -5 and 5
        change = random.randint(-5, 5) / 100
        self.low_price = min(self.low_price, self.closing_price * (1 + change))
        self.high_price = max(self.high_price, self.closing_price * (1 + change))
        self.closing_price *= (1 + change)

    def calculate_return(self):
        return ((self.closing_price - self.opening_price) / self.opening_price) * 100

class Trader:
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital
        self.portfolio = {}

    def buy_stock(self, stock, quantity):
        if self.capital >= stock.closing_price * quantity:
            self.capital -= stock.closing_price * quantity
            if stock in self.portfolio:
                self.portfolio[stock] += quantity
            else:
                self.portfolio[stock] = quantity

    def sell_stock(self, stock, quantity):
        if stock in self.portfolio and self.portfolio[stock] >= quantity:
            self.capital += stock.closing_price * quantity
            self.portfolio[stock] -= quantity
            if self.portfolio[stock] == 0:
                del self.portfolio[stock]

# Create stocks
stocks = [Stock("AAPL", "Apple", 150), Stock("GOOG", "Google", 2000), Stock("TSLA", "Tesla", 500)]

# Create traders
traders = [Trader("John", 10000), Trader("Jane", 10000), Trader("Bob", 10000)]

# Simulate a day of trading
for _ in range(10):
    for stock in stocks:
        stock.update_prices()
        for trader in traders:
            if random.choice([True, False]):
                trader.buy_stock(stock, random.randint(1, 100))
            else:
                trader.sell_stock(stock, random.randint(1, 100))

# Print results
for trader in traders:
    print(f"{trader.name} has a capital of {trader.capital}")