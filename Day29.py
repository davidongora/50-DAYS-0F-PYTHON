def middle_figure(a: str,b: str): 
    c = (a + b).replace(' ','') 
    print(c)
    b = len(c)
    middle = b//2
    if len(c)% 2 == 1:
        return c[middle]
    else:
        return 'No middle figure' 
print(middle_figure('make love', 'not wars'))

