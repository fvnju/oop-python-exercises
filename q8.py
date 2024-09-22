"""
Write a class that inherits from the Card_group class of this chapter.
The class should represent a deck of cards that contains only hearts and spades,
with only the cards 2 through 10 in each suit.
Add a method to the class called next2 that returns the top two cards from the deck.
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


class Answer(Card_group):
    def __init__(self):
        self.cards = []
        for s in ["Hearts", "Spades"]:
            for v in range(2, 11):
                self.cards.append(Card(v, s))

    def next2(self, stringify=True):
        if stringify:
            return str(self.nextCard()), str(self.nextCard())
        else:
            return self.nextCard(), self.nextCard()


# Test usage
test = Answer()
print(test.next2())
