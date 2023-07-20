def convert_add(list1):
    b = []
    for i in list1:
        b.append(int(i))
    return sum(b)
print(convert_add(['1','3','5']))

# EXTRA CHALLENGE

def check_duplicates(arr: list):
    for item in arr:
        # Using count to find items more than one
        if arr.count(item) > 1:
# lists
            return item
        else:
            return 'No duplicates'
fruits = ['apple', 'orange', 'banana', 'apple'] 
names = ['Yoda', 'Moses', 'Joshua', 'Mark']
print(check_duplicates(fruits))
print(check_duplicates(names))