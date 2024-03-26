class Card:
    def __init__(self, value, quality, price):
        self.value = value
        self.quality = quality
        self.price = price

def knapSack(cards, money):
    # Create a 2D array to store the maximum value that can be achieved at each capacity
    dp = [[0 for _ in range(money + 1)] for _ in range(len(cards) + 1)]
    
    # Fill the array
    for i in range(1, len(cards) + 1):
        for j in range(1, money + 1):
            # If the price of the current card is less than or equal to the current capacity,
            # consider whether it is better to include it or not
            if cards[i - 1].price <= j:
                dp[i][j] = max(
                    dp[i - 1][j],  # Don't include the current card
                    dp[i - 1][j - cards[i - 1].price] + (cards[i - 1].value * cards[i - 1].quality)  # Include the current card
                )
            # If the price of the current card is greater than the current capacity,
            # it cannot be included, so just copy the value from the previous iteration
            else:
                dp[i][j] = dp[i - 1][j]
    
    # Reconstruct the best set of cards
    i, j = len(cards), money
    result = []
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            result.append(cards[i - 1])
            j -= cards[i - 1].price
        i -= 1
    
    return result

# Define some cards
cards = [
    Card(value=1, quality=2, price=10),
    Card(value=2, quality=1, price=15),
    Card(value=1, quality=3, price=20),
    Card(value=3, quality=2, price=25),
    Card(value=2, quality=3, price=30)
]

# Set the amount of money
money = 50

# Get the best set of cards
best_set = knapSack(cards, money)

# Print the result
for card in best_set:
    print(f"Value: {card.value}, Quality: {card.quality}, Price: {card.price}")