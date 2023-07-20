def count_words(arr: str):
    words = []
    for word in arr.split():
        words.append(word) 
        print(words)
    return f'There are {len(words)} ' \
           f'words in the sentence'
print(count_words('I love learning'))

# EXTRA CHALLENGE
def count_characters(a):
    a = a.replace(' ', '')
    return f'The string has ' \
           f'{len(a)} elements '
print(count_characters('I love learning'))