# Write maintainable code like it's a psychopath who knows where you live
# who's going to maintain it

# Roulette Table
# * Wheel wheel

from pprint import pprint

from table import Table
from wheel import Wheel

class RouletteTable(Table):

    the_layout = [['', 0, '']] + [[x, x+1, x+2] for x in range(1, 37, 3)]
    wheel = Wheel()


if __name__ == '__main__':
    players = ["Big-O", "Lambda"]
    dealer = "Lil D"
    table = RouletteTable(players, dealer)
    pprint(table.the_layout)
