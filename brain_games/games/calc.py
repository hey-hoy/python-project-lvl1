"""Calc game."""
from random import randint, choice
from operator import add, sub, mul

MAX_NUMBER = 100
COUNT_NUMBERS = 2
DESCRIPTION = 'What is the result of the expression?'
functions = {' + ': add, ' - ': sub, ' * ': mul}


def question_answer():
    """Return one question and answer for calc game."""
    numbers = [randint(0, MAX_NUMBER) for _ in range(COUNT_NUMBERS)]
    fn_name, function = choice(list(functions.items()))
    question = str(numbers[0]) + fn_name + str(numbers[1])
    answer = str(function(numbers[0], numbers[1]))
    return question, answer
