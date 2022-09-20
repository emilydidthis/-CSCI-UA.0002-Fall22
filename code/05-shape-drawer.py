import random
import turtle

width = 100

print("How many sides would you like your shape to be?")
answer = input("Input a number between 3-5 or \
type 'random' if you want to be surprised: ")

if answer == "random":
    sides = random.randint(3,5)
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
else:
    turtle.setup(500,500)

    turtle.penup()
    turtle.goto(-200, 200)
    turtle.pendown()

    if sides == 3:
        # now draw a triangle
        turtle.forward(100)
        turtle.right(120)
        turtle.forward(100)
        turtle.right(120)
        turtle.forward(100)
        turtle.right(120)
    elif sides == 4:
        # draw a square here
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
    else:
        # draw the pentagon
        turtle.forward(100)
        turtle.right(360/5)
        turtle.forward(100)
        turtle.right(360/5)
        turtle.forward(100)
        turtle.right(360/5)
        turtle.forward(100)
        turtle.right(360/5)
        turtle.forward(100)
        turtle.right(360/5)

        
        

    
    
