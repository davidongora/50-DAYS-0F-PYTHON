import random
random_number = random.randint(0,10)
def guess_number():
    c=0
    while c < 4:
        guess = int(input("Guess a number "
                          "between 1 and 10: "))
        c += 1
        if c == 3:
            print("You have run out of guesses. " "You lose")
            break
        elif guess > random_number:
            print('Your guess is too high. ' 'Try again')
        elif guess < random_number: print('Your guess is too low. '
'Try again')
        else:
            return 'Correct. You win'
    return ''
print(guess_number())

# EXTRA CHALLENGE
list3 = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]
def missing_numbers(arr: list) -> list:
    missing_numz = []
# find the missing numbers using range
    for i in range(arr[0], arr[-1] + 1):
        if i not in arr:
            missing_numz.append(i)
    return missing_numz
print(missing_numbers(list3))