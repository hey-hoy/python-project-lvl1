"""Greatest common divisor game."""
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 100


def gcd(first, second):
    """Return greatest common divisor of first and second number."""
    return first if second == 0 else gcd(second, first % second)


def question_answer():
    """Return one question and answer for greatest common divisor game."""
    number = randint(0, MAX_NUMBER)
    second_number = randint(0, MAX_NUMBER)
    question = '{0} {1}'.format(str(number), str(second_number))
    answer = str(gcd(number, second_number))
    return question, answer
