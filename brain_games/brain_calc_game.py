"""Calc game."""
from random import SystemRandom
MAX_NUMBER = 100
DESCRIPTION = 'What is the result of the expression?'
FUNCTIONS = [[int.__add__, ' + '],
             [int.__sub__, ' - '],
             [int.__mul__, ' * ']]


def question_answer():
    """Return one question and answer for calc game."""
    number = SystemRandom().randrange(MAX_NUMBER)
    function = FUNCTIONS[SystemRandom().randrange(len(FUNCTIONS))]
    second_number = SystemRandom().randrange(MAX_NUMBER)
    return str(number) + function[1] + str(second_number), str(function[0](number, second_number))

