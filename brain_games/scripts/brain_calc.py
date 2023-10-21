import prompt
from random import randint, choices
from ..cli import welcome_user

round_game = 3
name = welcome_user()


def plus(s1, s2):
    return s1 + s2


def minus(s1, s2):
    return s1 - s2


def multiple(s1, s2):
    return s1 * s2


operations = {'+': plus,
              '-': minus,
              '*': multiple}


def main():
    print('What is the result of the expression?')
    answer = True
    current_round = 0
    game_over = False
    while (answer and current_round < round_game):
        current_round += 1
        randvalue1 = randint(1, 50)
        randvalue2 = randint(1, 50)
        operation = choices(list(operations.keys()))[0]
        print(f'Question: {randvalue1} {operation} {randvalue2}')
        answer = prompt.string('Your answer: ')
        reslt = operations[operation](randvalue1, randvalue2)
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
