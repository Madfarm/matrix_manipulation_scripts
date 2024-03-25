class Share:
    def __init__(self, name, opening_price, closing_price, high, low, volume):
        self.name = name
        self.opening_price = opening_price
        self.closing_price = closing_price
        self.high = high
        self.low = low
        self.volume = volume

    def advice(self):
        if self.closing_price > self.opening_price:
            return "Buy"
        elif self.closing_price < self.opening_price:
            return "Sell"
        else:
            return "Hold"


class DailyReport:
    def __init__(self):
        self.shares = []

    def add_share(self, share):
        self.shares.append(share)

    def top_highest_price(self, n):
        return sorted(self.shares, key=lambda x: x.high, reverse=True)[:n]

    def top_lowest_price(self, n):
        return sorted(self.shares, key=lambda x: x.low)[:n]

    def top_highest_volume(self, n):
        return sorted(self.shares, key=lambda x: x.volume, reverse=True)[:n]

    def top_lowest_volume(self, n):
        return sorted(self.shares, key=lambda x: x.volume)[:n]

    def highest_profit_margin(self):
        return max(self.shares, key=lambda x: x.high - x.low)


# Example usage
report = DailyReport()

share1 = Share("AAPL", 150.0, 160.0, 170.0, 140.0, 1000000)
share2 = Share("GOOG", 2000.0, 2100.0, 2200.0, 1900.0, 5000000)
share3 = Share("MSFT", 250.0, 240.0, 260.0, 230.0, 7500000)

report.add_share(share1)
report.add_share(share2)
report.add_share(share3)

print("Top 2 highest price shares:")
for share in report.top_highest_price(2):
    print(share.name)

print("\nTop 2 lowest price shares:")
for share in report.top_lowest_price(2):
    print(share.name)

print("\nTop 2 highest volume shares:")
for share in report.top_highest_volume(2):
    print(share.name)

print("\nShare with the highest profit margin:")
print(report.highest_profit_margin().name)