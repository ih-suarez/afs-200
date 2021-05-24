# Getting input to determine if even or odd
class user_input_eve_or_odd():
    number = int(input('What number do you have for me? '))
    check_if_even_or_odd = number % 2
    if check_if_even_or_odd == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")
user_input_eve_or_odd()