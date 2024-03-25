class Share:
    def __init__(self, opening_price, closing_price, highest_price, lowest_price, volume):
        self.opening_price = opening_price
        self.closing_price = closing_price
        self.highest_price = highest_price
        self.lowest_price = lowest_price
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

    def top_5_highest_price(self):
        sorted_shares = sorted(self.shares, key=lambda x: x.highest_price, reverse=True)
        return sorted_shares[:5]

    def top_5_lowest_price(self):
        sorted_shares = sorted(self.shares, key=lambda x: x.lowest_price)
        return sorted_shares[:5]

    def highest_volume(self):
        sorted_shares = sorted(self.shares, key=lambda x: x.volume, reverse=True)
        return sorted_shares[0]

    def lowest_volume(self):
        sorted_shares = sorted(self.shares, key=lambda x: x.volume)
        return sorted_shares[0]

    def highest_profit_margin(self):
        sorted_shares = sorted(self.shares, key=lambda x: x.highest_price - x.lowest_price, reverse=True)
        return sorted_shares[0]


# Create shares
share1 = Share(100, 120, 150, 90, 50000)
share2 = Share(80, 90, 100, 70, 70000)
share3 = Share(120, 130, 160, 110, 60000)

# Create daily report and add shares
report = DailyReport()
report.add_share(share1)
report.add_share(share2)
report.add_share(share3)

# Print advice for each share
for share in report.shares:
    print(f"Advice for share with opening price {share.opening_price}: {share.advice()}")

# Print top 5 highest and lowest price shares
print("Top 5 highest price shares:")
for share in report.top_5_highest_price():
    print(f"Highest price: {share.highest_price}, Lowest price: {share.lowest_price}")

print("Top 5 lowest price shares:")
for share in report.top_5_lowest_price():
    print(f"Highest price: {share.highest_price}, Lowest price: {share.lowest_price}")

# Print share with highest and lowest volume
print(f"Share with highest volume: {report.highest_volume().volume}")
print(f"Share with lowest volume: {report.lowest_volume().volume}")

# Print share with highest profit margin
print(f"Share with highest profit margin: {report.highest_profit_margin().highest_price - report.highest_profit_margin().lowest_price}")