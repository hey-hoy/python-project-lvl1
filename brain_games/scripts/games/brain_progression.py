"""Progression game."""
from random import SystemRandom

from brain_games.game_processor import game


def main():
    """
    Run progression game.

    Returns:
        str
    """
    explain = 'What number is missing in the progression?'

    def args():
        MAX_START_NUMBER = 20
        MAX_ADD = 8
        MIN_COUNT = 5
        MAX_COUNT = 10
        COUNT = SystemRandom().randrange(MIN_COUNT, MAX_COUNT)
        return [SystemRandom().randrange(MAX_START_NUMBER),
                SystemRandom().randrange(MAX_ADD),
                COUNT,
                SystemRandom().randrange(COUNT)]

    def question(arguments):
        start_number, add, count, question_number = arguments
        numbers = [str(start_number + x * add) for x in range(count)]
        numbers[question_number] = '..'
        return ' '.join(numbers)

    def correct_answer(arguments):
        start_number, add, count, question_number = arguments
        return str(start_number + question_number * add)

    game(explain, args, question, correct_answer)
