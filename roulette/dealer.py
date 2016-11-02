# Write maintainable code like it's a psychopath going to maintain it
# Write code like comments don't exist


# A dealer class modelling the dealer


    # Takes bets
    # Spins wheel # specific to Roulette Dealer
    # Checks if bets win
    # Pays out winning bets

from random import choice

class Dealer():

    def __init__(self):
        self.bets = {}

    def take_bet(player):
        raise NotImplementedError

    def take_bets(players):
        for player in players:
            InheritingClass.take_bet(player)

    def check_victory():
        raise NotImplementedError

    def payout():
        raise NotImplementedError
