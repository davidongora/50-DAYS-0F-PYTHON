def capitalize(a: str):
    upper = []
    for i, word in enumerate(a.split()):
        if word[0].islower():
            upper.append(word.capitalize()) 
        else:
            upper.append(word)
    return ' '.join(upper)
print(capitalize('i like learning'))

# EXTRA CHALLENGE
import string
str1 = 'leArning is hard, bUt if You appLy youRself ' \
'you can achieVe success'
upper_names = []
for word in str1.split():
    for letter in word:
# Using string module to find uppercase letters 
        if letter in string.ascii_uppercase:
            upper_names.append("".join(word[::-1]))
print(upper_names)