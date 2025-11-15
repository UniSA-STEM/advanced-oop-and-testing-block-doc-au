"""
File: enclosure.py
Description: This module sets up and manages animal enclosures withing defined animal-appropriate limits.
Author: Neil John Cochrane
ID: 110484750
Username: COCNJ001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

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
        self.__currently_contains = ""
        self.__is_open_for_business = True

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

    def get_currently_contains(self):
        return self.__currently_contains

    def get_animal_count(self):
        return self.__animal_count

    def get_is_open_for_business(self):
        return self.__is_open_for_business

    # SETTERS
    def set_name(self, name):
        if name is not None:
            self.__name = name

    def set_cleanliness(self, cleanliness):
        if cleanliness >= 0 and cleanliness <= 100:
            self.__cleanliness = cleanliness

    def set_currently_contains(self, currently_contains):
        self.__currently_contains = currently_contains

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
    currently_contains = property(get_currently_contains, set_currently_contains)
    animal_count = property(get_animal_count, set_animal_count)
    is_open_for_business = property(get_is_open_for_business, set_is_open_for_business)




    #CLASS METHODS

    def report_status(self):
        return_string = f"The enclosure '{self.name}' is a {self.__environment_type}.\n"
        return_string += f"It's size is {self.size} units, and cleanliness is currently {self.cleanliness}%\n"
        if self.animal_count == 0:
            return_string += f"The enclosure is empty.\n"
        else:
            return_string += f"The enclosure currently contains...\n{self.currently_contains} and the count is {self.animal_count}.\n"
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
        print(f"Trying to place a {animal_group} usually enclosed in {environs}.")
        print(f"This environment is a {self.environment_type}.")
        if self.is_open_for_business == False:
            raise ValueError("This enclosure is not open for business.")
        if self.environment_type not in environs:
           raise ValueError(f"The enclosure '{self.name}' is not suitable for a {animal_group}.")
        if self.animal_count > 0:
            if animal.species != self.currently_contains:
                raise ValueError(f"Sorry - you cant place a {animal.species} in an enclsure with a {self.currently_contains}.")
        else:
            self.currently_contains = animal.species
        self.animal_count += 1
        animal.on_display = True






