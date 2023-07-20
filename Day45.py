import string
def char(a): 
    special_cha = [] 
    numeric_cha = [] 
    d= {
        'numeric': '', 
        'special_cha': '',
        'total_char': ''
    }
    
    for i in a.replace(' ', ''):
        if i in string.punctuation:
            if i not in special_cha: 
                special_cha.append(i)
            d['special_cha'] = len(special_cha)
        if i in string.digits:
            if i not in numeric_cha:
                numeric_cha.append(i)
            d['numeric'] = len(numeric_cha)
        else:
            d['total_char'] = len(a.replace(' ', '')) 
    return d
print(char('Python has a string format operator %. ' 
           'This functions analogously to '
           'printf format strings in C, e.g.'
           '"spam=%s eggs=%d" % ("blah", 2) '
           'evaluates to "spam=blah eggs=2?'))