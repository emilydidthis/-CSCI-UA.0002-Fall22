# Adding Machine

# initialize total variable
total = 0

while True:
    num = int(input("Input an integer to add (enter 0 to end program): "))

    # condition for sentinel to break out of loop
    if num == 0:
        break

    # if we are still running, add num to a grand total
    # total = total + num
    total += num
    print(total)

print("Your total is: ", total)
print("Thank you for using our program.")
    
