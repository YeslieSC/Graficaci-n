# modulo tortuga
import turtle as t

screen = t.Screen()
# con tracer(0) se desactiva el dibujo automatico
screen.tracer(0)

# con visible=False se oculta la tortuga para tener una mejor vista
pen = t.Turtle(visible=False)

# estos parametros permiten modificar la posicion y apariencia del cuadrado.
x, y = 0, 0
lado = 60
color = "#0000FF"
paso = 16

# se define el cuadrado 
def cuadrado(x, y, tamano, color):
    pen.clear()      # borra lo dibujado previamente por esta tortuga
    pen.penup()      # con pen.penup el cuadrado no dejara rastro al moverse
    pen.goto(x, y)   # mueve a la tortuga a la posicion indicada anteriormente
    pen.pendown()    # se encarga de que el dibujo este visible
    pen.color(color) # define el color del cuadrado
# asigna los lados de la figura para formarla 
    for _ in range(4):
        pen.forward(tamano)
        pen.right(90)
pen.penup()

# esta funcion refresca la pantalla cada vez que se mueve el cuadrado
def actualizar():
    cuadrado(x, y, lado, color)
    screen.update()

# funciones para mover el cuadrado en las 4 direcciones
def izquierda():
    global x
    x -= paso
    actualizar()

def derecha():
    global x
    x += paso
    actualizar()

def arriba():
    global y
    y += paso
    actualizar()

def abajo():
    global y
    y -= paso
    actualizar()

# asocia las teclas de flechas con las funciones de movimiento
screen.onkeypress(izquierda, "Left")
screen.onkeypress(derecha, "Right")
screen.onkeypress(arriba, "Up")
screen.onkeypress(abajo, "Down")

# permite que la pantalla escuche las teclas presionadas
screen.listen()
actualizar()
screen.mainloop()