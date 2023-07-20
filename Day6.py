def user_name ():
    your_email = input("Enter your email")
    user_name = your_email.split('@')[0]
    return f'You user name is {user_name}'
print(user_name())

# EXTRA CHALLENGE

list1 = [2, 5, 7, 8, 9]
def zeroed(arr: list) -> list:
# Access and modify the first element arr[0] = 0
# Access and modify the last element arr[-1] = 0
    return arr
print(zeroed(list1))