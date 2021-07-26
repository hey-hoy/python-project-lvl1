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
        max_start_number = 20
        max_add = 8
        min_count = 5
        max_count = 10
        count = SystemRandom().randrange(min_count, max_count)
        return [SystemRandom().randrange(max_start_number),
                SystemRandom().randrange(max_add),
                count,
                SystemRandom().randrange(count)]

    def question(arguments):
        start_number, add, count, question_number = arguments
        numbers = [str(start_number+x*add) for x in range(count)]
        numbers[question_number] = '..'
        return ' '.join(numbers)

    def correct_answer(arguments):
        start_number, add, count, question_number = arguments
        return str(start_number+question_number*add)

    game(explain, args, question, correct_answer)
