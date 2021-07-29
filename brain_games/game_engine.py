"""Engine to all games."""
import logging

from brain_games.cli import welcome_user
from brain_games.cli import ask
QUESTIONS_COUNT = 3


def run(game):
    """Run game."""
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.info('Welcome to the Brain Games!')
    user_name = welcome_user()
    log.info('Hello, {0}!'.format(user_name))
    log.info(game.DESCRIPTION)
    for _ in range(0, QUESTIONS_COUNT):
        question, answer = game.question_answer()
        user_answer = ask('Question: {0}\n'
                          'Your answer: '.format(question))
        if user_answer == answer:
            log.info('Correct!')
        else:
            log.info("""'{0}' is wrong answer ;(.Correct answer was '{1}'.
Let's try again, {2}!""".format(user_answer, answer, user_name))
            break
    else:
        log.info('Congratulations, {0}!'.format(user_name))
