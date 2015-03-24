import turtle               # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("lightblue")
window.title("Forca")

n = 360
dist = 0.5
angulo = 180-((n-2)*180/n)

turtle.setpos(0,200)
turtle.setpos(100,200)
turtle.setpos(100,100)
turtle.penup

for i in range(360):
    turtle.left(angulo)  # Vira o angulo pedido
    turtle.forward(dist) # Avança a distancia pedida

turtle.setpos(100,100)
turtle.setpos(100,50)
turtle.setpos(50,50)
turtle.setpos(150,50)
turtle.setpos(100,50)
turtle.setpos(100,00)
turtle.setpos(50,-40)
turtle.setpos(100,0)
turtle.setpos(150,-40)


window.exitonclick()

