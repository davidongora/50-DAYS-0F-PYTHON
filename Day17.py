import random
num = random.randint(0,10)
def user_name():
    name = input('Enter name: ') 
    name = name[::-1]
    username = name + str(num)
    return username
print(user_name())

# EXTRA CHALLENGE
def sort_length(arr: list):
    for item in range(len(arr)):
        for j in range(len(arr) - 1):
# Check if any of the words is longer than the other 
            if len(arr[j]) > len(arr[j + 1]):
                # swap the longest for the shortest
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

names = ["Peter", "Jon", "Andrew"]
print(sort_length(names))