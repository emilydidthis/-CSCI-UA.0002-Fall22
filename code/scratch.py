# Calculating a Bonus

# initialize my variables
bonus = 0
percent = 0.01

# ask for a sales amount
sales = int(input("Enter monthly sales:"))

# over 10,000 --> 500 bonus
if sales >= 10000:
    print("You made the quota")
    bonus = 500 #update bonus

if sales >= 50000:
    percent = 0.05 #percent

# calculate commission:
commission = sales * percent

print("Your total take home will be $" + \
      str(sales + bonus + commission))



    
