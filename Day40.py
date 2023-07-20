def pig_latin(a):
    output = []
    for i, word in enumerate(a.split()):
        if word[0] in 'aeiou': output.append(word[i] + 'yay')
    else:
        output.append(word[1:] + word[0] + 'ay')
    return ' '.join(output)
print(pig_latin('i love python'))