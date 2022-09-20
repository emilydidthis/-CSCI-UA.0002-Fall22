# What if I changed my mind and wanted it to be
# 80 long or 20 long


width = 80

print("-" * width)
print(format("Class Grades", "^" + str(width) + "s"))
# ^ [variable] s
# "^" + str(width/2) + "s"
print("-" * width)

name1 = "Harry Potter"
grade1 = 89.9
name2 = "Hermione Granger"
grade2 = 99.9
name3 = "Ron Weasley"
grade3 = 67.8


print(format(name1, "<" + str(width//3) + "s"), end="")
print(grade1)
print(format(name2, "<" + str(width//3) + "s"), end="")
print(grade2)
print(format(name3, "<" + str(width//3) + "s"), end="")
print(grade3)
