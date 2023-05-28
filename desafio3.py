from turtle import *
from random import *

def moveToRandomLocation():
    penup()
    setpos( randint(-400,400) , randint(-400,400) )
    pendown()

def drawSquare(drawTriangle, squareColour):
    color(squareColour)
    pendown()
    begin_fill()
    for side in range(4):
        left(100)
        forward(drawTriangle)
    end_fill()
    penup()

bgcolor("MidnightBlue")

for square in range(20):
    moveToRandomLocation()
    drawSquare( randint(5,25) , "Red")
    forward(100)
    drawSquare( randint(5,25) , "yellow")
    left(120)
    drawSquare( randint(5,25) , "Green")
    forward(70)
    drawSquare( randint(5,25) , "Pink")
    left(90)
    forward(120)
    drawSquare( randint(5,25) , "Black")
    left(120)

hideturtle()
done()
