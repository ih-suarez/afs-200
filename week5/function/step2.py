def step2():
    print(f'Let us try something new.') 
    string_input = str(input(f'Give me a random word and I will tell you how many letters are uppercase or lowercase '))

    def count(string):
        upper, lower = 0, 0
        for letter in range(len(string)):
            if string[letter].isupper():
                upper += 1
            elif string[letter].islower():
                lower += 1
        print(f'Upper case letters: {upper}')
        print(f'Lower case letters: {lower}')
    count(string_input)
step2()