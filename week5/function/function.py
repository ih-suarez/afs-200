def step1():
    user_input = []
    print(f'I will be asking you for 3 numbers')
    
    for i in range(3):
        num = int(input(f'Give me a number: '))
        user_input.append(num)

    input_max = max(num for num in user_input)
    input_min = min(num for num in user_input)

    print(f'Your Numbers are: {user_input}. Calculating the max. ')
    print(f'The Max from the numbers given is {input_max}')
    print(f'The Min from the numbers given is {input_min}')

step1()