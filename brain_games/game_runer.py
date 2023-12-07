import prompt
from brain_games.cli import welcome_user

ROUND_GAME = 3


def run_game(game):
    USERNAME = welcome_user()
    current_round = 0
    print(game('description'))
    while (current_round < ROUND_GAME):
        current_round += 1
        correct_result = game()
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_result:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{correct_result}'.")
            print(f"Let's try again, {USERNAME}!")
            break
    if current_round == ROUND_GAME:
        print(f'Congratulations, {USERNAME}!')
