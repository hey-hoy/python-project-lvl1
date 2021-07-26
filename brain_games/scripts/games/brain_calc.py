"""Calc game."""
from random import SystemRandom
from brain_games.game_processor import game


def main():
    """
    Run calculator game.

    Returns:
        str
    """
    explain = 'What is the result of the expression?'

    def args():
        MAX_NUMBER = 100
        functions = [[int.__add__, ' + '],
                     [int.__sub__, ' - '],
                     [int.__mul__, ' * ']]
        return SystemRandom().randrange(MAX_NUMBER), functions[
            SystemRandom().randrange(len(functions))
        ], SystemRandom().randrange(MAX_NUMBER)

    def question(arguments):
        number, func, second_number = arguments
        return str(number) + func[1] + str(second_number)

    def correct_answer(arguments):
        number, func, second_number = arguments
        return str(func[0](number, second_number))

    game(explain, args, question, correct_answer)


if __name__ == '__main__':
    main()
