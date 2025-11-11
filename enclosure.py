"""
File: enclosure.py
Description: This module sets up and manages animal enclosures withing defined animal-appropriate limits.
Author: Neil John Cochrane
ID: 110484750
Username: COCNJ001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Enclosure:
    def __init__(self, name, size, environment_type):
        self.__name = name
        self.__size = size
        self.__environment_type = environment_type
        self.__cleanliness = 100
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

       def set_cleanliness(self, cleanliness):
        if cleanliness >= 0 and cleanliness <= 100:
            self.__cleanliness = cleanliness

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


    # Properties
    name = property(get_name, set_name)
    size = property(get_size)
    environment_type = property(get_environment_type)
    cleanliness = property(get_cleanliness, set_cleanliness)
    compatible_species = property(get_compatible_species)
    currently_contains = property(get_currently_contains, set_currently_contains)
    animal_count = property(get_animal_count)
    is_open_for_business = property(get_is_open_for_business, set_is_open_for_business)


    #Initialisaton methods to populate lists
    def list_compatible_species(self):
        pass


    #CLASS METHODS

    def report_status(self):
        pass

    def list_animals(self):
        pass
