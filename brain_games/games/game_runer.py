from brain_games.cli import welcome_user

ROUND_GAME = 3
NAME = welcome_user()


def run_game(game):
    current_round = 0
    success_game = True
    while (success_game and current_round < ROUND_GAME):
        current_round += 1
        user_answer, correct_result = game()
        if user_answer == correct_result:
            print('Correct!')
        else:
            success_game = False
            print(
                f"'{user_answer}' is wrong answer ;(. \
                Correct answer was '{correct_result}'.")
            break
    if success_game:
        print(f'Congratulations, {NAME}!')
    else:
        print(f"Let's try again, {NAME}!")


if __name__ == '__main__':
    run_game()