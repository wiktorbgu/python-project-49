import prompt
from random import randint, choices
from math import gcd
from ..cli import welcome_user

round_game = 3
name = welcome_user()

gcd(7,17)

def main():
    print('Find the greatest common divisor of given numbers.')
    answer = True
    current_round = 0
    game_over = False
    while (answer and current_round < round_game):
        current_round += 1
        randvalue1 = randint(1, 50)
        randvalue2 = randint(1, 50)
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
