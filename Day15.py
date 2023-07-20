def same_in_reverse(a):
    if a == a[::-1]:
        return True
    else:
        return False
print(same_in_reverse('mad'))

# EXTRA CHALLENGE
names_age ={"jane": 23, "kerry": 45, "tim": 34, "peter": 27}
def your_age():
# Convert name to lowercase letters
    name = input("Please enter your name: ").lower() # Use for loop to iterate over the dictionary
    for key in names_age.keys():
        if key == name:
# use the get method to access a specific value.
            return f'Hi, {name}! You are {names_age.get(key)} years old'
    else:
        # if name not in the dictionary
        while name not in names_age.keys():
            age = input("Your name is not in the dictionary, "
"please enter your age? ").lower() # Update the dictionary with name and age.
            names_age.update({name: age})
            return f'Hi, {name}! You are {names_age.get(name)} years old'
print(your_age())