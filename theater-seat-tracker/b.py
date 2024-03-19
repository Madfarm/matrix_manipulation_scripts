class Theater:
    def __init__(self, rows, cols):
        self.seats = [['available' for _ in range(cols)] for _ in range(rows)]
        self.prices = [[self.calculate_price(i, j) for j in range(cols)] for i in range(rows)]

    def calculate_price(self, row, col):
        return (row + 1) * (col + 1)

    def buy_ticket(self, row, col):
        if self.seats[row][col] == 'available':
            self.seats[row][col] = 'taken'
            return self.prices[row][col]
        else:
            return 'Sorry, this seat is already taken.'

# Demonstration
theater = Theater(5, 5)
print(theater.seats)
print(theater.prices)
print(theater.buy_ticket(1, 1))
print(theater.seats)
print(theater.prices)