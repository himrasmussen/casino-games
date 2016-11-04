# Write maintainable code like it's a psychopath going to maintain it
# Write code like comments don't exist

# A wheel class which models a roulette wheel
    # All the numbers and colors
        # Straight forward 0 through 36
    # Odd numbers are red, even are blacknumbers = list(range(37))

# TODO: Fix colors 


numbers = list(range(37))
colors = {"even": "black", "odd": "red"} # is this the best way?

class Wheel():

    class Pocket():
        def __init__(self, number):
            self.number = number
            self.color = colors["even"] if self.number % 2 == 0 else colors["odd"]

        def __str__(self):
            return "{number} {color}".format(number=self.number, color=self.color)

    def __init__(self):
        self.pockets = [self.Pocket(number) for number in numbers]

if __name__ == '__main__':
    wheel = Wheel()
    import random
    print(random.choice(wheel.pockets))
