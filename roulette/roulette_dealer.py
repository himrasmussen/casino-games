# Write maintainable code like it's a psychopath who knows where you live
# who's going to maintain it

#  Write code like comments don't exist

from dealer import BetHandling

class RouletteBetHandling(BetHandling):

    legal_bet_types = [
        "straight", "split", "street",
        "corner", "square", "six line",
        "double street", "trio", "basket",
        "first four", "top line",
        "low", "manque", "high", "passe",
        "red", "black", "even", "odd",
        "dozen bet", "column bet", "snake bet"
    ]

    the_layout = [[x, x+1, x+2] for x in range(1, 37, 3)]

    def take_roulette_type_bet(self, player):
        pass


    def take_bet(self, player):
        self.take_money_bet(self, player)
        # TODO: self.take_roulette_type_bet()
        # TODO: self.take_roulette_numbers_bet()


if __name__ == '__main__':
    roulette = RouletteBetHandling()
    print(roulette.legal_bet_types)
