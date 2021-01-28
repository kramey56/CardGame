import random
from enum import IntEnum

class Suits(IntEnum):
    SPADES = 1
    DIAMONDS = 2
    HEARTS = 3
    CLUBS = 4

class Card:
    """ Represent a standard playing card

    Each card has a suit and a value. Suit can be one of Hearts, Spades, Clubs,
    or Diamonds. In addition, each suit is given a point value with Spades
    being 1 point, Diamonds 2, Hearts 3, and Clubs 4. Within the suit each
    card has a face value from 2 - 14. A Jack counts for 11 points, Queen is 12,
    King is 13, and an Ace is worth 14.

    """

    def __init__(self, suit: Suits, value: int):
        """ Create a single card
        Args:
            suit: One of Heart, Spade, Club, Diamonds
            value: Between 2 and 14

        """

        self._suit = suit
        self._value = value

    def getSuit(self) -> Suits:
        """ Return the card's suit """

        return self._suit

    def getValue(self) -> int:
        """ Return the face value of the card """

        return self._value

    def show(self):
        """ Display the card suit and value """

        print(f"{self._value} of {self._suit}")

 
class Deck:
    """ Represents a deck of cards

    A standard deck of playing cards. The deck contains 52 cards. A single card
    has a suit and a value. Suits are: Spades, Hearts, Diamonds,
    or Clubs. Each suit is assigned a point value, with Spades being 1 point,
    Diamonds 2, Hearts 3, and Clubs 4. Card values are from 2 - 14, with the
    ace being value 14, king = 13, queen = 12, and jack = 11. All other card 
    values are equal to the face number.

    Methods are provided to randomly shuffle the deck and to deal the top card
    to a player

    """

    def __init__(self):
        """ Initialize the deck of cards

        Create a deck of 52 cards following the definition of a standard
        deck of playing cards.

        """

        self._cards = []
        self._build()

    def _build(self):
        """ Create the deck of cards in sorted order by suit and value """

        for s in Suits:
            for v in range(2, 15):
                self._cards.append(Card(s, v))

    def shuffle(self):
        """ Randomize the deck of cards """

        for i in range(len(self._cards) - 1, 0, -1):
            r = random.randint(0, i)
            self._cards[i], self._cards[r] = self._cards[r], self._cards[i]

    def draw(self) -> Card:
        """ Deal one card from the deck """

        return self._cards.pop()

    def size(self) -> int:
        return len(self._cards)
