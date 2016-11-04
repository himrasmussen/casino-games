# Write maintainable code like it's a psychopath who knows where you live
# who's going to maintain it

#  Write code like comments don't exist


class BetHandling():

    def __init__(self, minimum_table_bet=None):
        if minimum_table_bet is None:
            raise NotImplementedError("Forgot minimum_table_bet")
        self.bets = {}
        self.minimum_table_bet = minimum_table_bet

    def take_bet(self, player):
        raise NotImplementedError

    def store_bet(self, player, bet_type, bet):
        self.bets[player][bet_type] = bet

    def take_money_bet(self, player):
        self.money_bet = player.place_money_bet()
        while self.money_bet < self.minimum_table_bet:
            print("You have to bet at least {minimum_table_bet}."
                .format(minimum_table_bet = self.minimum_table_bet))
            self.money_bet = player.place_money_bet()
        self.store_bet(self, player, 'money', self.money_bet)



    # def check_is_bet_valid(self, player, bet):
    #     raise NotImplementedError

    def store_bet(self, player, bet):
        raise NotImplementedError

    def take_bets(players):
        for player in players:
            bet = self.take_bet(player)
            self.store_bet(player, bet)


# A dealer class modelling the dealer

    # Takes bets  // bet details varies
    # Checks if bets win  // will always check for who won, but how to do it varies
    # Pays out winners // will always payout, but the way to calculate payout varies
    # Prepare a new round // clear bets and winners is constant, may be more stuff which varies

class Dealer():

    def __init__(self, bet_handling, minimum_table_bet):
        # self.bets = {}
        self.winners = []
        self.bet_handling = bet_handling(minimum_table_bet)
        self.minimum_table_bet = minimum_table_bet

    def check_victory():
        raise NotImplementedError

    def payout_winners(self, winners):
        for winner in winners:
            self.payout(winner)

    def payout():
        raise NotImplementedError

    def new_round(self):
        pass

if __name__ == '__main__':
    pass
