"""
File: staff.py
Description: This defines the porent class of Staff and subclasses of zoo employees.
Author: Neil John Cochrane
ID: 110484750
Username: COCNJ001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

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
    def feed_animals(self):
        pass

    def move_animals(self):
        pass

    def clean_enclosures(self):
        pass


    def health_check(self):
        pass

    def treat_animals(self):
        pass


    def assign_to_enclosure(self, enclosure):
        pass

    def operational_matters(self):
        print("Doing operational matters to keep the Zoo running smoothly.")




class Veterinarian(Staff):
    def __init__(self, name, animals_can_treat):
        Staff.__init__(self, name)
        self.__responsibilities = ["health checks", "treat animals", "move animals", "assign enclosure"]
        self.__animals_can_treat = animals_can_treat


class Zookeeper(Staff):
    def __init__(self, name, animals_can_manage):
        Staff.__init__(self, name)
        self.__responsibilities = ["move animals", "feed animals", "clean enclosures", "assign enclosure"]
        self.__animals_can_manage = animals_can_manage

class Operations(Staff):
    def __init__(self, name):
        Staff.__init__(self, name)
        self.__responsibilities = ["operations"]








