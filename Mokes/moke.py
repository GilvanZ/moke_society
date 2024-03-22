import random
import pygame

class Moke:
    def __init__(self, name, age, gender, y, x, move_direction, pygame, surface, speed=0.5,):
        self.pygame = pygame
        self.surface = surface
        self.speed = speed
        self.move_direction = move_direction
        self.y = y
        self.x = x
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = self.choose_random_attribute("Mokes\occupation.txt")
        self.favorite_food = self.choose_random_attribute("Mokes\\foods.txt")
        self.favorite_music = self.choose_random_attribute("Mokes\\music.txt")
        self.favorite_color = self.choose_random_attribute("Mokes\\colors.txt")
        self.favorite_hobby0 = self.choose_random_attribute("Mokes\\hobbies.txt")
        self.favorite_hobby1 = self.choose_random_attribute("Mokes\\hobbies.txt")
        self.favorite_hobby2 = self.choose_random_attribute("Mokes\\hobbies.txt")
        self.fonte = pygame.font.Font(None,15)
        self.screen_width = 1200
        self.screen_height = 720
        self.life = 100
        self.hungry = 100


    def choose_random_attribute(self, file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            attributes = [line.strip() for line in file]
            return random.choice(attributes)

    #get moke names
    #get moke gender
    def moke_gender():
        moke_genders = ["male", "female"]
        gender_choose = random.choice(moke_genders)
        if gender_choose == "male":
            with open("moke_names/male.txt", "r") as file:
                attributes = [line.strip() for line in file]
                return "male", random.choice(attributes)
        else:
            with open("moke_names/female.txt", "r") as file:
                attributes = [line.strip() for line in file]
                return "female", random.choice(attributes)
    chosen_gender, chosen_name = moke_gender()

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Occupation: {self.occupation}")
        print(f"Favorite food: {self.favorite_food}")
        print(f"Favorite music: {self.favorite_music}")
        print(f"Favorite color: {self.favorite_color}")
        print(f"Favorite hobby: {self.favorite_hobby0}, {self.favorite_hobby1} e {self.favorite_hobby2}")

    #spawn a moke
    def move(self):
        sprite_speed = 15
        # Verifica se o macaco precisa mudar de direção
        if random.randint(1, 500) == 1 or not self.move_direction:
            self.move_direction = random.choice(["up", "down", "left", "right", "stay"])

        # Move o moke na direção atual
        if self.move_direction == "up":
            self.y -= self.speed
            sprite = []
            for i in range(5):
                sprite.append(self.pygame.image.load(f'accets\walk_left\wlk{i}.png'))

            # Controles de animação
            if not hasattr(self, "clock"):
                self.clock = 0
            if not hasattr(self, "sprite_index"):
                self.sprite_index = random.randint(0,len(sprite)-1)

            # Atualiza o índice do sprite
            if self.clock >= sprite_speed:
                self.sprite_index = random.randint(0,len(sprite)-1)
                self.clock = 0
            self.clock += 1
            # Desenha o sprite atual na tela
            self.surface.blit(sprite[self.sprite_index-1], (self.x, self.y))

        elif self.move_direction == "down":
            self.y += self.speed
            sprite = []
            for i in range(5):
                sprite.append(self.pygame.image.load(f'accets\walk_right\wlk{i}.png'))

            # Controles de animação
            if not hasattr(self, "clock"):
                self.clock = 0
            if not hasattr(self, "sprite_index"):
                self.sprite_index = random.randint(0,len(sprite)-1)

            # Atualiza o índice do sprite
            if self.clock >= sprite_speed:
                self.sprite_index = random.randint(0,len(sprite)-1)
                self.clock = 0
            self.clock += 1
            # Desenha o sprite atual na tela
            self.surface.blit(sprite[self.sprite_index-1], (self.x, self.y))
                
            
        elif self.move_direction == "left":
            self.x -= self.speed
            sprite = []
            for i in range(5):
                sprite.append(self.pygame.image.load(f'accets\walk_left\wlk{i}.png'))

            # Controles de animação
            if not hasattr(self, "clock"):
                self.clock = 0
            if not hasattr(self, "sprite_index"):
                self.sprite_index = random.randint(0,len(sprite)-1)

            # Atualiza o índice do sprite
            if self.clock >= sprite_speed:
                self.sprite_index = random.randint(0,len(sprite)-1)
                self.clock = 0
            self.clock += 1
            # Desenha o sprite atual na tela
            self.surface.blit(sprite[self.sprite_index-1], (self.x, self.y))
                
            
            
        elif self.move_direction == "right":
            self.x += self.speed
            sprite = []
            for i in range(5):
                sprite.append(self.pygame.image.load(f'accets\walk_right\wlk{i}.png'))

            if not hasattr(self, "clock"):
                self.clock = 0
            if not hasattr(self, "sprite_index"):
                self.sprite_index = random.randint(0, len(sprite) - 1)

            # Atualiza o índice do sprite
            if self.clock >= sprite_speed:
                self.sprite_index = random.randint(0,len(sprite)-1)
                self.clock = 0
            self.clock += 1
            # Desenha o sprite atual na tela
            self.surface.blit(sprite[self.sprite_index-1], (self.x, self.y))
            
            
        elif self.move_direction == "stay":
            #sprites
            sprite = []
            for i in range(6):
                sprite.append(self.pygame.image.load(f'accets\\stay\\sty{i}.png'))

            # Controles de animação
            if not hasattr(self, "clock"):
                self.clock = 0
            if not hasattr(self, "sprite_index"):
                self.sprite_index = random.randint(0,len(sprite)-1)

            # Atualiza o índice do sprite
            if self.clock == 600 or self.clock == random.randint(150,690):
                self.sprite_index = random.randint(0,len(sprite)-1)
                self.clock = 0
            self.clock += 1
                # Desenha o sprite atual na tela
            self.surface.blit(sprite[self.sprite_index-1], (self.x, self.y))
            
            
        #stay only in border
        if self.y <= 25:
            self.move_direction = random.choice(["down", "left", "right", "stay"])
        elif self.y >= 720-25:
            self.move_direction = random.choice(["up", "left", "right", "stay"])
        elif self.x <= 25:
            self.move_direction = random.choice(["up", "down", "right", "stay"])
        elif self.x >= 1200-25:
            self.move_direction = random.choice(["up", "down", "left", "stay"])
    def GUIscrren(self):
        #Dower
        dower = pygame.transform.scale(self.pygame.image.load(f'accets\GUI\GUIdown.png'),(1200,50))
        self.surface.blit(dower,(0,680))
        #Upper
        upper = pygame.transform.scale(self.pygame.image.load(f'accets\GUI\GUIupper.png'),(1200,50))
        self.surface.blit(upper,(0,0))
    
    def status(self):
        #GUI base
        gui_x, gui_y = 350, 100
        base = pygame.transform.scale(self.pygame.image.load(f'accets\GUI\status_base1.png'), (500, 500))
        self.surface.blit(base,(gui_x,gui_y))
        
        #name
        text_name = self.fonte.render(self.name, True, (0,0,0,200))
        self.surface.blit(text_name, (gui_x+230,gui_y+20))
        
        #ocupation
        text_occupation = self.fonte.render(self.occupation, True, (0,0,0,200))
        self.surface.blit(text_occupation, (gui_x+2,gui_y+15))
        
        #Hobbye
        text_hobbye0 = self.fonte.render(self.favorite_hobby0, True, (0,0,0,200))
        self.surface.blit(text_hobbye0, (gui_x+2,gui_y+25))
        
        #life
        bar_base = 350
        status_bar = pygame.transform.scale(pygame.image.load(f'accets\GUI\statusbar.png'),(bar_base,40))
        self.surface.blit(status_bar, (gui_x+70,gui_y+100))
        
        progression_bar = pygame.transform.scale(pygame.image.load(f'accets\GUI\statusprogress.png'),(bar_base-10,29))
        self.surface.blit(progression_bar, (gui_x+76,gui_y+105))
        
        
        