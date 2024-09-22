"""
Use the `Standard_deck` class of this section to create a simplified version of the game War.
In this game, there are two players. Each starts with half of a deck.
The players each deal the top card from their decks and
whoever has the higher card wins the other player’s cards and
adds them to the bottom of his deck. If there is a tie,
the two cards are eliminated from play (this differs from the actual game, but is simpler to program).
The game ends when one player runs out of cards.
"""

import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        names = ["Jack", "Queen", "King", "Ace"]
        if self.value <= 10:
            return "{} of {}".format(self.value, self.suit)
        else:
            return "{} of {}".format(names[self.value - 11], self.suit)


class Card_group:
    def __init__(self, cards=[]):
        self.cards = cards

    def nextCard(self):
        return self.cards.pop(0)

    def hasCard(self):
        return len(self.cards) > 0

    def size(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)


class Standard_deck(Card_group):
    def __init__(self):
        self.cards = []
        for s in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for v in range(2, 15):
                self.cards.append(Card(v, s))


player1 = Standard_deck()
player1.cards = player1.cards[: len(player1.cards) // 2]
player1.shuffle()

player2 = Standard_deck()
player2.cards = player2.cards[: len(player2.cards) // 2]
player2.shuffle()

while player1.hasCard() and player2.hasCard():
    p1_card = player1.nextCard()
    p2_card = player2.nextCard()
    print(f"Player 1 played {p1_card}, Player 2 played {p2_card}\n")
    if p1_card.value > p2_card.value:
        player1.cards.append(p2_card)
    elif p1_card.value < p2_card.value:
        player2.cards.append(p1_card)
    else:
        pass

if player1.hasCard():
    print(f"Player 1 wins with {player1.size()} cards left")
else:
    print(f"Player 2 wins with {player2.size()} cards left")
