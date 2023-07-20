def only_float(a,b):
    if type(a) == float and type(b) == float:
        return 2
    elif type(a) == float or type(b) == float:
        return 1 
    else:
        return 0 
print(only_float(12.1, 23))

# EXTRA CHALLENGE

def word_index(arr: list):
    for word in arr:
        for j in range(len(arr) - 1):
# Checking if the lengths of all the words are equal 
            if len(arr[j]) == len(arr[j + 1]):
                return 0
# Using len function and max to find the longest word 
            elif len(word) == len(max(arr)):
                # using list method index to find
                # index of the longest word
                return f'The longest word is at index: {arr.index(word)}'
words1 = ["Hate", "remorse", "vengeance"] 
words2 = ["Love", "Hate"] 
print(word_index(words1)) 
print(word_index(words2))