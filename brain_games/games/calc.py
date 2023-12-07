#!/usr/bin/env python3
from random import randint, choices
from brain_games.game_runer import run_game
from operator import add, mul, sub

MIN_VAL_RANDOM_NUMBER = 1
MAX_VAL_RANDOM_NUMBER = 50
DESCRIPTION = 'What is the result of the expression?'

operations = {'+': add,
              '-': sub,
              '*': mul}


def brain_calc(info=None):
    if info == 'description':
        return DESCRIPTION
    randvalue1 = randint(MIN_VAL_RANDOM_NUMBER, MAX_VAL_RANDOM_NUMBER)
    randvalue2 = randint(MIN_VAL_RANDOM_NUMBER, MAX_VAL_RANDOM_NUMBER)
    operation = choices(list(operations.keys()))[0]
    print(f'Question: {randvalue1} {operation} {randvalue2}')
    correct_result = operations[operation](randvalue1, randvalue2)
    return str(correct_result)


def run_brain_calc():
    run_game(brain_calc)
