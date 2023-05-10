from colores import *
import pygame
pygame.init()


window_size=(800,600)

# Establecer tamaño de la ventana
ventana = pygame.display.set_mode(window_size)
# Para los fps
clock = pygame.time.Clock()

game_over = False

class Player:
    def __init__(self,width,height,x,y,vel=0) -> None:
        self.width=width
        self.height=height
        self.x=x
        self.y=y
        self.velocity=vel

pelota = {"x":400,"y":300,"vel_x":3,"vel_y":3}


Jugador_a = Player(15,90,50,255)
Jugador_b = Player(15,90,750,255)
while not game_over:
    for  event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Jugador_a.velocity = -3
            elif event.key == pygame.K_s:
                Jugador_a.velocity = 3
            elif event.key==pygame.K_q:
                game_over = True
            
            if event.key == pygame.K_UP:
                Jugador_b.velocity = -3
            elif event.key == pygame.K_DOWN:
                Jugador_b.velocity = 3
                
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                Jugador_a.velocity = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                Jugador_b.velocity = 0
    
    if pelota["y"] > window_size[1]-9 or pelota["y"] < 9:
        pelota["vel_y"] *=-1

        
    if pelota["x"]>800 or pelota["x"] < 0:
        pelota["x"]=400
        pelota["y"]=300
        pelota["vel_x"] *=-1
        pelota["vel_y"] *=-1
    # Mover jugadores y pelota
    Jugador_b.y += Jugador_b.velocity 
    Jugador_a.y += Jugador_a.velocity 
    
    pelota["x"] +=pelota["vel_x"] 
    pelota["y"] +=pelota["vel_y"] 
    

    
    # Pintar la venta de azul
    ventana.fill(BLACK)
    # Escribir el titulo del juego
    # Dibujar a los jugadores
    jugadora_cuerpo = pygame.draw.rect(ventana, RED, (Jugador_a.x, Jugador_a.y,Jugador_a.width,Jugador_a.height))
    jugadorb_cuerpo = pygame.draw.rect(ventana, BLUE, (Jugador_b.x, Jugador_b.y ,Jugador_b.width,Jugador_b.height))
    
    # Dibujar pelota
    pelota_cuerpo = pygame.draw.circle(ventana, PINK, (pelota["x"],pelota["y"]),9)
    
    if pelota_cuerpo.colliderect(jugadora_cuerpo) or pelota_cuerpo.colliderect(jugadorb_cuerpo):
        pelota["vel_x"] *=-1
    
    # Actualizar ventana
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
