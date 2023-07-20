import string
def check_pangram(sentence):
    list1 = []
    alphabet = string.ascii_lowercase
    # removing white spaces in the string
    sentence = sentence.replace(' ', '')
    for i in sentence:
        if i not in list1: 
            list1.append(i)
    list1.sort()
    sentence = ''.join(list1)
    if alphabet == sentence:
        return True
    else:
        return False
print(check_pangram('the quick brown fox ' 'jumps over a lazy dog'))

# EXTRA CHALLENGE
def find_index(arr: list, n: int) -> list:
    list1 = []
    # Using enumerate to find index of integer
    for i, j in enumerate(arr):
        if j == n:
            list1.append(i)
        # If integer not in list
        if n not in arr:
            for j in arr:
                list1.append(n) 
            return list1
    return list1
lst1 = [1, 2, 4, 6, 7, 7]
print(find_index(lst1, 7))
print(find_index(lst1, 8))