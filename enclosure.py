"""
File: enclosure.py
Description: This module sets up and manages animal enclosures withing defined animal-appropriate limits.
Author: Neil John Cochrane
ID: 110484750
Username: COCNJ001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from colorama import Fore, Back, Style
from animal import *


MAX_HEALTH = 100
MAX_CLEANLINESS = 100
MAX_ZOO_SIZE = 1000
MAX_SAVANNAH = 250
MAX_CAGE = 25
MAX_AMPHIBIOUS = 40
MAX_AQUARIUM = 20
MAX_TERRARIUM = 10
CURRENT_ZOO_SPACE = 0
ADDED_ENCLOSURES = []



class Enclosure:
    def __init__(self, name, size, environment_type):
        if CURRENT_ZOO_SPACE + size > MAX_ZOO_SIZE:
            raise ValueError("Enclosure size is too big to fit in whats left of the zoo grounds")
        if environment_type == "savannah":
            if size > MAX_SAVANNAH:
                raise ValueError(f"This savananah is above allowable size of {MAX_SAVANNAH}")
        if environment_type == "cage":
            if size > MAX_CAGE:
                raise ValueError(f"This cage is above allowable size of {MAX_CAGE}")
        if environment_type == "amphibious":
            if size > MAX_AMPHIBIOUS:
                raise ValueError(f"This amphibious environment is above allowable size of {MAX_AMPHIBIOUS}")
        if environment_type == "aquarium":
            if size > MAX_AQUARIUM:
                raise ValueError(f"This aquarium is above allowable size of {MAX_AQUARIUM}")
        if environment_type == "terrarium":
            if size > MAX_TERRARIUM:
                raise ValueError(f"This terrarium is above allowable size of {MAX_TERRARIUM}")
        self.__name = name
        self.__size = size
        self.__environment_type = environment_type
        self.__cleanliness = 100
        self.__animal_count = 0
        self.__current_species = ""
        self.__population = []
        self.__is_open_for_business = True

    def __str__(self):
        return_string = f"Environment type : {self.environment_type}, holding {self.current_species}s\n"
        return_string += f"Cleanliness : {self.cleanliness}\n"
        return_string += f"Size : {self.size}\n"
        return_string += f"Animal Count : {self.animal_count}\n"
        if self.is_open_for_business:
            return_string += f"'{self.name}' is " + Fore.GREEN + "OPEN\n" + Fore.WHITE
        else:
            return_string += f"'{self.name}' is " + Fore.RED + "CLOSED\n" + Fore.WHITE
        return return_string

    # initialise getters and setters

    #GETTERS
    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def get_environment_type(self):
        return self.__environment_type

    def get_cleanliness(self):
        return self.__cleanliness

    def get_compatible_species(self):
        return self.__compatible_species

    def get_current_species(self):
        return self.__current_species

    def get_animal_count(self):
        return self.__animal_count

    def get_population(self):
        return self.__population

    def get_is_open_for_business(self):
        return self.__is_open_for_business


    # SETTERS
    def set_name(self, name):
        if name is not None:
            self.__name = name

    def set_cleanliness(self, cleanliness):
        if cleanliness >= 0 and cleanliness <= 100:
            self.__cleanliness = cleanliness

    def set_current_species(self, current_species):
        self.__current_species = current_species

    def set_population(self, population):
        self.__population = population

    def set_animal_count(self, animal_count):
        self.__animal_count = animal_count

    def set_is_open_for_business(self, is_open_for_business):
        self.__is_open_for_business = is_open_for_business


    # Properties
    name = property(get_name, set_name)
    size = property(get_size)
    environment_type = property(get_environment_type)
    cleanliness = property(get_cleanliness, set_cleanliness)
    compatible_species = property(get_compatible_species)
    current_species = property(get_current_species, set_current_species)
    animal_count = property(get_animal_count, set_animal_count)
    population = property(get_population, set_population)
    is_open_for_business = property(get_is_open_for_business, set_is_open_for_business)




    #CLASS METHODS

    def report_status(self):
        return_string = f"The enclosure '{self.name}' is a {self.__environment_type}.\n"
        return_string += f"It's size is {self.size} units, and cleanliness is currently {self.cleanliness}%\n"
        if self.animal_count == 0:
            return_string += f"The enclosure is empty.\n"
        else:
            return_string += f"The enclosure currently contains...\n{self.current_species}s and the count is {self.animal_count}.\n"
        if self.is_open_for_business:
            return_string += f"The enclosure is open for business."
        else:
            return_string += f"The enclosure is CLOSED at present."
        return return_string


    def list_animals(self):
        return_string = f"\nAnimal Count...\nThe enclosure '{self.name}' "
        if self.animal_count == 0:
            return_string += "is empty.\n"
        else:
            return_string += f"contains... {self.animal_count} {self.currently_contains}s.\n"
        return_string += "--------------------"
        return return_string

    def assign_animal(self, animal):
        animal_group = animal.return_animal_type()
        environs = animal.confirm_poss_environs()
        print(f"Attempting to place a {animal_group} usually enclosed in {environs}.")
        print(f"This environment is a {self.environment_type}.")
        if self.is_open_for_business == False:
            raise ValueError("This enclosure is not open for business.")
        if self.environment_type not in environs:
           raise ValueError(f"The enclosure '{self.name}' is not suitable for a {animal_group}.")
        if self.cleanliness <= 50:
            print(f"The enclosure '{self.name}' needs a clean!!")
            self.is_open_for_business = False
            raise ValueError(f"The enclosure '{self.name}' is not clean enough to accept an animal.")
        if self.animal_count > 0:
            if animal.species != self.current_species:
                raise ValueError(f"Sorry - you cant place a {animal.species} in an enclosure with a {self.current_species}.")
        else:
            self.current_species = animal.species
        self.__population.append(animal)
        self.animal_count += 1
        animal.on_display = True
        animal.current_enclosure = self.name
        if self.animal_count > 0:
            for animal in self.population:
                animal.health -= 10
        self.cleanliness -= 10
        if self.cleanliness <= 50:
            self.is_open_for_business = False








