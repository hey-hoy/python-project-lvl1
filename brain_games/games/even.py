"""Even check game."""
from random import randint

MAX_NUMBER = 100
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Is it even."""
    return not bool(number % 2)


def question_answer():
    """Return one question and answer for even check game."""
    argument = randint(0, MAX_NUMBER)
    return str(argument), 'yes' if is_even(argument) else 'no'
