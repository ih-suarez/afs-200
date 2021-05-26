# Getting input to determine if numbers are even or odd
class user_input_eve_or_odd():
    number = int(input('What number do you have for me? '))
    check_if_even_or_odd = number % 2

    if check_if_even_or_odd == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")

user_input_eve_or_odd()

# Is 'Number' a multiple of 4
class is_number_multiple_of_4():
    number = int(input('Give me a number and I will tell you if it is a multiple of 4... '))
    
    if number % 4 == 0:  
        print(f"Yes, {number} is a multiple of 4")
    else:
        print(f"No, {number} is not a multiple of 4")

is_number_multiple_of_4()

# Does 'Num' divides evenly into 'Check'
class is_it_divisible():
    num = int(input('Give me a number to be divided... '))
    check = int(input(f"Give me a number that {num} will be divided by... "))
    
    if num % check == 0:
        print(f"The numbers {num} and {check} are Divisible")
    else:
        print(f"The numbers {num} and {check} are Not Divisible")

is_it_divisible()
