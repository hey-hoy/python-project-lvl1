"""Is it prime game."""
from math import sqrt
from random import randint

MAX_NUMBER = 1000
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Is it prime."""
    if number < 4:
        return True
    for step in range(2, int(sqrt(number)) + 1):
        if number % step == 0:
            return False
    return True


def question_answer():
    """Return one question and answer for is it prime game."""
    argument = randint(0, MAX_NUMBER)
    return str(argument), 'yes' if is_prime(argument) else 'no'
