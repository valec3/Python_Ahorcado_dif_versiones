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

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
    posicion_mouse = pygame.mouse.get_pos()
    ventana.fill(WHITE)
    x,y = posicion_mouse
    pygame.draw.rect(ventana,RED,(x,y,50,50))
    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(15)