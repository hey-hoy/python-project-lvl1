"""Script to playing brain games."""
import logging

from brain_games.cli import welcome_user


def main():
    """
    Run the Brain Games.

    Returns:
        str
    """
    log = logging.getLogger()
    log.level = logging.INFO
    log.addHandler(logging.StreamHandler())
    log.info('Welcome to the Brain Games!')
    log.info('Hello, {0}!'.format(welcome_user()))
    return 'Game over.'


if __name__ == '__main__':
    main()
