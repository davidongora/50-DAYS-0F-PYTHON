## Day 1: 
    Division and Square-root 
        Write a function called divide_or_square that takes one argument (a number), and returns the square root of the number if it is divisible by 5, returns its remainder if it is not divisible by 5. For example, if you pass 10 as an argument, then your function should return 3.16 as the square root.
import sqrt
def divide_square(num):
  if num % 5 == 0:
    return sqrt(num)
  else:
    remainder = num % 5
    return remainder
 print(divide_square(20)) 

#mathematical operations
#SUBTRACTION
print(9-5)

#MULTIPLICATION
print(7*4)

#Divisiom
print(2*4)

#adding two numbers(integers)
print(1+2)
