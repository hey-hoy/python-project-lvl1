"""Greatest common divisor game."""
from random import SystemRandom
from math import gcd

from brain_games.game_processor import game


def main():
    """
    Run greatest common divisor game.

    Returns:
        str
    """
    explain = 'Find the greatest common divisor of given numbers.'

    def args():
        max_number = 100
        return [SystemRandom().randrange(max_number),
                SystemRandom().randrange(max_number)]

    def question(arguments):
        return ' '.join(str(arguments))

    def correct_answer(arguments):
        number, second_number = arguments
        return str(gcd(number, second_number))

    game(explain, args, question, correct_answer)


if __name__ == '__main__':
    main()
