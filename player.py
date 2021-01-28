import deck

class Player:
    """ Represents one player taking part in the card game """

    def __init__(self, id: int):
        """ Initialize a player with an identifier

        Args:
            id: An integer that identifies this player

        """

        self._ident = id
        self._hand = []

    def getHand(self) -> list:
        """ Returns a list of cards in the player's hand """

        return self._hand

    def draw(self, cards: deck.Deck):
        """ Take one card from the deck 
        
        Args:
            cards: The deck of cards to draw from

        """

        self._hand.append(cards.draw())

    def show(self):
        """ Display cards in player's hand """

        for deck.card in self._hand:
            deck.card.show()
