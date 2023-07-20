def your_password():
    password1 = input('Enter password')
    password = len(password1) * '*'
    return f'You password is {password} ' \
           f'and its {len(password)} characters long'
print(your_password())

#EXTRA CHALLENGE
def convert_numbers(n): 
    new_list = []
    for num in n:
        new_list.append("{:,}".format(num))
    return new_list
print(convert_numbers([1000000, 2356989, 2354672, 9878098]))