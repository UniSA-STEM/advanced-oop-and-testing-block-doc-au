"""
File: animal.py
Description: This module develops the parent class and child classes of animals of the zoo, with attendant methods.
Author: Neil John Cochrane
ID: 110484750
Username: COCNJ001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# Pre-requisites for animal management and allocation
# in a formal project, this would be a database connection so that it could be saved and modified
ALLOWABLE_FOODS = ["pellets", "fish_food", "fish", "meat", "fruit", "vegetables", "grass", "water"]
REGISTERED_ANIMALS = {"parrot": "bird", "macaw": "bird", "shark": "aquatic", "angelfish": "aquatic", "snake": "reptile",
                      "lizard": "reptile", "lion": "mammal", "tiger": "mammal", "meerkat": "mammal", "dolphin": "aquatic",
                      "seal": "amphibious", "penguin": "amphibious", "zebra": "mammal", "turtle": "aquatic", "chimpanzee": "mammal"}
FOOD_BY_SPECIES = {"parrot": ["pellets", "fruit", "vegetables"], "macaw": ["pellets", "fruit", "vegetables"], "shark": ["fish"],
                   "angelfish": ["fish_food"], "snake": ["meat"],
                   "lizard": ["meat"], "lion": ["meat"], "tiger": ["meat"], "meerkat": ["meat", "fruit"], "dolphin": ["fish"],
                   "seal": ["fish"], "penguin": ["fish"], "zebra": ["grass", "vegetables"], "turtle": ["fish_food", "vegetables"], "chimpanzee": ["meat", "fruit", "vegetables"]}
SUITABLE_ENVIRONMENTS = {"mammal": ["savannah", "cage", "amphibious"], "aquatic": ["amphibious", "tank"], "bird": "cage", "reptile": "terrarium"}

# Likely able to delete these once dictionary replacement completed
MAMMALS = ["lion", "tiger", "meerkat", "dolphin", "seal", "zebra", "chimpanzee"]
AQUATIC = ["shark", "angelfish", "dolphin", "seal", "penguin", "turtle"]
BIRDS = ["parrot", "macaw", "penguin"]
REPTILES = ["snake", "lizard", "turtle"]
ZOO_OCCUPANTS = []  # start with an empty zoo...

class Animals:
    def __init__(self, name, species, age, dietary_needs):
        if species not in REGISTERED_ANIMALS:
            raise ValueError("This is not a species allowed in this zoo.")
        suitable_foods = []
        for key, value in FOOD_BY_SPECIES.items():
            if key == species:
               for item in value:
                suitable_foods.append(item)
        if isinstance(dietary_needs, list):
            for item in dietary_needs:
               if item not in suitable_foods:
                   raise ValueError(f"{item} is not a food option suitable for a {species}")
        else:
            print("Just 1 food item in list...")
            if dietary_needs not in suitable_foods:
                raise ValueError(f"{dietary_needs} is not a food option suitable for a {species}")
        if age <= 0:
            raise ValueError("Age must be greater than zero.")
        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary_needs = dietary_needs
        self.__health = 100
        self.__being_treated = False
        self.__on_display = False


    # Define GETTERS
    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def get_age(self):
        return self.__age

    def get_dietary_needs(self):
        return self.__dietary_needs

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
    dietary_needs = property(get_dietary_needs)
    health = property(get_health, set_health)
    being_treated = property(get_being_treated, set_being_treated)
    on_display = property(get_on_display, set_on_display)


    # General class methods:

    def eat(self):
        # print("\nAbout to eat...")
        self.__health += 10
        if self.__health > 100:
            self.__health = 100
        return f"{self.__name} has eaten! Health is now {self.__health}%\n"

    def sleep(self):
        # print("\nAbout to sleep...")
        self.__health += 20
        if self.__health > 100:
            self.__health = 100
        return f"{self.__name} has slept! Health is now {self.__health}%\n"

    def make_sound(self):
        return "\nCould be any sound..."

    def return_animal_type(self):
        for species, group in REGISTERED_ANIMALS.items():
            if species == self.__species:
                return group
        return None

    def confirm_poss_environs(self):
        for group, environs in SUITABLE_ENVIRONMENTS.items():
           if group == self.return_animal_type():
               return environs
        return None


class Mammals(Animals):
    def __init__(self, name, species, age, dietary_needs, suitable_environment):
        super().__init__(name, species, age, dietary_needs)
        self.__suitable_environment = suitable_environment

    def __str__(self):
        return_string = f"\n{self.name} is a {self.species}, in the mammal group.\n"
        return_string += f"They are {self.age} years old, and health level is at {self.health}%\n"
        return_string += f"{self.name} eats : {self.dietary_needs} and lives in a {self.__suitable_environment}.\n"
        return_string += f"STATUS :\nHealth = {self.health}%, being treated = {self.being_treated}, and on display = {self.on_display}"
        return return_string

    # Define GETTERS

    def get_suitable_environment(self):
        return self.__suitable_environment

    suitable_environment = property(get_suitable_environment)

    def make_sound(self):
        if self.species in ["lion", "tiger"]:
            sound_character = "roars"
        elif self.species == "dolphin":
            sound_character = "clicks and chirps"
        elif self.species == "seal":
            sound_character = "barks"
        elif self.species == "chimpanzee":
            sound_character = "chatters and cries"
        elif self.species == "zebra":
            sound_character = "whinnies"
        else:
            sound_character = "growls !"
        return f"{self.name} {sound_character} !"

class Fish(Animals):
    def __init__(self, name, species, age, dietary_needs):
        super().__init__(name, species, age, dietary_needs)
        self.__suitable_environment = "aquarium"

    def __str__(self):
        return_string = f"\n{self.name} is a {self.species}, in the aquatic/fish group.\n"
        return_string += f"They are {self.age} years old, and health level is at {self.health}%\n"
        return_string += f"They eat {self.dietary_needs} and live in a {self.__suitable_environment}.\n"
        return_string += f"STATUS :\nHealth = {self.health}%, being treated = {self.being_treated}, and on display = {self.on_display}"
        return return_string

    # Define GETTERS

    def get_suitable_environment(self):
        return self.__suitable_environment

    suitable_environment = property(get_suitable_environment)

    def make_sound(self):
        return f"{self.name} goes 'glub glub'.\n"


class Reptiles(Animals):
    def __init__(self, name, species, age, dietary_needs):
        super().__init__(name, species, age, dietary_needs)
        self.__dietary_needs = dietary_needs
        self.__suitable_environment = "terrarium"

    def __str__(self):
        return_string = f"\n{self.name} is a {self.species}, in the reptile group.\n"
        return_string += f"They are {self.age} years old, and health level is at {self.health}%\n"
        return_string += f"They eat {self.dietary_needs} and live in a terrarium.\n"
        return_string += f"STATUS :\nHealth = {self.health}%, being treated = {self.being_treated}, and on display = {self.on_display}"
        return return_string

    # Define GETTERS

    def get_suitable_environment(self):
        return self.__suitable_environment

    suitable_environment = property(get_suitable_environment)

    def make_sound(self):
        return f"{self.name} goes 'hiss'.\n"


class Birds(Animals):
    def __init__(self, name, species, age, dietary_needs):
        super().__init__(name, species, age, dietary_needs)
        self.__suitable_environment = "cage"

    def __str__(self):
        return_string = f"\n{self.name} is a {self.species}, in the bird group.\n"
        return_string += f"They are {self.age} years old, and health level is at {self.health}%\n"
        return_string += f"They eat {self.dietary_needs} and live in a cage (sadly).\n"
        return_string += f"STATUS :\nHealth = {self.health}%, being treated = {self.being_treated}, and on display = {self.on_display}"
        return return_string

    # Define GETTERS
    #def get_dietary_needs(self):
    #    return self.dietary_needs

    def get_suitable_environment(self):
        return self.__suitable_environment

    suitable_environment = property(get_suitable_environment)

    def make_sound(self):
        return f"{self.name} goes 'cheep cheep' !"



