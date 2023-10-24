from brain_games.cli import welcome_user

ROUND_GAME = 3
USERNAME = welcome_user()


def run_game(game):
    current_round = 0
    success_game = True
    while (success_game and current_round < ROUND_GAME):
        current_round += 1
        user_answer, correct_result = game(current_round)
        if user_answer == correct_result:
            print('Correct!')
        else:
            success_game = False
            print(f"'{user_answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{correct_result}'.")
            break
    if success_game:
        print(f'Congratulations, {USERNAME}!')
    else:
        print(f"Let's try again, {USERNAME}!")
