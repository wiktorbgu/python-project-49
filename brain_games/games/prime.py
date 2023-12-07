#!/usr/bin/env python3
from random import randint
from brain_games.game_runer import run_game

MIN_VAL_RANDOM_NUMBER = 1
MAX_VAL_RANDOM_NUMBER = 1000
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(random_number):
    if random_number <= 1:
        return False
    for i in range(2, int(random_number / 2) + 1):
        if random_number % i == 0:
            return False
    return True


def brain_prime(info=None):
    if info == 'description':
        return DESCRIPTION
    randvalue = randint(MIN_VAL_RANDOM_NUMBER, MAX_VAL_RANDOM_NUMBER)
    print(f'Question: {randvalue}')
    if is_prime(randvalue) is True:
        return 'yes'
    else:
        return 'no'


def run_brain_prime():
    run_game(brain_prime)
