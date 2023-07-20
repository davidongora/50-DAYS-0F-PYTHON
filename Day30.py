from collections import Counter
name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
def frequent_name(a):
    return max(Counter(a).most_common())
print(frequent_name(name))

# EXTRA CHALLENGE
names = ['Beyonce knowles', 'Alicia Keys','Katie Perry', 'Chris Brown', 'Tom Cruise']
def sorted_names(list1):
    list2 = []
    for i in list1: 
        list2.append(i.split())
    list3 = []
    # creating a key for the sorted function
    x = lambda x: x[-1]
    for j in sorted(list2, key=x):
# appending sorted names to list3
        list3.append(' '.join([j[-1], j[0]])) 
    return list3
print(sorted_names(names))