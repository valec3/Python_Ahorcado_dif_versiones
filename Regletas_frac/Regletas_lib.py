import pygame


# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)

# Inicializar Pygame
pygame.init()

# Configurar pantalla
TAMAÑO_PANTALLA = (800, 600)
pantalla = pygame.display.set_mode(TAMAÑO_PANTALLA)
pygame.display.set_caption("REGLETAS FRACCIONARIAS")


# Carga la imagen de fondo
background_image = pygame.image.load('img/bg.png')
background_image = pygame.transform.scale(background_image,TAMAÑO_PANTALLA)

# Dibuja la imagen de fondo en la pantalla
pantalla.blit(background_image, (0, 0))

# Definir fuentes
fuente = pygame.font.Font(None, 36)

# Crear botones
boton_modo_basico = pygame.Rect(50, 50, 200, 50)
boton_modo_avanzado = pygame.Rect(50, 150, 200, 50)

# Dibujar botones en la pantalla
pygame.draw.rect(pantalla, AZUL, boton_modo_basico)
pygame.draw.rect(pantalla, AZUL, boton_modo_avanzado)

# Dibujar texto en los botones
texto_modo_basico = fuente.render("Modo básico", True, BLANCO)
texto_modo_avanzado = fuente.render("Modo avanzado", True, BLANCO)
pantalla.blit(texto_modo_basico, (boton_modo_basico.centerx - texto_modo_basico.get_width() // 2, boton_modo_basico.centery - texto_modo_basico.get_height() // 2))
pantalla.blit(texto_modo_avanzado, (boton_modo_avanzado.centerx - texto_modo_avanzado.get_width() // 2, boton_modo_avanzado.centery - texto_modo_avanzado.get_height() // 2))

imagen = pygame.image.load ( 'img/Regleta1-4.jpg' )
pantalla.blit ( imagen, ( 200, 300 ) )
pantalla.blit ( imagen, ( 280, 300 ) )

# Actualizar pantalla
pygame.display.update()

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Esperar un poco para no usar demasiado CPU
    pygame.time.wait(10)