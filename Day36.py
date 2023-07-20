def count(a):
    d = {}
    for i in range(len(a)):
        x = a[i]
        count = 0
        for j in range(i, len(a)):
            if a[j] == a[i]: count = count + 1
        countz = dict({x: count}) 
# updating the dictionary 
        if x not in d.keys():
            d.update(countz) 
    return d
print(count('hello'))   