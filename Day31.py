def longest_word(a):
    b =[]
    for word in a:
        b.append([len(word), word]) 
    return max(b)
print(longest_word(['Java','Javascript','Python']))


# EXTRA CHALLENGE
def create_user():
    d = {} # create an empty dictionary
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    password = input("Enter your password: ")
    # Updating the di   ionary using update method.
    d.update({'name': name})
    d.update({'age': age})
    d.update({'password': password})
    print("User saved   Please login")
# using while loo   to ensure the code runs
    # until user    ters correct login details
    while True: 
        user_name = input("Please enter your user name to login") 
        password = input("Please enter your password")
        if user_name == d.get('name') and password == d.get('password'):
            return "Logged in successfully"
        else:
            print('Wrong password or user_name please try again')
print(create_user())