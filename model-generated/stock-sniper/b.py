class Stock:
    def __init__(self, symbol, name, opening_price, low_price, high_price, closing_price):
        self.symbol = symbol
        self.name = name
        self.opening_price = opening_price
        self.low_price = low_price
        self.high_price = high_price
        self.closing_price = closing_price

    def update_prices(self, opening_price, low_price, high_price, closing_price):
        self.opening_price = opening_price
        self.low_price = low_price
        self.high_price = high_price
        self.closing_price = closing_price

    def calculate_return(self):
        return (self.closing_price - self.opening_price) / self.opening_price


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
            return f"{quantity} shares of {stock.name} bought successfully."
        else:
            return "Insufficient capital to buy the stock."

    def sell_stock(self, stock, quantity):
        if stock in self.portfolio and self.portfolio[stock] >= quantity:
            self.capital += stock.closing_price * quantity
            self.portfolio[stock] -= quantity
            if self.portfolio[stock] == 0:
                del self.portfolio[stock]
            return f"{quantity} shares of {stock.name} sold successfully."
        else:
            return "You don't have enough shares to sell."


# Hardcoded data
stock1 = Stock("AAPL", "Apple Inc.", 150.0, 145.0, 155.0, 152.0)
stock2 = Stock("GOOGL", "Alphabet Inc.", 2000.0, 1950.0, 2050.0, 2020.0)

trader1 = Trader("John", 100000.0)
trader2 = Trader("Jane", 150000.0)

# Simulate trading
trader1.buy_stock(stock1, 100)
trader2.buy_stock(stock2, 50)
trader1.sell_stock(stock1, 50)
trader2.buy_stock(stock1, 200)

# Determine who ends up with the highest capital
traders = [trader1, trader2]
traders.sort(key=lambda x: x.capital, reverse=True)

print(f"The trader with the highest capital is {traders[0].name} with {traders[0].capital} dollars.")