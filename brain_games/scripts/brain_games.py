"""Script to welcome brain games."""
from brain_games.cli import ask


def main():
    """Run the Brain Games."""
    print('Welcome to the Brain Games!')
    print('Hello, {0}!'.format(ask('May I have your name? ')))


if __name__ == '__main__':
    main()
