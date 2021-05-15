# Write your code here :-)
from turtle import Turtle
from random import randint

# Instance of turtle
laura = Turtle()
rik = Turtle()
lauren = Turtle()
svenja = Turtle()


laura.color('red')
laura.shape("turtle")
rik.shape("turtle")
lauren.shape("turtle")
svenja.shape("turtle")

# Instruction for the turtle
laura.penup()
laura.goto(-160,100)
laura.pendown()


rik.color('blue')
lauren.color('green')
svenja.color('pink')


rik.penup()
rik.goto(-160,70)
rik.pendown()

lauren.penup()
lauren.goto(-160,40)
lauren.pendown()

svenja.penup()
svenja.goto(-160,10)
svenja.pendown()

# Turtles to move forward
for movement in range(100):
    laura.forward(randint(1,5))
    rik.forward(randint(1,5))
    lauren.forward(randint(1,5))
    svenja.forward(randint(1,5))

input("Press Enter to close")
