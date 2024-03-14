class Dealer:
    def __init__(self):
        self.deck = []
        self.hand = []
        self.discard_pile = []

    def shuffle_deck(self):
        import random
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.deck = [{'suit': suit, 'rank': rank} for suit in suits for rank in ranks]
        random.shuffle(self.deck)

    def deal_cards(self, num):
        self.hand = [self.deck.pop() for _ in range(num)]

    def discard_cards(self):
        self.discard_pile.extend(self.hand)
        self.hand = []

    def flip_top_card(self):
        return self.deck[-1]

    def burn_card(self):
        self.discard_pile.append(self.deck.pop())

# Test the Dealer class
dealer = Dealer()
dealer.shuffle_deck()
print("Deck: ", dealer.deck)

dealer.deal_cards(5)
print("Hand: ", dealer.hand)

dealer.discard_cards()
print("Hand after discarding: ", dealer.hand)
print("Discard pile: ", dealer.discard_pile)

print("Top card: ", dealer.flip_top_card())

dealer.burn_card()
print("Top card after burning: ", dealer.flip_top_card())