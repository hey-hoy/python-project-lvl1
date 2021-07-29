"""Greatest common divisor game."""
from random import SystemRandom
DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 100


def gcd(a, b):
    """Return greatest common divisor of a and b."""
    return a if b == 0 else gcd(b, a % b)


def question_answer():
    """Return one question and answer for greatest common divisor game."""
    number = SystemRandom().randrange(MAX_NUMBER)
    second_number = SystemRandom().randrange(MAX_NUMBER)
    question = str(number) + ' ' + str(second_number)
    answer = str(gcd(number, second_number))
    return question, answer
