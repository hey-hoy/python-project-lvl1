"""Even check game."""
import logging
import sys
from random import SystemRandom

from brain_games.cli import welcome_user
from brain_games.cli import user_answer


def main():
    """
    Run even check game.

    Returns:
        str
    """
    log = logging.getLogger()
    log.level = logging.DEBUG
    log.addHandler(logging.StreamHandler(sys.stderr))
    log.info('Welcome to the Brain Games!')
    user_name = welcome_user()
    log.info('Hello, {0}!'.format(user_name))
    log.info('Answer "yes" if the number is even, otherwise answer "no".')
    questions_count = 3
    max_number = 100
    for _index in range(0, questions_count):
        number = SystemRandom().randrange(max_number)
        answer = user_answer('Question: {0}\nYour answer: '.format(number))
        correct_answer = 'yes' if (number % 2) == 0 else 'no'
        wrong_answer = 'yes' if correct_answer == 'no' else 'no'
        if answer == correct_answer:
            log.info('Correct!')
        else:
            log.info("""
    '{0}' is wrong answer ;(.Correct answer was '{1}'.
    Let's try again, {2}!
""".format(wrong_answer, correct_answer, user_name))
            return 'Game over.'
    log.info('Congratulations, {0}!'.format(user_name))
    return 'Win!'


if __name__ == '__main__':
    main()
