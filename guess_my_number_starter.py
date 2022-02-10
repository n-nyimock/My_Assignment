import random
my_code_range = random.randint(1, 99)
perfect_guess = None


while perfect_guess != my_code_range:
    perfect_guess = input('Guess a number between 1 and 99: ')
    perfect_guess = int(perfect_guess)

    if perfect_guess == 94:
        print('Congratulations! You won, the number was: 94')
        break
    elif perfect_guess > 94:
        print('Try again, your guess is too high!')
    else:
        print('Try again, your guess is too low!')
