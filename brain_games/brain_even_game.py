"""Even check game."""
from random import SystemRandom
MAX_NUMBER = 100
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Is it even?"""
    return True if (number % 2) == 0 else False


def question_answer():
    """Return one question and answer for even check game."""
    argument = SystemRandom().randrange(MAX_NUMBER)
    return str(argument), 'yes' if is_even(argument) else 'no'

