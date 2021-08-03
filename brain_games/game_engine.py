"""Engine to all games."""
from brain_games.cli import ask

QUESTIONS_COUNT = 3


def run(game):
    """Run game."""
    print('Welcome to the Brain Games!')
    user_name = ask('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    print(game.DESCRIPTION)
    for _ in range(0, QUESTIONS_COUNT):
        question, answer = game.question_answer()
        user_answer = ask(
            'Question: {0}\nYour answer: '.format(question)
        )
        if user_answer == answer:
            print('Correct!')
        else:
            print(
                "'{0}' is wrong answer ;(.Correct answer was '{1}'.\n"
                "Let's try again, {2}!".format(user_answer, answer, user_name)
            )
            break
    else:
        print('Congratulations, {0}!'.format(user_name))
