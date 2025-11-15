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




def print_zoo_occupants():
    print(f"The specific animal are...")
    for occupants in ZOO_OCCUPANTS:
        print(occupants)
    if len(ZOO_OCCUPANTS) == 0:
        print("No Zoo occupants as yet\n")


# BASIC testing code... to be removed


print("---------------------------")
print("    Welcome to our Zoo!    ")
print("---------------------------\n")

print("Initially the zoo is empty...")
print_zoo_occupants()

print("Now procuring some critters for our zoo...")

zebra1 = Mammals("Zane the Zebra", "zebra", 10, ["grass", "vegetables"], "savannah")
ZOO_OCCUPANTS.append(zebra1)
print(zebra1)
zebra1.eat()
zebra1.make_sound()

zebra2 = Mammals("Zoe the Zebra", "zebra", 8, ["grass", "vegetables"], "savannah")
ZOO_OCCUPANTS.append(zebra2)
print(zebra2)
zebra2.eat()
zebra2.make_sound()

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

print_zoo_occupants()

print(f"Zoo occupants are now saved as : \n{ZOO_OCCUPANTS}")

print("Trying ** FAIL ** options...")

try:
    bird2 = Birds("Peter the Pigeon", "pigeon", 12, ["fruit", "vegetables", "meat"])
except ValueError:
    print("\nERROR in animal allocation....\nI'm afraid this animal isn't set-up correctly to join our zoo\n")

try:
    incorrect_enclosure = Enclosure("Wetlands", 2000, "aquatic")
except ValueError:
    print("\nERROR in environment setup....\nI'm afraid this environment isn't set-up correctly to fit the zoo\n")


print('\nPlaying around with a terrarium...\n')

terrarium1 = Enclosure("Snake Space", 10, "terrarium")
print(terrarium1.report_status())
print(terrarium1.list_animals())


# Allocation to environments

try:
    amphibious1 = Enclosure("a pool and a bank", 20, "amphibious")
except:
    print("Unable to set up this enclosure")

print("Trying to assign animals...\n")
savannah1 = Enclosure("A New Savannah", 45, "savannah")
savannah1.assign_animal(zebra2)
savannah1.assign_animal(zebra1)
try:
    savannah1.assign_animal(bird1)
except ValueError:
    print("\nERROR in environment assignment....\nI'm afraid this environment isn't suitable for a bird\n")

print("An update on savannah1...\n")
print(f"After adding 2 zebras to savannahh 1...")
print(f"savannah1 contains : {savannah1.currently_contains}")
print(f"This comprises...\n{savannah1.animal_count} animals of this type.")
print(f"The zoo now has {len(ZOO_OCCUPANTS)} animals, which are specifically...\n")
for animal in ZOO_OCCUPANTS:
    print(animal)



