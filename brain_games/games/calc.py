"""The calculation game. Find the result of the generated expression."""

from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'

MIN_NUMBER = -10
MAX_NUMBER = 10

OPERATORS = ('+', '-', '*')


def _calculate(num_a, num_b, operator):
    if operator == '+':
        return num_a + num_b
    if operator == '-':
        return num_a - num_b
    if operator == '*':
        return num_a * num_b


def run_round():
    """Get data for the one round of the brain-calc game.

    Returns:
        expression: generated expression,
        correct_answer
    """
    num_a = randint(MIN_NUMBER, MAX_NUMBER)
    num_b = randint(MIN_NUMBER, MAX_NUMBER)
    operator = choice(OPERATORS)

    expression = f'{num_a} {operator} {num_b}'
    correct_answer = str(_calculate(num_a, num_b, operator))

    return (expression, correct_answer)
