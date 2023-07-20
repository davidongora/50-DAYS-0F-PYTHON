def sum_list(lst1: list):
    counta = 0
    for items in lst1: 
        for i in items: 
            counta += i
    return 'The sum is ', counta 
print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))

# EXTRA CHALLENGE
nested_list = [[12, 34, 56, 67], [34, 68, 78]]
new_list = []
# A nested for loop to access the inner list
for arr in nested_list:
    for num in arr:
        # Create a list of numbers wanted
        if num in [34, 67, 78]:
    # Checking if number already
    # exists before appending
            if num not in new_list:
                new_list.append(num)
print(new_list)