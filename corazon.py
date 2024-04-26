import turtle

# Configuración inicial
turtle.speed(2)
turtle.bgcolor("skyblue")
turtle.pensize(2)

# Función para dibujar un corazón
def draw_heart():
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()

# Dibujo del corazón
draw_heart()

# Esconde la tortuga al finalizar
turtle.hideturtle()

# Mantén la ventana abierta
turtle.done()
