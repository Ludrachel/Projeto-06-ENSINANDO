from turtle import *

# definindo e usando uma função

def drawRectangle():
    pendown()
    begin_fill()
    for side in range(3):
        left(90)
        forward(50)
    end_fill()
    penup()

#isso vai desenhar um quadrado cinza em um fundo azul escuro
color("WhiteSmoke")
bgcolor("MidnightBlue")

# usando a função para desenhar dois quadrados e formar um retângulo!

drawRectangle()
forward(50)
drawRectangle()
left(90)
forward(50)

hideturtle()
done()
