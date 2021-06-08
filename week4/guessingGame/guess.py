import random

def game():
    name = input('What is your name? ')

    number_to_guess = random.randint(1, 9)
    number_of_guesses = 1
    user_guess = input(f'Hello {name.capitalize()} Give me your best guess of what number I am thinking of.. 1 to 9: ')
    user_exit = 'exit'

    while user_guess != user_exit:
        number_of_guesses += 1
        if int(user_guess) < number_to_guess:
            print(f'{user_guess} is a bit low, {name.capitalize()} ')
            user_guess = input(f'{name.capitalize()} try another number 1-9 ')

        if int(user_guess) > number_to_guess:
            print(f"{user_guess} is a bit high, {name.capitalize()}")
            user_guess = input(f'{name.capitalize()} give it another shot, 1-9 ')

        if int(user_guess) == number_to_guess:
            print(f"You can type 'exit' to stop playing.")
            print(f'{name.capitalize()} you guessed it! You got it in {number_of_guesses} guesses. ')
            user_guess = input(f'Keep playing... 1-9, hit me with another guess ')

        if str(user_guess)  == user_exit:
            print(f'Thank you for playing {name.capitalize()}! ')     

        if user_guess == str():
            print(f'{user_guess} is not valid. Guess again')
            user_guess = input(f'{name.capitalize()} guess a number, 1-9 ')

game()
