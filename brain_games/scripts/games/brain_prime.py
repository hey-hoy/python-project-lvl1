"""Is it prime game."""
from random import SystemRandom
from math import sqrt

from brain_games.game_processor import game


def main():
    """
    Run is it prime game.

    Returns:
        str
    """
    explain = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    def args():
        MAX_NUMBER = 1000
        return SystemRandom().randrange(MAX_NUMBER)

    def question(number):
        return str(number)

    # flake8: noqa: C901
    def correct_answer(arguments):
        if arguments < 4:
            return 'yes'
        for n in range(2, int(sqrt(arguments))):
            if arguments % n == 0:
                return 'no'
        return 'yes'

    game(explain, args, question, correct_answer)
