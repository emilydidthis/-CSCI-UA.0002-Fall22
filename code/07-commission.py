# Calculating comissionsn for 3 people

# control variable
calculate_comms = "yes"

while calculate_comms == "yes": 
    # get user input
    sales = float(input("Input gross sales: "))
    comm_rate = float(input("Input commission rate (i.e. .04): "))

    # calculate commission
    comm = sales * comm_rate

    # output commission
    print("You made", "$" + str(comm), "in commissions.")

    # ask user if they want to continue
    calculate_comms = input("Do you want to continue? Type yes or no: ")

print("Thank you for using our program!")



