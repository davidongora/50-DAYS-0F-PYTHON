def count_dots(word):
    m = word.split(".")
    return f'The string has {len(m)-1} dots'
print(count_dots("h.e.l.p."))

# Extra Challenge
from datetime import datetime
def your_age():
    while True:
        birth_year = input('Enter your year of birth: ') 
        if len(birth_year) != 4:
            print('Please enter a four digits year')
        elif int(birth_year) < 1900 or int(birth_year) > 2022:
            print('Please enter a valid year')
        else:
# This returns the current year
            now1 = int(datetime.now().strftime("%Y")) 
            age = (now1 - int(birth_year)) * 525600
            return f'You are {age:,} minutes old.'
print(your_age())