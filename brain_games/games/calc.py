import prompt
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


def brain_calc():
    print('What is the result of the expression?')
    randvalue1 = randint(MIN_VAL_RANDOM_NUMBER, MAX_VAL_RANDOM_NUMBER)
    randvalue2 = randint(MIN_VAL_RANDOM_NUMBER, MAX_VAL_RANDOM_NUMBER)
    operation = choices(list(operations.keys()))[0]
    print(f'Question: {randvalue1} {operation} {randvalue2}')
    answer = prompt.string('Your answer: ')
    correct_result = operations[operation](randvalue1, randvalue2)
    return answer, correct_result


if __name__ == '__main__':
    run_game(brain_calc)