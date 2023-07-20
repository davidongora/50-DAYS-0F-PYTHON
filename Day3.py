register = {'Michael':'yes', 'John': 'no', 'Peter':'yes', 'Mary': 'yes'}
def register_check(reg: dict):
    # Create a count variable
    count = 0
    for value in reg.values():
        if value == 'yes': count += 1
    return 'Number of students in school is', count 
print(register_check(register))

# EXTRA CHALLENGE
names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
# creating an empty list
d = []
# Using sorted function to sort list in descending order
for name in sorted(names, reverse=True):
    if name.islower():
        d.append(name) 
        tuple_names = tuple(d)
print(tuple_names)