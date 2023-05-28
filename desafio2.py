from turtle import *

# uma função para desenhar um planeta de um tamanho específico
def drawPlanet(circleSize, circleColour):
    color(circleColour)
    pendown()
    begin_fill()
    for side in range(360):
        forward(circleSize)
        right(1)
    end_fill()
    penup()

#isso vai desenha um fundo azul escuro
bgcolor("MidnightBlue")

# usando a função para desenhar um circulo e preenche-lo da cor desejada !

drawPlanet(1, "Red")
forward(1)


hideturtle()
done()
