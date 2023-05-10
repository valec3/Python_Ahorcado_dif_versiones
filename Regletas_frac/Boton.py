import pygame

pygame.init()

# Definir el tamaño de la ventana y crear una superficie de pantalla
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Definir el botón como un rectángulo en la pantalla
button_width, button_height = 100, 50
button_x, button_y = 100, 100
button = pygame.Rect(button_x, button_y, button_width, button_height)

# Definir el color original y el color de presionado del botón
button_color = pygame.Color('blue')
button_pressed_color = pygame.Color('darkgray')

# Dibujar el botón en la pantalla
pygame.draw.rect(screen, button_color, button)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                # Cambiar el color del botón al presionarlo
                pygame.draw.rect(screen, button_pressed_color, button)
        if event.type == pygame.MOUSEBUTTONUP:
            # Cambiar el color del botón al soltarlo
            pygame.draw.rect(screen, button_color, button)

    pygame.display.flip()
