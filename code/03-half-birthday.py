# Emily Zhao
# Half-Birthday Problem

# Take user inputs
month = int(input("What month were you born in? (i.e. 10): "))
day = int(input("What day were you born in? (i.e. 28): "))


# How do I calculate a half birthday?
# 10/28 --> 4/28
# subtract 6 from month

print("Your half birthday is", month-6, "/", day)
