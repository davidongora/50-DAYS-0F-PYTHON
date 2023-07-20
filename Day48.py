def search_binary(list1, x):
    low = 0
    high = len(list1) - 1 
    mid_index = 0
    while low <= high:
        mid_index = (high + low) // 2
        if list1[mid_index] == x: 
            return mid_index
        # if an element is lower than the middle index
        # then search the lower part of the list
        elif list1[mid_index] > x:
            high = mid_index - 1
# if an element is higher than the middle index # then search the upper part of the list
        elif list1[mid_index] < x:
            low = mid_index + 1
# if an element is not found, return -1
    return 'no element'
list1 = [12, 34, 56, 78, 98, 22, 45, 13] 
list1 = sorted(list1)
number = 22
results = search_binary(list1, number) 
if results == 'no element':
    print('Element is not in the list')
else:
    print(f'The element index is {results}')