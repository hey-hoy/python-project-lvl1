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

    Attributes
    ----------
    question : str
        Question to user
    """
    return prompt.string(question)
