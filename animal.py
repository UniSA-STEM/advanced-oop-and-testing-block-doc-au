"""
File: animal.py
Description: This module develops the parent class and child classes of animals of the zoo, with attendant methods.
Author: Neil John Cochrane
ID: 110484750
Username: COCNJ001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from collections.abc import async_generator


class Animals:
    def __init__(self, name, species, age):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__health = 100
        self.__being_treated = False
        self.__on_display = True
        # self.__dietary_needs = self.assign_diet_for_species()
        # self.__environmental_needs = self.assign_environmental_needs()



    # Define GETTERS
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

    # Define SETTERS
    def set_name(self, name):
        if name is not None:
            self.__name = name

    def set_health(self, health):
        if health is not None:
            self.__health = health

    def set_being_treated(self, being_treated):
        self.__being_treated = being_treated

    def set_on_display(self, on_display):
        self.__on_display = on_display

    # Properties

    name = property(get_name, set_name)
    species = property(get_species)
    age = property(get_age)
    health = property(get_health, set_health)
    being_treated = property(get_being_treated, set_being_treated)
    on_display = property(get_on_display, set_on_display)


    # General class methods:
    def make_sounds(self):
        pass

    def eat(self):
        print("About to eat...")
        self.__health += 10
        if self.__health > 100:
            self.__health = 100
        print(f"{self.__name} has eaten! Health is now {self.__health}%\n")

    def sleep(self):
        pass


class Mammal(Animals):
    def __init__(self, name, species, age, dietary_needs, suitable_environment):
        super().__init__(name, species, age)
        # self.__age = age
        self.__dietary_needs = dietary_needs
        self.__suitable_environment = suitable_environment

    def __str__(self):
        return_string = f"{self.name} is a {self.species.title()}, in the mammal group.\n"
        return_string += f" They are {self.age} years old, and health level is at {self.health}%\n"
        return_string += f"They eat {self.__dietary_needs} and live in a {self.__suitable_environment}.\n"
        return_string += f"Being treated = {self.being_treated}, and on display = {self.on_display}"
        return return_string

    # Define GETTERS
    def get_dietary_needs(self):
        return self.__dietary_needs

    def get_suitable_environment(self):
        return self.__suitable_environment


    dietary_needs = property(get_dietary_needs)
    suitable_environment = property(get_suitable_environment)


class Fish(Animals):
    def __init__(self, name, species, age, dietary_needs):
        super().__init__(name, species, age)
        self.__dietary_needs = dietary_needs
        self.__suitable_environment = "aquarium"

    def __str__(self):
        return_string = f"\n{self.name} is a {self.species.title()}, in the aquatic/fish group.\n"
        return_string += f"They are {self.age} years old, and health level is at {self.health}%\n"
        return_string += f"They eat {self.__dietary_needs} and live in a {self.__suitable_environment}.\n"
        return_string += f"Being treated = {self.being_treated}, and on display = {self.on_display}"
        return return_string

    # Define GETTERS
    def get_dietary_needs(self):
        return self.__dietary_needs

    def get_suitable_environment(self):
        return self.__suitable_environment

    dietary_needs = property(get_dietary_needs)
    suitable_environment = property(get_suitable_environment)

    def eat(self):
        print("\nAbout to eat...")
        self.health += 10
        if self.health > 100:
            self.health = 100
        print(f"{self.name} has eaten! Health is now {self.health}%\n")



class Reptiles(Animals):
    def __init__(self, name, species, age, dietary_needs):
        super().__init__(self, name, species, age)
        self.__dietary_needs = dietary_needs
        self.__suitable_environment = "terrarium"

    # Define GETTERS
    def get_dietary_needs(self):
        return self.__dietary_needs

    def get_suitable_environment(self):
        return self.__suitable_environment

    dietary_needs = property(get_dietary_needs)
    suitable_environment = property(get_suitable_environment)


class Birds(Animals):
    def __init__(self, name, species, age, dietary_needs):
        super().__init__(self, name, species, age)
        self.__dietary_needs = dietary_needs
        self.__suitable_environment = "cage"

    # Define GETTERS
    def get_dietary_needs(self):
        return self.__dietary_needs

    def get_suitable_environment(self):
        return self.__suitable_environment

    dietary_needs = property(get_dietary_needs)
    suitable_environment = property(get_suitable_environment)




