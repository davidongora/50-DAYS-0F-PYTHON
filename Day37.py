def count_vowels(a): 
    vowels = []
    for letter in a:
        if letter in 'AEIOUaeiou':
            if letter not in vowels:
                vowels.append(letter)
    return len(vowels)
print(count_vowels('hello'))