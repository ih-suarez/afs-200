def step1():
    print(f'I will be asking you for 3 numbers')
    num1 = int(input(f'Give me the first number: '))
    num2 = int(input(f'Give me the second number: '))
    num3 = int(input(f'Give me the third number: '))

    user_input = [num1, num2, num3]
    input_max = max(num for num in user_input)
    input_min = min(num for num in user_input)

    print(f'Your Numbers are: {user_input}. Calculating the max. ')
    print(f'The Max from the numbers given is {input_max}')
    print(f'The Min from the numbers given is {input_min}')

step1()