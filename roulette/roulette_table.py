# Write maintainable code like it's a psychopath who knows where you live
# who's going to maintain it

# Roulette Table
# * Wheel wheel

from table import Table
from wheel import Wheel

class RouletteTable(Table):

    def __init__(self, players, dealer):
        super().__init__(players, dealer)
        self.wheel = Wheel()


if __name__ == '__main__':
    players = ["Big-O", "Lambda"]
    dealer = "Lil D"
    table = RouletteTable(players, dealer)
