def uniq_numbers(a: list):
    list1 = []
    for number in a:
        if number not in list1:
            list1.append(number) 
    dif = sum(a) - sum(list1)
    if dif % 2 == 0: return a
    else:
        return list1
print(uniq_numbers([1, 2, 4, 5, 6, 7, 8, 8]))

# EXTRA CHALLENGE
def difference(arr1: list, arr2: list):
    # Find items in list 1 not in list 2
    list1 = [i for i in arr1 if i not in arr2 ] # Find items in list 2 one not in list 1 
    list2 = [j for j in arr2 if j not in arr1] # concatenate the two lists
    return 'The difference between two sets is ', list1 + list2
print(difference(list1, list2))