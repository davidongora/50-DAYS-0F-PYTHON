import string
import random
def password_generator():
# string module constants
    a = string.ascii_letters + \ 
    string.digits + string.punctuation 
    password1 =[]
    length = input("Pick your password length "
"a,b or c: \na. weak \nb.strong \nc."
"Very strong...: ")
    if length == 'a': 
        length = 5
    elif length == 'b': 
        length = 8
    elif length == 'c': 
        length = 12
    for i in range(length):
        password = str(random.choice(a)) 
        password1.append(password)
    return 'You password is', ''.join(password1) 
print(password_generator())