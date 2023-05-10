import pygame
import sys
import random
# Importar colores
from colores import *

# Iniciar libreria pygame
pygame.init()

# Tamaño de la ventana
ventana_size = (800 , 500)

# Crear ventana
ventana = pygame.display.set_mode(ventana_size)

# Reloj para pausar y controlar FPS
reloj = pygame.time.Clock()
# --------------------------------------------------------------------
class Particulas:
    cords_puntos=[]
    for i in range(60):
            x = random.randint(0,ventana_size[0])
            y = random.randint(0,ventana_size[1])
            cords_puntos.append([ x , y ])


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()

    ventana.fill(WHITE)
    # Dibujar circulos
    puntos=Particulas()
    for punto in puntos.cords_puntos:
        x = punto[0]
        y = punto[1]
        pygame.draw.circle(ventana,RED, (x, y), 2)
        punto[1] +=4
        if punto[1] > ventana_size[1]:
            punto[1] = 0

    
    pygame.display.flip()
    reloj.tick(15)