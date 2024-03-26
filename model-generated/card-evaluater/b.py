class Card:
    def __init__(self, value, quality, price):
        self.value = value
        self.quality = quality
        self.price = price

def knapSack(cards, money):
    n = len(cards)
    dp = [[0 for i in range(money + 1)] for j in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for m in range(money + 1):
            if i == 0 or m == 0:
                dp[i][m] = 0
            elif cards[i - 1].price <= m:
                dp[i][m] = max(
                    dp[i - 1][m],
                    dp[i - 1][m - cards[i - 1].price]
                    + (cards[i - 1].value * cards[i - 1].quality),
                )
            else:
                dp[i][m] = dp[i - 1][m]

    # Store the result of Knapsack
    res = dp[n][money]
    print("Maximum value of items that can be carried:", res)

    w = money
    result = []
    for i in range(n, 0, -1):
        if res <= 0:
            break
        # either the result comes from the
        # top (K[i-1][w]) or from (val[i-1]
        # + K[i-1] [w-wt[i-1]]) as in Knapsack
        # table. If it comes from the latter
        # one/ it means the item is included.
        if res == dp[i - 1][w]:
            continue
        else:
            # This item is included.
            result.append(cards[i - 1])

            # Since this weight is included
            # its value is deducted
            res = res - (cards[i - 1].value * cards[i - 1].quality)
            w = w - cards[i - 1].price

    return result

# Test the function
cards = [
    Card(10, 2, 5),
    Card(20, 1, 10),
    Card(30, 3, 15),
    Card(40, 2, 20),
    Card(50, 1, 25),
]

money = 50
print("Cards to buy:", knapSack(cards, money))