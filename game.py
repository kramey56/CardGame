""" Play a game of cards 

The game is played by two or more players using a standard deck of 52 cards.
The cards are shuffled and each player takes a turn drawing one card from the
deck until each player has three cards.

Each player's score is determined by adding the value of their cards. The value
of each card is determined by multiplying its suit value by the points value
of the card. The player with the highest score wins.

"""

import deck
import player

def sort(cards: list) -> list:
    return sorted(cards, key=lambda x: (x._suit, x._value))

def score(hand: list) -> int:
    """ Calculate the score of a hand 

    Args:
        hand: A list of cards in the hand

    Returns:
        The score as an integer

    """

    suitVals = {"Spades": 1, "Diamonds": 2, "Hearts": 3, "Clubs": 4}
    total = 0
    for deck.card in hand:
        total += suitVals[deck.card.getSuit()] * deck.card.getValue()

    return total

if __name__ == "__main__":
    print("* * * * Start of game * * * *")
    player1 = player.Player(1)
    player2 = player.Player(2)

    # Create a deck and shuffle it
    cardDeck = deck.Deck()
    cardDeck.shuffle()

    # Each player draws three cards
    for _ in range(1, 4):
        player1.draw(cardDeck)
        player2.draw(cardDeck)

    # Show hands and calculate scores

    print("Player 1's hand:")
    player1.show()
    score1 = score(player1.getHand())
    print(f"Player 1 score: {score1}")
    print("\nPlayer 2's hand:")
    player2.show()
    score2 = score(player2.getHand())
    print(f"Player 2 score: {score2}\n")

    # Determine winner

    if score1 > score2:
        print(f"Player 1 wins with a score of {score1}")
    elif score2 > score1:
        print(f"Player 2 wins with a score of {score2}")
    else:
        print(f"The game is a tie with a score of {score1}")
