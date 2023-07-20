def equal_strings(st1, st2):
    str1 = sorted(st1)
    str2 = sorted(st2)
    if str1 == str2:
        return True
    else:
        return False
print(equal_strings('love', 'evol'))

# EXTRA CHALLENGE
def swap_values(arr: list):
# Create a variable for first number 
    first_number = arr[0]
# Create a second variable for the last number 
    last_number = arr[-1]
# assign last number to index 1
    arr[0] = last_number
# assign first number to index -1
    arr[-1] = first_number
    return arr
list1 = [2, 4, 67, 7]
print(swap_values(list1))