def any_num (*args):
    ave = sum(args)/len(args) 
    return f'The average is {ave}'
print(any_num(12, 90))

# EXTRA CHALLENGE
def add_reverse(n:list, k:list): # Creating an empty list
    new_list = []
    if len(n) == len(k):
        for i in range(0, len(n)):
# adding and appending corresponding numbers 
            new_list.append(n[i] + k[i])
# Reversing new list
            new_list.reverse()
        return new_list
    else:
        return f'Lists have different lengths'
# Lists to add and reverse
list1 = [10, 12, 34] 
list2 = [12, 56, 78]
print(add_reverse(list1, list2))