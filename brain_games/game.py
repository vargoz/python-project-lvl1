import sys
from random import randint

from brain_games.cli import (
    greet,
    welcome_user,
    get_game_description,
    get_win_phrase,
    get_loose_phrase,
)


def get_number():
    return randint(-sys.maxsize, sys.maxsize)


from brain_games.games.even_numbers import even_numbers_game


def _run_round(game):
    if game == 'brain-even':
        ( res, user_answer, correct_answer ) = even_numbers_game()
    return ( res, user_answer, correct_answer )


_rounds_per_game = 3


def game(username, game):
    get_game_description(game)
    
    counter = 0

    while counter < _rounds_per_game:
        ( res, user_answer, correct_answer ) = _run_round(game)
        if not res:
            get_loose_phrase(user_answer, correct_answer, username)
            return
        counter += 1
    
    get_win_phrase(username)
