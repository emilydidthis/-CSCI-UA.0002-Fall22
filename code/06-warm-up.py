# Warmup Problem

# import random

# generating random numbers
num1 = random.randint(1, 9)
num2 = random.randint(1, 9)
# calculating the product
product = num1 * num2


print("Let's test your multiplication skills!")
answer = int(input("What is " + str(num1) + "*" + str(num2) + "?"))

if answer == product:
    print("You guessed correctly!")
else:
    print("You guessed incorrectly.") 


