#!/usr/bin/env python3
import prompt
from random import randint
from math import gcd
from brain_games.cli import welcome_user

round_game = 3
name = welcome_user()

MIN_VAL_RANDOM_NUMBER = 1
MAX_VAL_RANDOM_NUMBER = 50


def main():
    print('Find the greatest common divisor of given numbers.')
    answer = True
    current_round = 0
    game_over = False
    while (answer and current_round < round_game):
        current_round += 1
        randvalue1 = randint(MIN_VAL_RANDOM_NUMBER, MAX_VAL_RANDOM_NUMBER)
        randvalue2 = randint(MIN_VAL_RANDOM_NUMBER, MAX_VAL_RANDOM_NUMBER)
        reslt = gcd(randvalue1, randvalue2)
        print(f'Question: {randvalue1} {randvalue2}')
        answer = prompt.string('Your answer: ')
        if reslt == int(answer):
            print('Correct!')
        else:
            game_over = True
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{reslt}'.")
            break
    if game_over:
        print(f"Let's try again, {name}!")
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
