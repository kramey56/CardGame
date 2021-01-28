import pytest
import random
import deck

def test_newDeck():
    """ Test that new decks are all the same size """

    deck1 = deck.Deck()
    deck2 = deck.Deck()
    assert deck1.size() == deck2.size()

def test_deckOrder():
    """ Test that all new, unshuffled decks are in same order """
    deck1 = deck.Deck()
    deck2 = deck.Deck()
    count = random.randint(0, 50)
    for i in range(count):
        card1 = deck1.draw()
        card2 = deck2.draw()

    assert ((card1.getSuit() == card2.getSuit()) and 
                                (card1.getValue() == card2.getValue()))

def test_random():
    """ Test that a shuffled deck is in different order than new deck """
    deck1 = deck.Deck()
    deck2 = deck.Deck()
    deck2.shuffle()

    card1 = deck1.draw()
    card2 = deck2.draw()

    assert ((card1.getSuit() != card2.getSuit()) or 
                                (card1.getValue() != card2.getValue()))

def test_draw():
    """ Verify that deck size decreases with draws """

    testDeck = deck.Deck()
    startSize = testDeck.size()

    testDeck.draw()
    newSize = testDeck.size()

    assert newSize < startSize