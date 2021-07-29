"""Is it prime game."""
from random import SystemRandom
from math import sqrt
MAX_NUMBER = 1000
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Is it even?"""
    if number < 4:
        return True
    for n in range(2, int(sqrt(number))):
        if number % n == 0:
            return False
    return True


def question_answer():
    """Return one question and answer for is it prime game."""
    argument = SystemRandom().randrange(MAX_NUMBER)
    return str(argument), 'yes' if is_prime(argument) else 'no'
