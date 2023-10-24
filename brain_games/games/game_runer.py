from brain_games.cli import welcome_user

ROUND_GAME = 3
USERNAME = welcome_user()


def run_game(game):
    current_round = 0
    while (current_round < ROUND_GAME):
        current_round += 1
        user_answer, correct_result = game(current_round)
        if user_answer == correct_result:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{correct_result}'.")
            print(f"Let's try again, {USERNAME}!")
            break
    if current_round == ROUND_GAME:
        print(f'Congratulations, {USERNAME}!')
