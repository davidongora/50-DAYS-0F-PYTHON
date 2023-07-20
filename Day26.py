def sort_words(sentence): 
    list1 = []
    sentence = sentence.replace(' ', '') 
    for i in sentence:
        if i not in list1: list1.append(i)
    list1.sort()
    sorted_words = [','.join(list1)]
    return sorted_words
print(sort_words('love life'))

# EXTRA CHALLENGE
s = 'Hi my name is Richard'
def string_length(s: str) -> dict: 
    list1 = []
    dict1 = {}
    # converting string into a list of strings
    for word in s.split():
        list1.append(word)
# update the dictionary with word lengths
    for word in list1:
        d.update({word: len(word)})
    return dict1
print(string_length(s))