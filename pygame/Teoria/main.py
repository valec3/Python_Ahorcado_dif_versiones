import pygame
import sys
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



cord_x = 100
velocidad_x=5
while True:
    for evento in pygame.event.get():
        # Verificar si se ha cerrado la pantalla
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Poner color de fondo
    ventana.fill(BLUE)
    
    if cord_x > 800-50 or cord_x < 0:
        velocidad_x *=-1
    cord_x += velocidad_x
    pygame.draw.rect(ventana, RED, (cord_x,240,50,50))
    
    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(60)