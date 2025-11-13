"""
File: main.py
Description: A brief description of this Python module.
Author: Neil John Cochrane
ID: 110484750
Username: COCNJ001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# GitHub Classroom repo = https://github.com/UniSA-STEM/advanced-oop-and-testing-block-doc-au.git

#IMPORTS
from animal import *
from enclosure import *
from staff import *

#   Constants and globalS
MAX_HEALTH = 100
MAX_CLEANLINESS = 100
MAX_ZOO_SIZE = 1000
MAX_SAVANNAH = 250
MAX_CAGE = 25
MAX_AMPHIBIOUS = 40
MAX_AQUARIUM = 20
MAX_TERRARIUM = 10
CURRENT_ZOO_SPACE = 0
ZOO_OCCUPANTS = []  # start with an empty zoo...

ALLOWABLE_FOODS = ["pellets", "fish_food", "fish", "meat", "fruit", "vegetables", "grass", "water"]
REGISTERED_ANIMALS = ["parrot", "macaw", "shark", "angelfish", "snake", "lizard", "lion", "tiger", "meerkat", "dolphin", "seal", "penguin", "zebra", "turtle", "chimpanzee"]
MAMMALS = ["lion", "tiger", "meerkat", "dolphin", "seal", "zebra", "chimpanzee"]
AQUATIC = ["shark", "angelfish", "dolphin", "seal", "penguin", "turtle"]
BIRDS = ["parrot", "macaw", "penguin"]
REPTILES = ["snake", "lizard", "turtle"]

# BASIC testing codse... to be removed

zebra1 = Mammals("Zane the Zebra", "zebra", 10, ["grass", "fruit", "vegetables"], "savannah")
ZOO_OCCUPANTS.append(zebra1)
print(zebra1)
zebra1.eat()
zebra1.make_sound()


fish1 = Fish("Sam the Shark", "shark", 15, "fish")
ZOO_OCCUPANTS.append(fish1)
print(fish1)
fish1.eat()
fish1.make_sound()


reptile1 = Reptiles("Sydney the Snake", "snake", 3, "meat")
ZOO_OCCUPANTS.append(reptile1)
print(reptile1)
reptile1.eat()
reptile1.health = 50
reptile1.sleep()
reptile1.make_sound()


bird1 = Birds("Molly the Macaw", "macaw", 12, ["fruit", "vegetables", "pellets"])
ZOO_OCCUPANTS.append(bird1)
print(bird1)
bird1.eat()
bird1.sleep()
bird1.make_sound()



print(f"Zoo occupants are : \n{ZOO_OCCUPANTS}")

if bird1 in ZOO_OCCUPANTS:
    ZOO_OCCUPANTS.remove(bird1)

print(f"Zoo occupants are now : \n{ZOO_OCCUPANTS}")


print("Trying fail options...")

try:
    bird2 = Birds("Peter the Pigeon", "pigeon", 12, ["fruit", "vegetables"])
except ValueError:
    print("The provided species is not allowed in this zoo")

print(f"Zoo occupants are now : ")
for occupants in ZOO_OCCUPANTS:
    print(occupants)

terrarium1 = Enclosure("Snake Space", 15, "terrarium")


