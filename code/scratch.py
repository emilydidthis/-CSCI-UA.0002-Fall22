width = 40
divider = "-" * width

print(divider)
print(format("Class Grades", "^" + str(width) + "s")) # ^40s
print(divider)

# watch out for integer division!
# dividing by 2 so that they are equal columns
name1 = format("Harry Potter", "<" + str(width//2) + "s") # <20s
grade1 = 81.5

name2 = format("Hermione Granger", "<" + str(width//2) + "s")
grade2 = 99.9

name3 = format("Ron Weasley", "<" + str(width//2) + "s")
grade3 = 61.9

print(name1, end="")
print(grade1)
print(name2, end="")
print(grade2)
print(name3, end="")
print(grade3)

