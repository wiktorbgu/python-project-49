import prompt
from random import randint, choices
from brain_games.cli import welcome_user

round_game = 3
name = welcome_user()

MIN_LENGTH_PROGRESSION = 5
MAX_LENGTH_PROGRESSION = 10

MIN_VAL_STEP = 1
MAX_VAL_STEP = 30

MIN_VAL_START_PROGRESS = 1
MAX_VAL_START_PROGRESS = 50


def main():
    print('What number is missing in the progression?')
    answer = True
    current_round = 0
    game_over = False
    while (answer and current_round < round_game):
        current_round += 1
        length = randint(MIN_LENGTH_PROGRESSION, MAX_LENGTH_PROGRESSION)
        randval_start = randint(MIN_VAL_START_PROGRESS, MAX_VAL_START_PROGRESS)
        # * choices для рандомной возможности обратного шага
        randval_step = randint(MIN_VAL_STEP, MAX_VAL_STEP) * choices((1, -1))[0]
        result_progression = []
        result_max_value = randval_start + (length * randval_step)
        for i in range(randval_start, result_max_value, randval_step):
            result_progression.append(str(i))
        index_skip_value = randint(0, length - 1)
        secrt = result_progression[index_skip_value]
        result_progression[index_skip_value] = '..'
        progression_str = ' '.join(result_progression)
        print(f'Question: {progression_str}')
        answer = prompt.string('Your answer: ')
        if secrt == answer:
            print('Correct!')
        else:
            game_over = True
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{secrt}'.")
            break
    if game_over:
        print(f"Let's try again, {name}!")
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
