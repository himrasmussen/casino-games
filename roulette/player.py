# Write maintainable code like it's a psychopath who knows where you live
# who's going to maintain it

#  Write code like comments don't exist

# A player class modelling the players
    # Has money
    # Can bet money

class Player():

    def __init__(self, id, money):
        self.id = id
        self.money = money

    def place_bet():
        raise NotImplementedError

    def place_money_bet(self):
        def get_nonnegative_int():
            n = -1
            while n < 0:
                try:
                    n = int(input())
                    if n < 0:
                        print("Retry: ", end='')
                except ValueError:
                    print("Retry: ", end='')
            return n

        print("How much do you bet? ", end='')
        self.money_bet = get_nonnegative_int()
        while self.money_bet > self.money:
            print("You don't have that much money.")
            self.money_bet = get_nonnegative_int()
        return self.money_bet

if __name__ == '__main__':
    player = Player(1, 2000)
    player.place_money_bet()
