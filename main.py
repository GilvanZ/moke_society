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

# Chamada da função para obter o gênero e nome escolhidos
chosen_gender, chosen_name = Moke.moke_gender()
moke_one= Moke(chosen_name,20,chosen_gender,325,800,"stay",pygame,screen)
moke_one.display_info()

population = {
    'mokes': [],
    'names': []
}

for i in range(10):
    chosen_gender, chosen_name = Moke.moke_gender()
    population['mokes'].append(Moke(chosen_name, random.randint(5, 18), chosen_gender, random.randint(0, 700), random.randint(0, 1180), "stay", pygame, screen,1))
    population['names'].append(chosen_name)
    print(chosen_name)
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

    for moke in population['mokes']:
        moke.move(screen)
        
    
    

    # Update the display
    pygame.display.flip()
# Quit Pygame
pygame.quit()
#os.system("cls")
