# Write maintainable code like it's a psychopath who knows where you live
# who's going to maintain it

#  Write code like comments don't exist

from player import Player

class RoulettePlayer(Player):

    def place_bet_name(self):
        print("What kind of bet do you want to place? ", end='')
        return input()

    def place_roulette_number_bet(self):
        def make_int_list(arr): # adapter here
                for idx, entry in enumerate(arr):
                    try:
                        arr[idx] = int(arr[idx])
                    except ValueError:
                        print("Retry: ")
        def is_all_elements_int(arr):
                for element in arr:
                    if type(arr) is not int:
                        return False
                return True

        print("What numbers do you bet on? ", end='')
        self.number_bet = input().split()
        while not is_all_elements_int(self.number_bet):
            print("Retry: ", end='')
            self.number_bet = input().split()
        return make_int_list(self.number_bet)

    def place_column_or_row_bet(self, name=None):
        print
