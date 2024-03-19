import pygame
import sys
from Mokes.moke import Moke

# Inicialize o Pygame
pygame.init()

# Defina as dimensões da tela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Interagindo com Tiles")

# Defina as dimensões do tile
TILE_SIZE = 16

# Função para converter as coordenadas do mouse para coordenadas de tile
def mouse_to_tile(mouse_pos):
    tile_x = mouse_pos[0] // TILE_SIZE
    tile_y = mouse_pos[1] // TILE_SIZE
    return (tile_x, tile_y)



# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botão esquerdo do mouse
                mouse_pos = pygame.mouse.get_pos()
                tile_pos = mouse_to_tile(mouse_pos)
                print("Mouse sobre o tile:", tile_pos)

    # Limpe a tela
    screen.fill((255, 255, 255))

    # Desenhe uma grade de tiles na tela para visualização
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
        pygame.draw.line(screen, (0, 0, 0), (0, y), (SCREEN_WIDTH, y))

    # Atualize a tela
    pygame.display.flip()

# Encerre o Pygame
pygame.quit()
sys.exit()
