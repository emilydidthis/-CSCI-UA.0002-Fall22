# Calculate Half Birthday

month = int(input("What month were you born? (i.e. 2): "))
day = int(input("What day were you born?: "))

# How do I calculate a half birthday?

# Let's find a pattern:
# 2/2 --> 8/2; just add 6
# 10/2 --> 4/2; how do I get 4?

# Need to come up with formula
# (month + 6) % 12

# print("Your half birthday is", (month + 6) % 12, "/", day)
print("Your half birthday is " + str((month + 6) % 12) + "/" + str(day))
