import pytest
import player
import deck

def test_unique():
    """ Verify two unique players """

    player1 = player.Player(1)
    player2 = player.Player(2)

    assert player1 != player2

def test_hand():
    """ Verify the player gets the cards we expect on unshuffled deck """

    player1 = player.Player(1)
    deck1 = deck.Deck()

    testHand = [deck.Card(deck.Suits.CLUBS, 14),
                deck.Card(deck.Suits.CLUBS, 13),
                deck.Card(deck.Suits.CLUBS, 12)]

    match = True
    for _ in range(0, 3):
        player1.draw(deck1)

    cards = player1.getHand()
    for count in range(0, 3):
        match = match and (cards[count].getSuit() == testHand[count].getSuit())
        match = match and (cards[count].getValue() == testHand[count].getValue())

    assert match