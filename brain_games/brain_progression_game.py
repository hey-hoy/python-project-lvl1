"""Progression game."""
from random import SystemRandom
DESCRIPTION = 'What number is missing in the progression?'
MAX_START_NUMBER = 20
MAX_ADD = 8
MIN_COUNT = 5
MAX_COUNT = 10


def question_answer():
    """Return one question and answer for progression game."""
    start_number = SystemRandom().randrange(MAX_START_NUMBER)
    add = SystemRandom().randrange(MAX_ADD)
    count = SystemRandom().randrange(MIN_COUNT, MAX_COUNT)
    question_number = SystemRandom().randrange(count)
    numbers = [str(start_number + x * add) for x in range(count)]
    numbers[question_number] = '..'
    return ' '.join(numbers), str(start_number + question_number * add)

