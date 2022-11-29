#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = str(number)
j = len(n)
t = n[j-1]
x = int(t)
if number < 0:
    x = -x
print("Last digit of", end=" ")
if x > 5:
    print(f"{number} is {x} and is greater than 5")
elif x == 0:
    print(f"{number} is {x} and is 0")
elif x < 6 and t != 0:
    print(f"{number} is {x} and is less than 6 and not 0")
