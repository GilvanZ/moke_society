import random

class Moke:
    def __init__(self, name, age, gender, occupation):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.favorite_food = self.choose_random_attribute("Mokes\\foods.txt")
        self.favorite_music = self.choose_random_attribute("Mokes\\music.txt")
        self.favorite_color = self.choose_random_attribute("Mokes\\colors.txt")
        self.favorite_hobby0 = self.choose_random_attribute("Mokes\\hobbies.txt")
        self.favorite_hobby1 = self.choose_random_attribute("Mokes\\hobbies.txt")
        self.favorite_hobby2 = self.choose_random_attribute("Mokes\\hobbies.txt")


    def choose_random_attribute(self, file_name):
        with open(file_name, "r") as file:
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

    


    #draw a moke
    def draw(self, pygame, surface, x,y):
        pygame.draw.circle(surface, (100, 2, 25), (x, y), 7)

    def reproduction(self,):
        love = 0
        

# Example usage:
if __name__ == "__main__":
    moke = Moke("John", 30, "Male", "Software Engineer")
    moke.display_info()
