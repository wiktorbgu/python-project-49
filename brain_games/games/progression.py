#!/usr/bin/env python3
from random import randint, choices
from brain_games.games.game_runer import run_game

MIN_LENGTH_PROGRESSION = 5
MAX_LENGTH_PROGRESSION = 10

MIN_VAL_STEP = 1
MAX_VAL_STEP = 30

MIN_VAL_START_PROGRESS = 1
MAX_VAL_START_PROGRESS = 50


def brain_progression(current_round):
    if current_round == 1:
        print('What number is missing in the progression?')
    length = randint(MIN_LENGTH_PROGRESSION, MAX_LENGTH_PROGRESSION)
    randval_start = randint(MIN_VAL_START_PROGRESS, MAX_VAL_START_PROGRESS)
    # * choices для рандомной возможности обратного шага
    randval_step = randint(MIN_VAL_STEP, MAX_VAL_STEP) * choices((1, -1))[0]
    result_progression = []
    result_max_value = randval_start + (length * randval_step)
    for i in range(randval_start, result_max_value, randval_step):
        result_progression.append(str(i))
    index_skip_value = randint(0, length - 1)
    correct_result = result_progression[index_skip_value]
    result_progression[index_skip_value] = '..'
    progression_str = ' '.join(result_progression)
    print(f'Question: {progression_str}')
    return str(correct_result)


def run_brain_progression():
    run_game(brain_progression)


if __name__ == '__main__':
    run_game(brain_progression)
