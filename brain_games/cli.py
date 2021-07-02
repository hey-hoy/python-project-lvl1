"""User representation."""
import prompt


def welcome_user():
    """
    Return a user's self-introduction.

    Returns:
        str
    """
    return prompt.string('May I have your name? ')
