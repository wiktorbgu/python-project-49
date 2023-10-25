#!/usr/bin/env python3
from random import randint, choices
from brain_games.games.game_runer import run_game

MIN_VAL_RANDOM_NUMBER = 1
MAX_VAL_RANDOM_NUMBER = 50


def plus(s1, s2):
    return s1 + s2


def minus(s1, s2):
    return s1 - s2


def multiple(s1, s2):
    return s1 * s2


operations = {'+': plus,
              '-': minus,
              '*': multiple}


def brain_calc(current_round):
    if current_round == 1:
        print('What is the result of the expression?')
    randvalue1 = randint(MIN_VAL_RANDOM_NUMBER, MAX_VAL_RANDOM_NUMBER)
    randvalue2 = randint(MIN_VAL_RANDOM_NUMBER, MAX_VAL_RANDOM_NUMBER)
    operation = choices(list(operations.keys()))[0]
    print(f'Question: {randvalue1} {operation} {randvalue2}')
    correct_result = operations[operation](randvalue1, randvalue2)
    return str(correct_result)


def run_brain_calc():
    run_game(brain_calc)


if __name__ == '__main__':
    run_game(brain_calc)
