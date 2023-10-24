#!/usr/bin/env python3
import prompt
from random import randint
from brain_games.games.game_runer import run_game

MIN_VAL_RANDOM_NUMBER = 1
MAX_VAL_RANDOM_NUMBER = 1000


def is_prime(random_number):
    if random_number <= 1:
        return False
    for i in range(2, int(random_number / 2) + 1):
        if random_number % i == 0:
            return False
    return True


def brain_prime(current_round):
    if current_round == 1:
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
    randvalue = randint(MIN_VAL_RANDOM_NUMBER, MAX_VAL_RANDOM_NUMBER)
    print(f'Question: {randvalue}')
    answer = prompt.string('Your answer: ')
    if is_prime(randvalue) is True:
        return answer, 'yes'
    else:
        return answer, 'no'


def run_brain_prime():
    run_game(brain_prime)


if __name__ == '__main__':
    run_game(brain_prime)
