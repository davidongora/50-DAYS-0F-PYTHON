def odd_even(a):
    even = []
    odd = [] 
    for i in a:
        if i % 2 ==0: 
            even.append(i)
        if i % 2 != 0: 
            odd.append(i)
    return max(even) - min(odd)
print(odd_even([1,2,4,6]))

# EXTRA CHALLENGE
def prime_numbers() -> list: 
    prime_num = []
    n = int(input('Please enter a number (integer): ')) # Creating a range of the input number
# remember to add a 1 and the end ensure
# all numbers in the range are covered
    for i in range(0, n + 1):
         # only numbers above 1 are needed
        if i > 1:
            for j in range(2, i):
# if a number in the range is divisible by j
          # Then number is not prime
                if i % j == 0:
                    break
            else:
                prime_num.append(i)
    return prime_num
print(prime_numbers())