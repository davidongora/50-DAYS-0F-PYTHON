def make_tuples(a,b):
    a = zip(a,b)
    return list(tuple(a))
print(make_tuples([1,2,3,4],[5,6,7,8]))

# EXTRA CHALLENGE
def even_or_average():
    avg_num = []
    even_number = []
    # Using while loop to ensure code keeps running
    while True:
        number = input("Please enter numbers or done: ")
        avg_num.append(int(number))
        if int(number) % 2 == 0:
            even_number.append(number)
            # Once the user inputs five numbers the code breaks
        if len(avg_num) == 5:
            break
    if len(even_number) > 0: # checking if list empty
        return f'The largest even number: {max(even_number)}'
    else:
        return f'The average is : {sum(avg_num) / len(avg_num):.2f}'
print(even_or_average())