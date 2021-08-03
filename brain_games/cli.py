"""User representation."""
import prompt


def ask(question: str):
    """
    Return an answer to question.

    Attributes
    ----------
    question : str
        Question to user
    """
    return prompt.string(question)
