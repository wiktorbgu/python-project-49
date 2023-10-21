import prompt
from random import randint, choices
from ..cli import welcome_user

round_game = 3
name = welcome_user()


def main():
    print('What number is missing in the progression?')
    answer = True
    current_round = 0
    game_over = False
    while (answer and current_round < round_game):
        current_round += 1
        length = randint(5, 10)
        randvalue_start = randint(1, 50)
        randvalue_step = randint(1, 30) * choices((1, -1))[0]  # для рандомной возможности обратного шага
        result_progression = []
        result_max_value = randvalue_start + (length * randvalue_step)
        for i in range(randvalue_start, result_max_value, randvalue_step):
            result_progression.append(str(i))
        index_skip_value = randint(0, length - 1)
        secret_val = result_progression[index_skip_value]
        result_progression[index_skip_value] = '..'
        progression_str = ' '.join(result_progression)
        print(f'Question: {progression_str}')
        answer = prompt.string('Your answer: ')
        if secret_val == answer:
            print('Correct!')
        else:
            game_over = True
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{secret_val}'.")
            break
    if game_over:
        print(f"Let's try again, {name}!")
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
