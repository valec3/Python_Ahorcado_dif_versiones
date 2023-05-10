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
#____________________________________________________________

# Ocultar mouse
pygame.mouse.set_visible(0)
x,y=10,10
v_x,v_y=0,0
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                v_x = -3
            if evento.key == pygame.K_RIGHT:
                v_x = 3
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                v_x = 0
            if evento.key == pygame.K_RIGHT:
                v_x = 0
    ventana.fill(BLACK)
    x += v_x 
    pygame.draw.rect(ventana,RED,(x,y,50,50))
    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(15)