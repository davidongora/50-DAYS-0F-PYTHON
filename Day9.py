def biggest_odd(string1: str):
    odd_nums = [i for i in string1 if int(i) % 2 != 0] 
    return f' The biggest old number is {max(odd_nums)}'
print(biggest_odd('23569'))

# EXTRA CHALLENGE
def zeros_last(arr: list) -> list:
    i=0 #settingindex0
    arr1 = arr
    for num in arr:
# Checking for non-zero numbers
        if num != 0:
# Moving non-zero numbers to the front of the list
            arr[i] = num
            i += 1
# Moving zero elements to the end of the list.
    while i < len(arr):
        arr[i] = 0
        i += 1
        return arr
    else:
# if no zeros return original list in ascending order
        return sorted(arr1)
list1 = [1, 4, 6, 0, 7, 0] 
list2 = [2, 1, 4, 7, 6]
print(zeros_last(list1))
print(zeros_last(list2))