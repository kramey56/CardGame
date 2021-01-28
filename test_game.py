import pytest
import deck
import game

def test_sort():
    cards = []
    cards.append(deck.Card(deck.Suits.SPADES, 2))
    cards.append(deck.Card(deck.Suits.DIAMONDS, 5))
    cards.append(deck.Card(deck.Suits.SPADES, 13))
    cards.append(deck.Card(deck.Suits.HEARTS, 3))
    cards.append(deck.Card(deck.Suits.CLUBS, 14))

    testCards = []
    testCards.append(deck.Card(deck.Suits.SPADES, 2))
    testCards.append(deck.Card(deck.Suits.SPADES, 13))
    testCards.append(deck.Card(deck.Suits.DIAMONDS, 5))
    testCards.append(deck.Card(deck.Suits.HEARTS, 3))
    testCards.append(deck.Card(deck.Suits.CLUBS, 14))

    newCards = game.sort(cards)
    
    match = True
    for c in range(0, 5):
        match = match and (newCards[c].getSuit() == testCards[c].getSuit())
        match = match and (newCards[c].getValue() == testCards[c].getValue())

    assert match
