# Write maintainable code like it's a psychopath who knows where you live
# who's going to maintain it

# Table
# * list players  // typen spillere varier
# * Dealer dealer // typen dealer varierer
# * game objects  // dette varierer

class Table():

    def __init__(self, players, dealer):
        self.players = players
        self.dealer = dealer

    def print_players(self):
        print(", ".join(self.players))
