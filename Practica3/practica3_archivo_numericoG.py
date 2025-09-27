import random      # esta libreria permitira generar numeros aleatorios
import turtle as t # modulo tortuga 
# asignacion de color a caada numero
colores = {
    "0": "#000000",
    "1": "#FF0000",
    "2": "#00FF00",
    "3": "#0000FF",
    "4": "#FFFF00",
    "5": "#FFA500",
    "6": "#800080",
    "7": "#00FFFF",
    "8": "#FF00FF",
    "9": "#8B4513" 
}
# se define el archivo donde se guardara la matriz de numeros y la dimension que tendra
archivo = "matriz.txt"
filas, columnas = 100, 100

# se genera el archivo con la matriz
# con ayuda de la IA Copilot se diseño este bloque para generar automaticamente el archivo matriz.txt
# esto garantiza que el archivo se cree y se cierre al finalizar
with open(archivo, "w", encoding="utf-8") as f:
    for _ in range(filas):
        linea = "".join(str(random.randint(0, 9)) for _ in range(columnas))
        f.write(linea + "\n")

# se lee el archivo y se guarda la matriz en una lista de listas
matriz = []
with open(archivo, "r", encoding="utf-8") as f:
    for linea in f:
        matriz.append(list(linea.strip()))

# configuracion inicial de la tortuga
t.speed(0)
t.hideturtle()  # oculta la flecha de la tortuga
t.tracer(False) # desactiva la animacion paso a paso para dibujar mas rapido

# parametros para el dibujo
pixel = 5
inicio_x = - (len(matriz[0]) * pixel) // 2
inicio_y = (len(matriz) * pixel) // 2

# indicaciones para dibujar la matriz
# la tortuga se mueve a la posicion correspondiente en pantalla calculando las coordenadas X y Y
for i, fila in enumerate(matriz):
    for j, valor in enumerate(fila):
        t.penup()
        t.goto(inicio_x + j * pixel, inicio_y - i * pixel)
        t.pendown()
        t.fillcolor(colores.get(valor, "#FFF"))
        t.begin_fill()
        for _ in range(4):
            t.forward(pixel)
            t.right(90)
        t.end_fill()
t.update() # actualiza la pantalla con el dibujo completo
t.done()