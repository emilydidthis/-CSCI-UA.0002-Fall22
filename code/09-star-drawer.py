
while True:
    # keep asking for num1 input
    num1 = int(input("Number 1: "))
    if num1 <= 0:
        print("Invalid, try again") # ask again
    else: # num1 input is valid
        while True: # start another loop for num2 input
            # keep asking for num2
            num2 = int(input("Number 2: "))
            # num2 needs to be positive and greater than num1
            if num2 <= 0 or num2 < num1: 
                print("Invalid, try again")
            else:
                break #num2 is good, get out of the loop
        break #num1 is good, get out of the loop

# set counter equal to first number
counter = num1 

# print first part of triangle
while counter <= num2:
    print(counter, "*" * counter)
    counter += 1
# counter is going to be 1 more than num2
# we don't want to print another row of num2, so subtract 2

counter -= 2

# print second part of triangle
while counter >= num1:
    print(counter, "*" * counter)
    counter -= 1
    
           
