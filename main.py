import pygame
from Mokes.moke import Moke
import random
import os
os.system("cls")

# Initialize Pygame
pygame.init()
# Set up the screen
screen_width = 1200
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("MOKES")

#tile
TILE_SIZE = 32

# Call function to get chosen gender and name
chosen_gender, chosen_name = Moke.moke_gender()
#moke_one= Moke(chosen_name,20,chosen_gender,325,800,"stay",pygame,screen)
#moke_one.display_info()

population = {
    'mokes': [],
    'names': []
}

for i in range(10):
    chosen_gender, chosen_name = Moke.moke_gender()
    population['mokes'].append(Moke(chosen_name, random.randint(5, 18), chosen_gender, random.randint(0, 700), random.randint(0, 1180), "stay", pygame, screen,1))
    population['names'].append(chosen_name)
    print(chosen_name)
    
    
#Sprites    
#tiles_sprites_resized = []
# Load and resize each image to 32x32
#for i in range(5):
#    tile = pygame.image.load(f'accets\cenary\grass\grass{i}.png')
#    tile_resized = pygame.transform.scale(tile, (TILE_SIZE, TILE_SIZE))
#    tiles_sprites_resized.append(tile_resized)
#tiles_on_screen = []
#for x in range(0, screen_width, TILE_SIZE):
#    for y in range(0, screen_height, TILE_SIZE):
#        random_tile_index = random.randint(0, 4)
#        tiles_on_screen.append((tiles_sprites_resized[random_tile_index], (x, y)))
        


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Fill the screen with white
    screen.fill((30, 150, 40))
    
    #tiles
    #for tile, position in tiles_on_screen:
    #    screen.blit(tile, position)

    for moke in population['mokes']:
        moke.move()
    
    

    # Update the display
    pygame.display.flip()
# Quit Pygame
pygame.quit()
#os.system("cls")
