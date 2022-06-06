import random
from pet import Pet

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        print(f"Walking {self.pet.name}!")
        self.pet.play()
        return self

    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        if len(self.pet_food) == 0:
            print("Oh no!! You need more pet food!")
        else:
            cur_idx = random.randint(0, len(self.pet_food) - 1)
            cur_pet_food = self.pet_food.pop(cur_idx)
            print(f"Feeding {self.pet.name} {cur_pet_food}!")
            self.pet.eat()
        return self

    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        print(f"Bathing {self.pet.name}!")
        self.pet.noise()
        return self
