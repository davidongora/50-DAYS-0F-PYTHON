def password_checker(): 
    errors = []
    while True:
        password = input('Enter your password: ') 
        if not any(i.isupper() for i in password):
            errors.append("Please add at least one " "capital letter to your password")
        elif not any(i.islower() for i in password):
            errors.append("Please add at least one "
"small letter to your password") 
        elif not any(i.isdigit() for i in password):
            errors.append('Please add at least one ' 'number to your password')
        elif len(password) < 8: 
            errors.append("Your password is less "
"than 8 characters") 
        if len(errors) > 0:
            print('Check the following errors:')
            print(str(errors))
            del errors[0:]
        else:
            return f'Your password is {password}'
print(password_checker())

# EXTRA CHALLENGE
def email_validator(arr: list): # Creating an empty list. 
    valid_emails = []
    for email in arr:
        # conditions that make email valid
        if "@" in email and email.count('@') == 1 and email[-4:] == '.com': 
            if email[0] != '@':
                valid_emails.append(email)
# Checking if list with emails is empty.
        elif len(valid_emails) == 0: return 'All emails are invalid'
    return f'The list of valid emails is: {valid_emails}'
emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com', ] 
print(email_validator(emails))