# modulo tortuga 
import turtle as t

# funciones para dibijar cada figura

# funcion para el cuadrado
# se piden los parametros que debe dar el usuario

# los parametros son: posicion x, posicion y, tamaño del lado y color
# penup() sirve para que no dibuje lineas al moverse
# goto(x, y) es el punto de donde se comienza a dibujar
# pendow() es para que comience a dibujar
# color() define su color
def cuadrado(x, y, tamano, color):
    t.penup() 
    t.goto(x, y)
    t.pendown()
    t.color(color)
# repite los lados de la figura segun sean necesarias para formarla
    for _ in range(4):
        t.forward(tamano)
        t.right(90)
# forward() es la cantidad de pixeles que avanzara antes de hacer la otra figura
# right() son los grados que gira para formar la figura

# funcion para el triangulo
def triangulo(x, y, tamano, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for _ in range(3):
        t.forward(tamano)
        t.left(120)

# funcion para el circulo
def circulo(x, y, radio, color):
    t.penup()
    t.goto(x, y - radio)
    t.pendown()
    t.color(color)
    pasos = 120 
# los pasos definen que tan redondo se vera el circulo
    longitud = (2 * 3.1416 * radio) / pasos
# define que tan largos son los pasos
    for _ in range(pasos):
        t.forward(longitud)
        t.left(360 / pasos)

# funcion para dibujar una linea recta
def linea(x1, y1, x2, y2, color):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.color(color)
    t.goto(x2, y2)

# configuracion inicial de la tortuga
# velocidad al dibujar
t.speed(2)

# llamar las funciones para dibujar las figuras
cuadrado(-200, 20, 60, "#0000FF")
triangulo(-80, 40, 80, "#FFA500")
circulo(80, 0, 40, "#FF0000")
linea(160, 0, 260, 0, "#000000")

t.done()