import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animación Maravillosa")

# Configuración del círculo
circle_radius = 30
circle_color = (255, 0, 0)  # Rojo
circle_position = [width // 2, height // 2]  # Posición inicial del círculo

# Configuración de la velocidad del círculo
speed = [2, 2]

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar posición del círculo
    circle_position[0] += speed[0]
    circle_position[1] += speed[1]

    # Rebotar cuando alcanza los bordes
    if circle_position[0] + circle_radius > width or circle_position[0] - circle_radius < 0:
        speed[0] = -speed[0]
    if circle_position[1] + circle_radius > height or circle_position[1] - circle_radius < 0:
        speed[1] = -speed[1]

    # Limpiar la pantalla
    screen.fill((255, 255, 255))  # Rellenar la pantalla con blanco

    # Dibujar el círculo
    pygame.draw.circle(screen, circle_color, (int(circle_position[0]), int(circle_position[1])), circle_radius)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de la animación
    pygame.time.Clock().tick(60)
