#!/usr/bin/env python3
from random import randint
from math import gcd
from brain_games.game_runer import run_game

MIN_VAL_RANDOM_NUMBER = 1
MAX_VAL_RANDOM_NUMBER = 50
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def brain_gcd(info=None):
    if info == 'description':
        return DESCRIPTION
    randvalue1 = randint(MIN_VAL_RANDOM_NUMBER, MAX_VAL_RANDOM_NUMBER)
    randvalue2 = randint(MIN_VAL_RANDOM_NUMBER, MAX_VAL_RANDOM_NUMBER)
    correct_result = gcd(randvalue1, randvalue2)
    print(f'Question: {randvalue1} {randvalue2}')
    return str(correct_result)


def run_brain_gcd():
    run_game(brain_gcd)
