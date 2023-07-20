def index_position (a): 
    idex = []
    for i, item in enumerate(a):
        if item.islower():
            idex.append(i)
    return idex
print(index_position('LovE'))

# EXTRA CHALLENGE
def largest_number(arr: list):
# Create empty list
    list1 = []
# remove brackets and spaces in the lists
    n = str(arr).strip('[,]').replace(',', '').replace(' ', '') # append the numbers to the empty list
    for i in n:
        list1.append(int(i))
# Sorting the list in descending order
    list1.sort(reverse=True)
# removing parenthesis and spaces from the sorted
# list and converting it to int
    large_number = int(str(list1).strip('[]').replace(',', '').replace(' ', '')) # return a large formatted number
    return 'The largest number is, {:,}'.format(large_number)
n = [3, 67, 87, 9, 2] 
print(largest_number(n))