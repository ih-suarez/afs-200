import random

def step3():
    user_input = int(input(f'Enter a number I can multiply '))
    random_multiple = random.randint(1, 100)

    multiply_random = lambda user_input: user_input*random_multiple
    print(f'Your number was multiplied by {random_multiple} and the result was {multiply_random(user_input)}')
step3()