"""
File: animal.py
Description: This module develops the parent class and child classes of animals of the zoo, with attendant methods.
Author: Neil John Cochrane
ID: 110484750
Username: COCNJ001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Animals:
    def __init__(self, name, species, age   ):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__health = 100
        self.__being_treated = False
        self.__on_display = True
        self.__dietary_needs = self.assign_diet_for_species()
        self.__environmental_needs = self.assign_environmental_needs()

    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def get_age(self):
        return self.__age

    def get_health(self):
        return self.__health

    def get_being_treated(self):
        return self.__being_treated

    def get_on_display(self):
        return self.__on_display

    def get_dietary_needs(self):
        return self.__dietary_needs

    def get_environmental_needs(self):
        return self.__environmental_needs



    def assign_diet_for_species(self):
        pass

    def assign_environmental_needs(self):
        pass

    def make_sounds(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass






