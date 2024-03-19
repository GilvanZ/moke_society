import pygame
from Mokes.moke import Moke
import random
import os

#random int
def rand(val1, val2):
    i = random.randint(val1,val2) 
    return i

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

moke_one_male = Moke("John", 17, "Male", "just a monkey")
moke_one_female = Moke("cassy", 18, "Male", "just a monkey")



# Chamada da função para obter o gênero e nome escolhidos
chosen_gender, chosen_name = Moke.moke_gender()

moke_one= Moke(chosen_name,20,chosen_gender,"estudante")
moke_one.display_info()


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






    # Update the display
    pygame.display.flip()
# Quit Pygame
pygame.quit()
