def all_the_same(a):
    a = all(i == a[0] for i in a) 
    return a
print(all_the_same(['Mary', 'Mary', 'Mary']))

# EXTRA CHALLENGE
str1 = "the love is real"
def read_backwards(n: str) -> str: # Create an empty list
    x = []
    for i in n.split()[::-1]: # Using split to split string on whitespaces
        x.append(i)
    # using the join method to join string
    return ' '.join(x) 
print(read_backwards(str1))

