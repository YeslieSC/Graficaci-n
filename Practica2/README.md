# Practica 2 – Mover una Figura con el Teclado

## Objetivo  
Controlar una figura en pantalla con el teclado

## Compatibilidad  
Este proyecto es compatible con **Python 3.10** y versiones superiores (hasta 3.13)
No requiere instalacion de librerias externas, ya que utiliza únicamente el modulo estandar `turtle`

## Descripción  
El programa abre una ventana grafica donde se dibuja un cuadrado azul en una posicion inicial definida por el usuario
El cuadrado puede moverse en las cuatro direcciones (arriba, abajo, izquierda, derecha) usando las teclas de flechas
Cada vez que se presiona una tecla, el cuadrado se redibuja en su nueva posicion sin dejar rastro, gracias al uso de `pen.clear()` y `screen.tracer(0)`

Los parametros como posicion, tamaño, color y velocidad de movimiento pueden modificarse facilmente en las variables globales del codigo

## Instrucciones para ejecutar el proyecto  
1. Abrir el archivo `practica2_movimientoG_.py` en Visual Studio Code, Thonny o cualquier editor de Python
2. Verificar que Python 3.10 o superior este instalado
3. Ejecutar el archivo con el siguiente comando:

  ```bash python practica2_movimientoG_.py```