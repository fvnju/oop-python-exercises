"""
Write a class called Poker_hand that has a field that is a list of Card objects. 
There should be the following self-explanatory methods:

    has_royal_flush, has_straight_flush, has_four_of_a_kind, has_full_house, 
    has_flush, has_straight, has_three_of_a_kind, has_two_pair, has_pair

There should also be a method called best that returns a string 
indicating what the best hand is that can be made from those cards.
"""

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class Poker_hand:
    def __init__(self):
        self.cards = []

    def has_royal_flush(self):
        return self.has_straight_flush() and max(card.rank for card in self.cards) == 14

    def has_straight_flush(self):
        return self.has_flush() and self.has_straight()

    def has_four_of_a_kind(self):
        ranks = [card.rank for card in self.cards]
        return any(ranks.count(rank) == 4 for rank in set(ranks))

    def has_full_house(self):
        ranks = [card.rank for card in self.cards]
        return self.has_three_of_a_kind() and self.has_pair()

    def has_flush(self):
        return len(set(card.suit for card in self.cards)) == 1

    def has_straight(self):
        ranks = sorted(set(card.rank for card in self.cards))
        return len(ranks) == 5 and ranks[-1] - ranks[0] == 4

    def has_three_of_a_kind(self):
        ranks = [card.rank for card in self.cards]
        return any(ranks.count(rank) == 3 for rank in set(ranks))

    def has_two_pair(self):
        ranks = [card.rank for card in self.cards]
        pairs = sum(1 for rank in set(ranks) if ranks.count(rank) == 2)
        return pairs == 2

    def has_pair(self):
        ranks = [card.rank for card in self.cards]
        return any(ranks.count(rank) == 2 for rank in set(ranks))

    def best(self):
        if self.has_royal_flush():
            return "Royal Flush"
        elif self.has_straight_flush():
            return "Straight Flush"
        elif self.has_four_of_a_kind():
            return "Four of a Kind"
        elif self.has_full_house():
            return "Full House"
        elif self.has_flush():
            return "Flush"
        elif self.has_straight():
            return "Straight"
        elif self.has_three_of_a_kind():
            return "Three of a Kind"
        elif self.has_two_pair():
            return "Two Pair"
        elif self.has_pair():
            return "Pair"
        else:
            return "High Card"

# TEST usage
def test_poker_hand():
    # Create a new poker hand
    hand = Poker_hand()

    # Add cards to the hand
    hand.cards = [
        Card(10, "Hearts"),
        Card(11, "Hearts"),
        Card(12, "Hearts"),
        Card(13, "Hearts"),
        Card(14, "Hearts")
    ]

    # Test different hand types
    print("Royal Flush:", hand.has_royal_flush())
    print("Straight Flush:", hand.has_straight_flush())
    print("Flush:", hand.has_flush())
    print("Straight:", hand.has_straight())
    print("Best hand:", hand.best())

    # Create a new hand for testing other combinations
    hand.cards = [
        Card(10, "Hearts"),
        Card(10, "Diamonds"),
        Card(10, "Spades"),
        Card(11, "Hearts"),
        Card(11, "Diamonds")
    ]

    print("\nTesting new hand:")
    print("Four of a Kind:", hand.has_four_of_a_kind())
    print("Full House:", hand.has_full_house())
    print("Three of a Kind:", hand.has_three_of_a_kind())
    print("Two Pair:", hand.has_two_pair())
    print("Pair:", hand.has_pair())
    print("Best hand:", hand.best())

    # Test a hand with just a pair
    hand.cards = [
        Card(10, "Hearts"),
        Card(10, "Diamonds"),
        Card(2, "Spades"),
        Card(5, "Hearts"),
        Card(8, "Clubs")
    ]

    print("\nTesting hand with just a pair:")
    print("Pair:", hand.has_pair())
    print("Two Pair:", hand.has_two_pair())
    print("Best hand:", hand.best())

if __name__ == "__main__":
    test_poker_hand()