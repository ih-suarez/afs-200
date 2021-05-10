#Sting manipulation
from datetime import datetime

def user_input(): 
    name=input('What is your name? ') 
    age=int(input('How old are you? '))
    return name, age

def year_when_100(age): 
    return 100 - age + datetime.now().year

if __name__ == "__main__":
    name, age = user_input()
    print(f"{name}'s age is {age} and is going to be 100 by the year {year_when_100(age)}")