def your_vat():
    while True:
        try:
            price = int(input("Enter the price of item: "))
            vat = int(input('Enter vat: '))
        except ValueError:
            print("Enter a valid number")
        else:
            total_price = price + \
                        (price * vat / 100 + 1) - 1
        return 'The price VAT inclusive is', total_price
print(your_vat())

# EXTRA CHALLENGE
from emoji import emojize
def Python_snakes(n: int):
# the loop to determine the number of rows of the pyramid
    for i in range(0, n):
# The loop that determines number of columns
        for j in range(n, i, -1):
# print space between the snake signs 
            print(end=" ")
        for k in range(0, i):
# printing the snake emoji
            print(emojize(':snake:'), end=" ")
        print("\n")
money_pyramid(7)