def convert_list(lst1: list):
    list1 = []
    for items in lst1:
        for i in items:
            list1.append(i) 
    return list1
print(convert_list([[2, 4, 5, 6]]))

# EXTRA CHALLENGE
def your_salary():
    name = input('Enter the name of the teacher: ')
    rate = int(input('Enter rate per period: '))
    period = int(input('Enter the number of periods taught: '))
    if period <= 100:
        gross_salary = rate * period
    else:
        gross_salary = (rate * 100)\
                        + ((period-100) * (rate + 5))
    return f'Teacher: {name}, \nPeriods: ' \
           f'{period} \nGross salary:{gross_salary:,}'
print(your_salary())