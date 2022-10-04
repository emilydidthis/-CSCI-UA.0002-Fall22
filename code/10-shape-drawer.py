import random
import turtle

width = 100

print("How many sides would you like your shape to be?")
answer = input("Input a number between 3-9 or \
type 'random' if you want to be surprised: ")

if answer == "random":
    sides = random.randint(3,9)
else:
    sides = int(answer)

#print(sides)

selection = input("Would you like a visual (v) or textual (t) \
description of your shape?")

if selection == "t":
    if sides == 3:
        print("Your shape is a triangle.")
    elif sides == 4:
        print("Your shape is a quadrilateral.")
    elif sides == 5:
        print("Your shape is a pentagon.")
    elif sides == 6:
        print("Your shape is a hexagon.")
    elif sides == 7:
        print("Your shape is a septagon.")
    elif sides == 8:
        print("Your shape is a octagon.")
else:
    turtle.setup(500,500)

    turtle.penup()
    turtle.goto(-100, 100)
    turtle.pendown()

    for side in range(sides):
        angle = 360/sides
        turtle.forward(100)
        turtle.right(angle)
    
        
        

    
    
