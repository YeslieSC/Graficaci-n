# Practica – Colisiones

## Objetivo
Resolver Colisiones Laterales

## Descripcion
Un juego sencillo en 2D donde un jugador puede moverse, saltar sobre plataformas y evitar enemigos
Se utiliza la libreria **Pygame**
El juego incluye un sistema de puntuacion que incrementa con el tiempo

## Estructura del proyecto
- Se inicializa la ventana de juego con dimensiones fijas (900x500)
- Se definen colores en estilo neon para la estetica del juego
- El jugador se representa con un rectangulo (`pygame.Rect`) y se controla con las teclas de direccion y espacio para saltar
- Se implementa la gravedad y la deteccion de colisiones en los ejes horizontal y vertical
- Se definen plataformas estaticas y paredes laterales
- Los enemigos se mueven horizontalmente y terminan la partida al colisionar con el jugador
- Se muestra en pantalla la puntuacion acumulada

## Manejo de errores
- Se imprimen mensajes en consola cuando ocurren colisiones (horizontal o vertical)

## Solucion al problema de colisiones
El jugador atravesaba los bordes de la pantalla porque las paredes laterales estaban definidas con **ancho 0**, lo que en Pygame significa que el rectangulo no existe fisicamente.  

El codigo original era:
pygame.Rect(0, 10, 0, 500)      # pared izquierda (incorrecto)
pygame.Rect(897, 10, 0, 500)    # pared derecha (incorrecto)

La solución fue darles un grosor real 
Use 10 píxeles porque:
- Es un valor pequeño que no afecta la jugabilidad ni reduce el espacio visible
- Es suficiente para que el rectangulo exista y Pygame pueda detectar la colision
- Mantiene simetria en ambos lados de la ventana

Codigo corregido:
pygame.Rect(0, 0, 10, 500),          # pared izquierda
pygame.Rect(900-10, 0, 10, 500),     # pared derecha

## Requisitos
- Python 3.10
- Libreria externa: Pygame (se instala con pip install pygame)
