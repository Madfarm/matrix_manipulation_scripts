class Dealer:
    def __init__(self):
        self.deck = []
        self.hand = []

    def shuffle_deck(self):
        # Assume that we have a function shuffle() that shuffles the deck
        self.deck = shuffle(self.deck)

    def deal_cards(self, num_cards):
        # Deal num_cards from the deck to the dealer's hand
        for _ in range(num_cards):
            self.hand.append(self.deck.pop())

    def discard_hand(self):
        # Discard the current hand and put the cards back into the deck
        self.deck.extend(self.hand)
        self.hand = []

# Create a dealer
dealer = Dealer()

# Shuffle the deck
dealer.shuffle_deck()

# Deal 5 cards
dealer.deal_cards(5)
print("Dealer's hand:", dealer.hand)

# Discard the hand
dealer.discard_hand()
print("Dealer's hand after discarding:", dealer.hand)