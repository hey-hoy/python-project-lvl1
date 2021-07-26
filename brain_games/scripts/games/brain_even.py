"""Even check game."""
from random import SystemRandom

from brain_games.game_processor import game


def main():
    """
    Run even check game.

    Returns:
        str
    """
    explain = 'Answer "yes" if the number is even, otherwise answer "no".'

    def args():
        MAX_NUMBER = 100
        return SystemRandom().randrange(MAX_NUMBER)

    def question(number):
        return number

    def correct_answer(number):
        return 'yes' if (number % 2) == 0 else 'no'

    game(explain, args, question, correct_answer)


if __name__ == '__main__':
    main()
