def just_digits():
    with open('python.csv', 'r') as file:
        a = file.read().split() 
        list1 = []
        for i in a:
            if i.isdigit(): list1.append(i)
    return list1
print(just_digits())

# EXTRA CHALLENGE
