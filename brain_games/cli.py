"""CLI interactions with user."""

import prompt


def greet():
    """Greeting on startup event."""
    print('Welcome to the Brain Games!')


def welcome_user():
    """User acquaintance.

    Returns:
        user's name.
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


brain_even_description = 'Answer "yes" if the number is even, \
otherwise answer "no".'
brain_calc_description = 'What is the result of the expression?'
brain_gcd_description = 'Find the greatest common divisor of given numbers.'
brain_progression_description = 'What number is missing in the progression?'
brain_prime_description = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'


def print_game_description(game):
    """Print game explanation.

    Parameters:
        game: name of the game
    """
    if game == 'brain-even':
        print(brain_even_description)
        return
    if game == 'brain-calc':
        print(brain_calc_description)
        return
    if game == 'brain-gcd':
        print(brain_gcd_description)
        return
    if game == 'brain-progression':
        print(brain_progression_description)
        return
    if game == 'brain-prime':
        print(brain_prime_description)
        return


question_string = 'Question: '
answer_prompt = 'Your answer: '


def print_win_phrase(username):
    """Print win phrase.

    Parameters:
        username: user's name
    """
    print('Congratulations, {0}!'.format(username))


def print_loose_phrase(user_answer, correct_answer, username):
    """Print loose phrase.

    Parameters:
        user_answer: user's answer
        correct_answer: correct answer
        username: user's name
    """
    print("'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.\n\
Let's try again, {user}!".
        format(  # noqa: E128 (intendation)
            user_answer=user_answer,
            correct_answer=correct_answer,
            user=username,
        ),
    )
