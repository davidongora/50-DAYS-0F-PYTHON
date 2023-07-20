def string_range(num:int):
    x = [str(i) for i in range(num)] 
    #Using join method to add dots
    x = ".".join(x) 
    return x
print(string_range(6))


# EXTRA CHALLENGE

names = ["Joseph", "Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]
d = {} # Creating an empty dictionary 
for name in names:
    if name.startswith('S'):
# Using the dictionary update method 
        d.update({name: names.count(name)})
print(d)


# SECOND METHOD
from collections import Counter
count = [] # Creating an empty list
for name in names:
    if name.startswith("S"):
        # Appending names that start with S to the list
        count.append(name)
# Using the counter method to return a dictionary
names = Counter(count)
print(names)