"""
File: staff.py
Description: This defines the porent class of Staff and subclasses of zoo employees.
Author: Neil John Cochrane
ID: 110484750
Username: COCNJ001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from animal import ZOO_OCCUPANTS
from enclosure import ADDED_ENCLOSURES


class Staff:
    def __init__(self, name, date_employed):
        self.__name = name
        self.__responsibilities = []
        self.__is_active_staff = True
        self.__date_employed = date_employed

    #Getters and setters..

    #GETTERS
    def get_name(self):
        return self.__name

    def get_responsibilities(self):
        return self.__responsibilities

    def get_is_active_staff(self):
        return self.__is_active_staff


    def get_date_employed(self):
        return self.__date_employed

    #SETTERS
    def set_name(self, name):
        if name is not None:
            self.__name = name

    def set_is_active_staff(self, is_active_staff):
        self.__is_active_staff = is_active_staff

    #Properties

    name = property(get_name, set_name)
    responsibilities = property(get_responsibilities)
    is_active_staff = property(get_is_active_staff, set_is_active_staff)
    date_employed = property(get_date_employed)


    #Parent Class methods...
    def operational_matters(self):
        print("Doing operational matters to keep the Zoo running smoothly.")

    def move_animal(self, animal, enclosure_from, enclosure_to):
        if self.__class__.__name__ == "Operations":
            raise ValueError("An operations person is unable to assign to an enclosure.")
        print(f"About to move an animal from an enclosure containing : {enclosure_from.population}...\n")
        if animal not in enclosure_from.population:
            raise ValueError(f"There isn't a {animal.species} in the enclosure '{enclosure_from.name}' to move.")
        if enclosure_to.environment_type != enclosure_from.environment_type:
            raise ValueError("The enclosure types aren't the same - cannot move the animal between them.")
        moving_animal = animal
        enclosure_from.population.remove(animal)
        enclosure_from.animal_count -= 1
        enclosure_to.assign_animal(moving_animal)
        moving_animal.on_display = False

    def remove_animal(self, animal, enclosure):
        if self.__class__.__name__ == "Operations":
            raise ValueError("An operations person is unable to assign to an enclosure.")
        print(f"About to remove an animal from an enclosure containing : {enclosure.population}...\n")
        if animal not in enclosure.population:
            raise ValueError(f"There isn't a {animal.species} in the enclosure '{enclosure.name}' to move.")
        moving_animal = animal
        enclosure.population.remove(animal)
        enclosure.animal_count -= 1
        animal.on_display = False

    def assign_to_enclosure(self, animal, enclosure):
        if self.__class__.__name__ == "Operations":
            raise ValueError("An operations person is unable to assign to an enclosure.")
        enclosure.assign_animal(animal)


    def feed_animal(self, animal):
        if self.__class__.__name__ == "Operations":
            raise ValueError("An operations person is unable to feed the animals.")
        animal.eat()

    def health_check(self, animal):
        if self.__class__.__name__ == "Operations":
            raise ValueError("An operations person is unable to undertake health checks.")

    def treat(self, animal):
        if self.__class__.__name__ == "Operations":
            raise ValueError("An operations person is unable to treat animals.")

    def clean_enclosure(self, enclosure):
        if self.__class__.__name__ == "Operations":
            raise ValueError("An operations person is unable to clean enclosures.")
        enclosure.cleanliness = 100
        enclosure.is_open_for_business = True

    def do_daily_routines(self):
        if "feed animals" in self.responsibilities:
            for animal in ZOO_OCCUPANTS:
                animal.eat()
        if "treat animals" in self.responsibilities:
            for animal in ZOO_OCCUPANTS:
                if animal.species in self.animals_can_treat:
                    self.treat(animal)
        if "clean enclosures" in self.responsibilities:
            for enclosure in ADDED_ENCLOSURES:
                self.clean_enclosure(enclosure)


class Veterinarian(Staff):
    def __init__(self, name, date_employed, animals_can_treat):
        Staff.__init__(self, name, date_employed)
        self.__name = name
        self.__date_employed = date_employed
        self.__responsibilities = ["health checks", "treat animals", "move animals", "assign enclosure"]
        self.__animals_can_treat = animals_can_treat
        self.__is_active_staff = True

    def __str__(self):
        return_string = f"{self.name} is a veterinarian employed on {self.date_employed}.\n"
        return_string += f"Their responsibilities include : {self.responsibilities}\n"
        return_string += f"They can treat : {self.animals_can_manage}\n"
        if self.is_active_staff:
            return_string += "They are ACTIVE in their role.\n"
        else:
            return_string += f"{self.name} is NOT actively empoyed at this time.\n"
        return return_string

    # GETTERS

    def get_name(self):
        return self.__name

    def get_responsibilities(self):
        return self.__responsibilities

    def get_is_active_staff(self):
        return self.__is_active_staff

    def get_date_employed(self):
        return self.__date_employed

    def get_animals_can_treat(self):
        return self.__animals_can_treat


    # SETTERS
    def set_name(self, name):
        if name is not None:
            self.__name = name

    def set_responsibilities(self, responsibilities):
        self.__responsibilities = responsibilities

    def set_animals_can_treat(self, animals_can_treat):
        if animals_can_treat is not None:
            self.__animals_can_treat.append(animals_can_treat)

    def set_is_active_staff(self, is_active_staff):
        self.__is_active_staff = is_active_staff

    # Properties
    name = property(get_name, set_name)
    responsibilities = property(get_responsibilities, set_responsibilities)
    is_active_staff = property(get_is_active_staff, set_is_active_staff)
    date_employed = property(get_date_employed)
    animals_can_treat = property(get_animals_can_treat, set_animals_can_treat)

    def health_check(self, animal):
        if animal.species not in self.animals_can_treat:
            raise ValueError(f"This vet cannot undertake health checks on {animal.species}s.")
        if animal.health < 100:
            animal.being_treated = True
            animal.on_display = False
            return "treat"

    def treat(self, animal):
        if animal.species not in self.animals_can_treat:
            raise ValueError(f"This vet cannot treat {animal.species}s.")
        animal.health = 100
        animal.illness = {}
        animal.injuries = {}
        animal.behavioural_problems = {}
        animal.being_treated = False
        animal.on_display = True

class Zookeeper(Staff):
    def __init__(self, name, date_employed, animals_can_manage):
        Staff.__init__(self, name, date_employed)
        self.__responsibilities = ["move animals", "feed animals", "clean enclosures", "assign enclosure"]
        self.__animals_can_manage = animals_can_manage
        self.__is_active_staff = True

    def __str__(self):
        return_string = f"{self.name} is a zookeeper employed on {self.date_employed}.\n"
        return_string += f"Their responsibilities include : {self.responsibilities}\n"
        return_string += f"They can manage : {self.animals_can_manage}\n"
        if self.is_active_staff:
            return_string += "They are ACTIVE in their role.\n"
        else:
            return_string += f"{self.name} is NOT actively empoyed at this time.\n"
        return return_string


    # GETTERS


    def get_responsibilities(self):
        return self.__responsibilities

    def get_is_active_staff(self):
        return self.__is_active_staff

    def get_animals_can_manage(self):
        return self.__animals_can_manage

    # SETTERS


    def set_responsibilities(self, responsibilities):
        self.__responsibilities = responsibilities

    def set_animals_can_manage(self, animals_can_manage):
        if animals_can_manage is not None:
            self.__animals_can_manage = animals_can_manage

    def set_is_active_staff(self, is_active_staff):
        self.__is_active_staff = is_active_staff

    # Properties
    responsibilities = property(get_responsibilities, set_responsibilities)
    is_active_staff = property(get_is_active_staff, set_is_active_staff)
    animals_can_manage = property(get_animals_can_manage, set_animals_can_manage)



class Operations(Staff):
    def __init__(self, name, date_employed):
        Staff.__init__(self, name, date_employed)
        self.__responsibilities = ["operations"]

    def __str__(self):
        return_string = f"{self.name} is an operations person employed on {self.date_employed}.\n"
        return_string += f"Their responsibilities include : {self.responsibilities}\n"
        return_string += f"They CANNOT treat or manage animals in the zoo.\n"
        if self.is_active_staff:
            return_string += "They are ACTIVE in their role.\n"
        else:
            return_string += f"{self.name} is NOT actively empoyed at this time.\n"
        return return_string

    # GETTERS

    def get_name(self):
        return self.__name

    def get_is_active_staff(self):
        return self.__is_active_staff

    def get_date_employed(self):
        return self.__date_employed

    def get_responsibilities(self):
        return self.__responsibilities


    # SETTERS
    def set_name(self, name):
        if name is not None:
            self.__name = name

    def set_is_active_staff(self, is_active_staff):
        self.__is_active_staff = is_active_staff

    def set_responsibilities(self, responsibilities):
        self.__responsibilities = responsibilities


    # Properties
    name = property(get_name, set_name)
    responsibilities = property(get_responsibilities, set_responsibilities)
    is_active_staff = property(get_is_active_staff, set_is_active_staff)
    date_employed = property(get_date_employed)







