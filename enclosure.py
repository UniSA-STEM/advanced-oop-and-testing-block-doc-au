"""
File: enclosure.py
Description: This module sets up and manages animal enclosures withing defined animal-appropriate limits.
Author: Neil John Cochrane
ID: 110484750
Username: COCNJ001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Enclosures:
    def __init__(self, name, size, environment_type, cleanliness, compatible_species, currently_contains, animal_count, is_open_for_business):
        self.__name = name
        self.__size = size
        self.__environment_type = environment_type
        self.__cleanliness = 100
        self.__compatible_species = self.list_compatible_species()
        self.__currently_contains = self.currently_contains()
        self.__animal_count = 0
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

    def set_size(self, size):
        if size > 0:
            self.__size = size

    def set_environment_type(self, environment_type):
        pass
        if environment_type is not None:
            self.__environment_type = environment_type

    def set_cleanliness(self, cleanliness):
        if cleanliness >= 0 and cleanliness <= 100:
            self.__cleanliness = cleanliness

    def set_compatible_species(self, compatible_species):
        pass
        if compatible_species is not None:
            self.__compatible_species = compatible_species

    def set_currently_contains(self, currently_contains):
        pass
        if currently_contains is not None:
            self.__currently_contains = currently_contains

    def set_animal_count(self, animal_count):
        pass
        if animal_count is not None:
            self.__animal_count = animal_count

    def set_is_open_for_business(self, is_open_for_business):
        pass


    #Initialisaton methods to populate lists
    def list_compatible_species(self):
        pass

    def currently_contains(self):
        pass

    #CLASS METHODS

    def report_status(self):
        pass

    def list_animals(self):
        pass




