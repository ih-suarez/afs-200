#Sting manipulation
# name=input('What is your name? ')
# age=input('How old are you? ')
# print('Welcome ' + name + '  your age is ' + age)
# print(name, 'is going to be 100 by', currentYear - age + 100)

from datetime import datetime

def user_input(): 
    name=input('What is your name? ') 
    age=int(input('How old are you? '))
    return name, age

def year_when_100(age): 
    return 100 - age + datetime.now().year

if __name__ == "__main__":
    name, age = user_input()
    print(f"{name} is going to be 100 by {year_when_100(age)}")