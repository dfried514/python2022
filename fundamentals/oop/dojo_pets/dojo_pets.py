from ninja import Ninja
from pet import Pet
from dog import Dog
from horse import Horse
from cat import Cat

pet_1 = Dog(name="Spot", tricks=['roll over', 'jump', 'shake hands'])
pet_2 = Horse(name="Trusty", tricks=['fall over', 'go to sleep'])
pet_3 = Cat(name="Serena", tricks=['sunbathing', 'drinking water from a glass'])

ninja_1 = Ninja(first_name="David", last_name="Friedman",
    treats=['Jerky', 'Bacon', 'Cookies'],
    pet_food=['Hamburger', 'Pizza', 'Hot Dog', 'Chicken Fingers', 'Taco'],
    pet=pet_3)

ninja_1.feed().walk().bathe()
