
# get user input
sales = float(input("Input gross sales: "))
comm_rate = float(input("Input commission rate (i.e. .04): "))

# calculate commission
comm = sales * comm_rate

# output commission
print("You made", "$" + str(comm), "in commissions.")


