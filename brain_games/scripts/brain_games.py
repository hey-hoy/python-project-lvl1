#!/usr/bin/env python
"""Script to playing brain games."""

from ..cli import welcome_user


def main():
    """
    Run the Brain Games.

    Returns:
        str
    """
    print('Welcome to the Brain Games!')
    print('Hello, {name}!'.format(name=welcome_user()))
    return 'Game over.'


if __name__ == '__main__':
    main()
