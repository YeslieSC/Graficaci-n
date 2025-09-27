import turtle as t
import os # ayuda al manejo de rutas de archivo

# funciones para dibujar cada figura
def cuadrado(x, y, tamano, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for _ in range(4):
        t.forward(tamano)
        t.right(90)

def triangulo(x, y, tamano, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for _ in range(3):
        t.forward(tamano)
        t.left(120)

def circulo(x, y, radio, color):
    t.penup()
    t.goto(x, y - radio)
    t.pendown()
    t.color(color)
    pasos = 120 
    longitud = (2 * 3.1416 * radio) / pasos
    for _ in range(pasos):
        t.forward(longitud)
        t.left(360 / pasos)

def linea(x1, y1, x2, y2, color):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.color(color)
    t.goto(x2, y2)

def teleport(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# funcion para interpretar y ejecutar cada instruccion
def ejecutar_instruccion(instruccion):
    p = instruccion.strip().split() # divide la funcion en partes segun los espacios 
    if not p or p[0].startswith("#"):
        return

    comando = p[0].upper() # convierte el comando a mayusculas para evitar errores

    # llaman a la funcion correspondiente de cada comando
    try: 
        if comando == "CUADRADO":
            cuadrado(int(p[1]), int(p[2]), int(p[3]), p[4])
        elif comando == "TRIANGULO":
            triangulo(int(p[1]), int(p[2]), int(p[3]), p[4])
        elif comando == "CIRCULO":
            circulo(int(p[1]), int(p[2]), int(p[3]), p[4])
        elif comando == "LINEA":
            linea(int(p[1]), int(p[2]), int(p[3]), int(p[4]), p[5])
        elif comando == "TELEPORT":
            teleport(int(p[1]), int(p[2]))
        else:
            print(f"WARNING: Instruccion desconocida -> {instruccion}") # manejo de comandos no reconocido
    except Exception as e:
        print(f"WARNING: Error en instruccion '{instruccion}' -> {e}") # manejo de errores en la ejecucion de comandos

# funcion principal
def main():
    t.setup(600, 600)
    t.speed(2)
    # ruta del archivo de instrucciones
    base = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(base, "dibujante.txt")
    print("Usando archivo en:", ruta)
    # lee y ejecuta cada instruccion del archivo
    try:
        with open(ruta, "r") as archivo:
            for linea in archivo:
                ejecutar_instruccion(linea)
    except FileNotFoundError:
        print("ERROR: No se encontrO el archivo en la ruta indicada")

    t.done()
    
if __name__ == "__main__":
    main()
