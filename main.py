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
from colorama import Fore, Back, Style
import datetime
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

def list_animals_by_species():
    for animal_species in REGISTERED_ANIMALS:
        species_count = 0
        for zoo_animal in ZOO_OCCUPANTS:
            if zoo_animal.species == animal_species:
                species_count += 1
        if species_count > 0:
            if species_count < 2:
                print(f" There is {species_count} {animal_species}")
            else:
                print(f" There are {species_count} {animal_species}s")
    print(f"\nTotal zoo occupants is {len(ZOO_OCCUPANTS)}\n")

def list_all_enclosures():
    if len(ADDED_ENCLOSURES) == 0:
        print("No enclosures added to our zoo as yet...")
    else:
        for enclosure in ADDED_ENCLOSURES:
            total_open_enclosures = 0
            print(f"'{enclosure.name}")
            print(enclosure)


# BASIC testing code... to be removed


print("---------------------------")
print("    Welcome to our Zoo!    ")
print("---------------------------\n")

print("Initially the zoo is empty...")
print_zoo_occupants()

print(f"Now enlisting staff to manage the zoo or to move, allocate and fee animals...\n")
vet1 = Veterinarian("Dr Chris", datetime.datetime(2020, 1, 26), ["zebra", "penguin", "seal", "dolphin", "meerkat", "chimpanzee", "snake"])
keeper1 = Zookeeper("Bob the Zookeeper", "20/01/2020", ["zebra", "penguin", "seal", "dolphin", "meerkat", "chimpanzee", "lion", "tiger"])
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
ADDED_ENCLOSURES.append(terrarium1)
print(terrarium1.report_status())
print(terrarium1.list_animals())


# Allocation to environments

try:
    amphibious1 = Enclosure("a pool and a bank", 20, "amphibious")
except:
    print("Unable to set up this enclosure")

print("Trying to assign animals...\n")
savannah1 = Enclosure("A New Savannah", 45, "savannah")
ADDED_ENCLOSURES.append(savannah1)
savannah1.assign_animal(zebra2)
savannah1.assign_animal(zebra1)
try:
    savannah1.assign_animal(bird1)
except ValueError:
    print("\nERROR in environment assignment....\nI'm afraid this environment isn't suitable for a bird\n")

print("An update on savannah1...\n")
print(f"After adding 2 zebras to savannahh 1...")
print(f"savannah1 contains : {savannah1.current_species}")
print(f"This comprises...\n{savannah1.animal_count} animals of this type.")
print(f"The zoo now has {len(ZOO_OCCUPANTS)} animals, which are specifically...\n")
for animal in ZOO_OCCUPANTS:
    print(animal)


savannah2 = Enclosure("A Slightly Bigger Savannah", 65, "savannah")
ADDED_ENCLOSURES.append(savannah2)
zebra3 = Mammals("Ziggy the Zebra", "zebra", 20, ["grass", "vegetables"], "savannah")
zebra4 = Mammals("Zilda the Zebra", "zebra", 16, ["grass", "vegetables"], "savannah")
zebra5 = Mammals("Zeek the Zebra", "zebra", 14, ["grass", "vegetables"], "savannah")
ZOO_OCCUPANTS.append(zebra3)
vet1.assign_to_enclosure(zebra3, savannah1)
print("Ziggy the Zebra now added...\n")
print(f"The zoo now has {len(ZOO_OCCUPANTS)} animals, which are specifically...\n")
for animal in ZOO_OCCUPANTS:
    print(animal)
print("An update on savannah1...\n")
print(f"After adding a zebra to savannahh 1...")
print(f"savannah1 contains : {savannah1.current_species}")
print(f"This comprises...\n{savannah1.animal_count} animals of this type.")
print(f"\nNow moving a zebra...\n")
vet1.move_animal(zebra3, savannah1, savannah2)
print("An update on savannah2...\n")
print(f"After moving a zebras from savannah1...")
print(f"savannah2 now contains : {savannah2.current_species}")
print(f"This comprises...\n{savannah2.animal_count} animals of this type.\n")

print("\nAn update on savannah1...\n")
print(f"savannah1 contains : {savannah1.current_species}")
print(f"This comprises...\n{savannah1.animal_count} animals of this type.\n")

#remove an animal from an enclosure
print(Fore.RED + f"Now using staff to remove an animal from an enclosure...\n")
print(Style.RESET_ALL)
vet1.remove_animal(zebra3, savannah2)
print("An update on savannah1...\n")
print(f"savannah1 contains : {savannah1.current_species}")
print(f"This comprises...\n{savannah1.animal_count} animals of this type.")
print(f"\nNow moving a zebra...\n")
print("An update on savannah2...\n")
print(f"savannah2 now contains : {savannah2.current_species}")
print(f"This comprises...\n{savannah2.animal_count} animals of this type.\n")
print(f"The zoo now has {len(ZOO_OCCUPANTS)} animals, which are specifically...\n")
for animal in ZOO_OCCUPANTS:
    print(animal)
print("The enclosure status....\n")
print(savannah1.report_status())
print(savannah2.report_status())

print(Fore.RED + "\nTrying to move animals to an uncleaned enclsure...\n")
print(Style.RESET_ALL)
vet1.assign_to_enclosure(zebra4, savannah1)
vet1.assign_to_enclosure(zebra5, savannah1)
print("The enclosure status....\n")
print(savannah1.report_status())

#HEALTH CHECK tasks
if vet1.health_check(zebra1) == "treat":
    print(f"Need to treat {zebra1.name}!")
    print(zebra1)
    print(f"\nNow treating {zebra1.name}...\n")
    vet1.treat(zebra1)
    print(f"\nAfter treatment of {zebra1.name}...")
    print(zebra1)

# CLEANING tasks
print(Fore.RED + "\nNOW.. cleaning savannah1...\n")
print(Style.RESET_ALL)
print(keeper1)
keeper1.clean_enclosure(savannah1)
print(Fore.GREEN + "The enclosure status....\n")
print(Style.RESET_ALL)
print(savannah1.report_status())



print(Fore.RED + f"Now a vet will do their tasks...")
zebra1.health = 50
zebra2.health = 50
zebra3.health = 50
print(Style.RESET_ALL)
print(f"The zoo now has {len(ZOO_OCCUPANTS)} animals, which are specifically...\n")
for animal in ZOO_OCCUPANTS:
    print(animal)
vet1.do_daily_routines()
print("\nTasks completed...\n")
print(f"The zoo now has {len(ZOO_OCCUPANTS)} animals, which are specifically...\n")
for animal in ZOO_OCCUPANTS:
    print(animal)

print(Fore.GREEN + f"Listing zoo occupants by species")
print(Style.RESET_ALL)
list_animals_by_species()

print(Fore.GREEN + f"Listing enclosures...")
print(Style.RESET_ALL)
list_all_enclosures()

print(Fore.GREEN + f"Adding an ILLNESS to {zebra1.name}...")
print(Style.RESET_ALL)
zebra1.add_illness("layngitis", "Developed from too much whinnying", datetime.datetime.now(), "mild", "antibiotics")
print(zebra1)
print(zebra1.illness)

print(Fore.GREEN + f"Adding an INJURY to {zebra1.name}...")
print(Style.RESET_ALL)
zebra1.add_injury("Broken foreleg", "Developed from too much running", datetime.datetime.now(), "severe", "casting")
print(zebra1)
print(zebra1.injuries)

print(Fore.GREEN + f"Adding ANOTHER INJURY to {zebra1.name}...")
print(Style.RESET_ALL)
zebra1.add_injury("Broken hindleg", "Developed from running with a broken foreleg", datetime.datetime.now(), "severe", "surgery")
print(zebra1)
print(zebra1.injuries)

print(Fore.GREEN + f"Adding BEHAVIOURAL PROBLEM to zebra1...")
print(Style.RESET_ALL)
zebra1.add_behavioural_problem("Depression", "Miserable due to broken legs", datetime.datetime.now(), "moderate", "a few days off")
print(zebra1)
print(zebra1.behavioural_problems)
zebra1.health_report()

print(Fore.GREEN + f"\nNow TREATING all problems for {zebra1.name}...")
print(Style.RESET_ALL)
vet1.treat(zebra1)
print(zebra1)
zebra1.health_report()
