#!/usr/bin/env python3
from random import randint
from brain_games.games.game_runer import run_game

MIN_VAL_RANDOM_NUMBER = 1
MAX_VAL_RANDOM_NUMBER = 25


def brain_even(current_round):
    if current_round == 1:
        print('Answer "yes" if the number is even, otherwise answer "no".')
    randvalue = randint(MIN_VAL_RANDOM_NUMBER, MAX_VAL_RANDOM_NUMBER)
    print(f'Question: {randvalue}')
    if randvalue % 2 == 0:
        return 'yes'
    else:
        return 'no'


def run_brain_even():
    run_game(brain_even)


if __name__ == '__main__':
    run_game(brain_even)
