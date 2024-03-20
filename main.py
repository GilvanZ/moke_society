import pygame
from Mokes.moke import Moke
import random
import os

# Initialize Pygame
pygame.init()
# Set up the screen
screen_width = 1200
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("MOKES")

#Model Moke
#moke_model = Moke("Brian",22,"male","Farmer")
#moke_model.display_info()


# Chamada da função para obter o gênero e nome escolhidos
chosen_gender, chosen_name = Moke.moke_gender()
moke_one= Moke(chosen_name,20,chosen_gender,"estudante",100,500,"stay")
moke_one.display_info()


#moke position
moke_position_x = []
moke_position_y = []

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Fill the screen with white
    screen.fill((30, 150, 40))


    #Tile
    #Size
    TILE_SIZE  = 16
    for x in range(0, screen_width, TILE_SIZE):
        for y in range(0, screen_height, TILE_SIZE):
            pygame.draw.rect(screen, (30, 150, 40), (x, y, TILE_SIZE, TILE_SIZE))


    moke_one.spawn(pygame,screen)
    moke_one.move()
    

    # Update the display
    pygame.display.flip()
# Quit Pygame
pygame.quit()
os.system("cls")
