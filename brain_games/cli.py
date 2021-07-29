"""User representation."""
import prompt


def welcome_user():
    """
    Return a user's self-introduction.

    Returns:
        str
    """
    return prompt.string('May I have your name? ')


def ask(question: str):
    """
    Return an answer to question.

    Args:
            question: question to user

    Returns:
        str
    """
    return prompt.string(question)
