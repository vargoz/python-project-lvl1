"""Logic for CLI interactions with user."""

import prompt


def welcome_user():
    """User acquaintance."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')