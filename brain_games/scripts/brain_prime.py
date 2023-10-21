import prompt
from random import randint
from brain_games.cli import welcome_user

round_game = 3
name = welcome_user()
dict_answer = {'yes': True, 'no': False}

MIN_VAL_RANDOM_NUMBER = 1
MAX_VAL_RANDOM_NUMBER = 1000


def is_prime(random_number):
    if random_number <= 1:
        return False
    for i in range(2, int(random_number / 2) + 1):
        if random_number % i == 0:
            return False
    return True


def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    answer = True
    current_round = 0
    game_over = False
    while (answer and current_round < round_game):
        current_round += 1
        randvalue = randint(MIN_VAL_RANDOM_NUMBER, MAX_VAL_RANDOM_NUMBER)
        print(f'Question: {randvalue}')
        answer = prompt.string('Your answer: ')
        if is_prime(randvalue) is True:
            if dict_answer[answer] is True:
                print('Correct!')
            else:
                game_over = True
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                break
        else:
            if dict_answer[answer] is False:
                print('Correct!')
            else:
                game_over = True
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                break
    if game_over:
        print(f"Let's try again, {name}!")
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
