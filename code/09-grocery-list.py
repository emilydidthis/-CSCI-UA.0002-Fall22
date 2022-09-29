
# accumulator variables
total_cost = 0
minimum = 0.00
maximum = 0.00
number_of_items = 0
all_items = ""

# create a loop that keeps going until a sentinel is typed
while True:
    item_name = input("Enter an item's name (or type 'end'): ") # ask for item name
    if item_name == "end": # set sentinel aka when do I stop?
        break
    item_price = float(input("Enter an item's price: ")) # ask for price
    if number_of_items == 0: # set first item equal to both min and max
        maximum = item_price
        minimum = item_price
    if item_price > maximum: # check and update max
        maximum = item_price
    if item_price < minimum: # check and update min
        minimum = item_price
        
    # update accumulator variables
    total_cost += item_price
    all_items += item_name + " "
    number_of_items += 1

print("You purchased:", all_items, sep=",")
print("Total price:", total_cost)
print("Most expensive price:", maximum)
print("Lease expensive price:", minimum)


