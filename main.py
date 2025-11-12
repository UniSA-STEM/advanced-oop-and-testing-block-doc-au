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
from enclosure import Enclosure
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

ALLOWABLE_FOODS = ["pellets", "fish_food", "fish", "meat", "fruit", "vegetables", "grass", "water"]
REGISTERED_ANIMALS = ["parrot", "macaw", "shark", "angelfish", "snake", "lizard", "lion", "tiger", "meerkat", "dolphin", "seal", "penguin", "zebra", "turtle", "chimpanzee"]
MAMMALS = ["lion", "tiger", "meerkat", "dolphin", "seal", "zebra", "chimpanzee"]
AQUATIC = ["shark", "angelfish", "dolphin", "seal", "penguin", "turtle"]
BIRDS = ["parrot", "macaw", "penguin"]
REPTILES = ["snake", "lizard", "turtle"]

# BASIC testiung codse... to be removed

zebra1 = Mammal("Zane the Zebra", "zebra", 10, ["grass", "fruit", "vegetables"], "savannah")
print(zebra1)

fish1 = Fish("Sam the Shark", "shark", 15, "fish")
print(fish1)

fish1.eat()
