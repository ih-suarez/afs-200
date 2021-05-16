#Sting manipulation
from datetime import datetime

name = input('What is your name? ') 
age = int(input('How old are you? '))

year_subject_is_100 = 100 - age + datetime.now().year

print(f"{name.capitalize()}'s age is {age} and is going to be 100 by the year {year_subject_is_100}")