"""Even check game."""
import logging

from brain_games.cli import welcome_user
from brain_games.cli import user_answer


def game(explain, args, question, correct_answer):
    """
    Run even check game.

    Returns:
        str
    """
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.info('Welcome to the Brain Games!')
    user_name = welcome_user()
    log.info('Hello, {0}!'.format(user_name))
    log.info(explain)
    QUESTIONS_COUNT = 3
    for _index in range(0, QUESTIONS_COUNT):
        current_args = args()
        answer = user_answer('Question: {0}\n'
                             'Your answer: '.format(question(current_args)))
        if answer == correct_answer(current_args):
            log.info('Correct!')
        else:
            log.info("""
        '{0}' is wrong answer ;(.Correct answer was '{1}'.
        Let's try again, {2}!
    """.format(answer, correct_answer(current_args), user_name))
            return 'Game over.'
    log.info('Congratulations, {0}!'.format(user_name))
    return 'Win!'


if __name__ == '__main__':
    pass
