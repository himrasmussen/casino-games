#!/usr/bin

# Write maintainable code like it's a psychopath who knows where you live
# who's going to maintain it

#  Write code like comments don't exist

# from roulette_dealer import RouletteDealer
from dealer_roulette import Croupier#, RouletteBetHandling
from table_roulette import RouletteTable
from player_roulette import RoulettePlayer

if __name__ == '__main__':
    players = [RoulettePlayer(id=1, money=200)]
    croupier = Croupier(bet_handling=RouletteBetHandling, minimum_table_bet=10)
    table = RouletteTable(minimum_table_bet=10)
    while True:
        croupier.take_bets(players)
        croupier.spin_wheel()
        croupier.check_players_for_victory(players)
        crouper.payout_winners()
