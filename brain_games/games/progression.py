"""Progression game."""
from random import randint

DESCRIPTION = 'What number is missing in the progression?'
MAX_START_NUMBER = 20
MAX_ADD = 8
MIN_COUNT = 5
MAX_COUNT = 10


def generate_progression(start, addition, length):
    """Return progression as list of str."""
    return [str(start + number * addition) for number in range(length)]


def question_answer():
    """Return one question and answer for progression game."""
    start_number = randint(0, MAX_START_NUMBER)
    add = randint(0, MAX_ADD)
    count = randint(MIN_COUNT, MAX_COUNT)
    question_number = randint(0, count)
    numbers = generate_progression(start_number, add, count)
    numbers[question_number] = '..'
    return ' '.join(numbers), str(start_number + question_number * add)
