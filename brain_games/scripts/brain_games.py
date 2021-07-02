"""Script to playing brain games."""
import logging
import sys

from brain_games.cli import welcome_user


def main():
    """
    Run the Brain Games.

    Returns:
        str
    """
    log = logging.getLogger()
    log.level = logging.DEBUG
    log.addHandler(logging.StreamHandler(sys.stderr))
    log.info('Welcome to the Brain Games!')
    log.info('Hello, {name}!'.format(name=welcome_user()))
    return 'Game over.'


if __name__ == '__main__':
    main()
