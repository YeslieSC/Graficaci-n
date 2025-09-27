# PrActica 4 – Archivo Instrucciones

## Objetivo
Leer el contendio de un archivo para evaluar y ejecutar las instrucciones en el plano de dibujo de turtle

## Descripcion del proyecto
Este proyecto implementa un interprete de instrucciones en Python que lee un archivo de texto y ejecuta comandos graficos 
usando la libreria estandar turtle. 

## Estructura del proyecto
Se utilizo el modulo turtle para el dibujo grafico y el modulo os para la gestion de archivos
Se uso import os para verificar la existencia del archivo de instrucciones
Se definieron las figuras geometricas como funciones
Se implemento el interprete que lee y ejecuta las instrucciones del archivo

## Manejo de errores
Si una instruccion es invalida se muestra un **WARNING** en consola y el programa continua con la siguiente
Si el archivo `dibujante.txt` no se encuentra se muestra un **ERROR** en consola

## Instrucciones soportadas
El archivo `dibujante.txt` debe contener una instruccion por linea
Las instrucciones válidas son:
- `CUADRADO x y tamaño color`
- `TRIANGULO x y tamaño color`
- `CIRCULO x y radio color`
- `LINEA x1 y1 x2 y2 color`
- `TELEPORT x y`

## ?? Requisitos
- Python 3.10 
- No requiere librerias externas, solo modulos estandar (`turtle`, `os`)