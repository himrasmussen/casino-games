# Write maintainable code like it's a psychopath who knows where you live
# who's going to maintain it

#  Write code like comments don't exist

import webbrowser
from pprint import pprint

from dealer import BetHandling

class RouletteBetHandling(BetHandling):

    bet_types = [
        "single", "split", "street",
        "corner", "six line", "trio",
        "basket",
        "low", "manque", "high", "passe",
        "red", "black", "even", "odd",
        "dozen bet", "column bet", "snake bet"
    ]

    bet_types_description = {
        "single": "Bet on a single number",
        "split": "Bet on two vertically/horizontally adjacent numbers (e.g. 14-17 or 8-9)",
        "street": "Bet on three consecutive numbers in a horizontal line (e.g. 7-8-9)",
        "corner": "Bet on four numbers that meet at one corner (e.g. 10-11-13-14)",
        "six line": "Bet on six consecutive numbers that form two horizontal lines (e.g. 31-32-33-34-35-36)",
        "trio": "A three-number bet that involves at least one zero: 0-1-2 (either layout); 0-2-3 (single-zero only); 0-00-2 or 00-2-3 (double-zero only)",
        "basket": "Bet on 0-1-2-3",

        "low", : "A bet that the number will be in the range 1-18",
        "high": "A bet that the number will be in the range 19-36",
        "red": "A bet that the number will be red",
        "black": "A bet that the number will be black",
        "even": "A bet that the number will be even",
        "odd": "A bet that the number will be odd",
        "dozen bet": "A bet that the number will be in the chosen dozen (1-12, 13-24, 25-36)",
        "column bet": "A bet that the number will be in the chosen column (1-4-7-10 and so on) ",
        "snake bet": "A special bet that covers the numbers 1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, and 34"
    }

    required_numbers_for_each_bet_type = {
        "straight": 1, "split": 2, "street": 3,
        "corner": 4, "square": 4, "six line": 6,
        "double street": 6, "trio": 3, "basket": 4,
        "first four": 4, **{
        entry: 0 for entry in [
        "low", "manque", "high", "passe",
        "red", "black", "even", "odd",
        "dozen bet", "column bet", "snake bet"
        ]}
    }

# TODO: Enter row or column for those bets
# TODO: Enter option for check if special bet input type

    def take_roulette_type_bet(self, player):
        print("What type of bet do you want to place? ", end='')
        self.roulette_type_bet = player.place_roulette_type_bet()
        while self.roulette_type_bet not in self.bet_types:
            print("Retry: ", end='')
            self.roulette_type_bet = player.place_roulette_type_bet()
        self.store_bet(self, player, 'bet_type', self.roulette_type_bet)

    def take_roulette_numbers_bet(self, player, bet_type):
        def is_all_elements_int(arr):
            for element in arr:
                if type(arr) is not int:
                    print("Enter only integers.")
                    return False
            return True
        def are_all_numbers_between_0_and_36(arr):
            for num in arr:
                if not 0 <= num <= 36:
                    print("Enter only numbers from 0 to 36.")
                    return False
            return True
        def is_valid_bet(self, bet_type, bet_numbers):

            def are_numbers_adjacent(bet_numbers):
                if abs(min(bet_numbers) - max(bet_numbers)) == (1 or 3):
                    return True
                elif 0 in bet_numbers and (1 or 2 or 3) in bet_numbers:
                    return True
                return False

            def are_numbers_around_a_corner(bet_numbers):
                if max(bet_numbers) - min(bet_numbers)  == 4 and \
                bet_numbers[2] - bet_numbers[1] == 2:
                    return True
                return False

            def are_3_numbers_consecutive_along_a_horizontal_line(bet_numbers):
                if bet_numbers[0] == bet_numbers[1] - 3 == bet_numbers[2] - 6:
                    return True
                return False

            def are_6_numbers_consecutive_along_two_horizontal_rows(bet_numbers):
                def is_difference_one(a, b):
                    if abs(a - b) == 1:
                        return True
                    return False

                for i in range(len(bet_numbers)-1):
                    if not is_difference_one(bet_number[i], bet_number[i+1]):
                        return False
                    return True

            def has_bet_0_and_either_1_2_or_3(bet_numbers):
                if 0 in bet_numbers:
                    if (1 or 2 or 3) in bet_numbers:
                        return True
                return False


            the_massive_dict_of_legal_numbers_relative_to_bet_type = {
                "single": True,
                "split": True if are_numbers_adjacent(bet_numbers) else False,
                "corner" True if are_numbers_around_a_corner(bet_numbers) else False,
                "street": True if are_3_numbers_consecutive_along_a_horizontal_line(bet_numbers) else False,
                "six line": True if are_6_numbers_consecutive_along_two_horizontal_rows(bet_numbers) else False,
                "basket" True if has_bet_0_and_either_1_2_or_3(bet_numbers)
            }

        def get_sorted_bet_numbers():
            print("Enter numbers you want to bet on: ", end='')
            self.bet_numbers = player.place_roulette_numbers_bet()
            while not is_all_elements_int(self.bet_numbers_bet) or \
                      are_all_numbers_between_0_and_36(self.take_roulette_numbers_bet) or \
                      self.is_valid_bet(bet_type, self.bet_numbers):
                self.bet_numbers = player.place_roulette_numbers_bet()
            return self.bet_numbers.sort()

    # def check_number_bet_validity(self, bet_type, number_bet):
        # pass


    def take_bet(self, player):
        self.take_money_bet(player)
        self.take_roulette_type_bet(player)
        # self.take_roulette_numbers_bet(self, player) or self.take_column_or_row_bet(self, player)


if __name__ == '__main__':
    roulette = RouletteBetHandling(minimum_table_bet=150)
