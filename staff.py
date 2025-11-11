"""
File: staff.py
Description: A brief description of this Python module.
Author: Neil John Cochrane
ID: 110484750
Username: COCNJ001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Staff:
    def __init__(self, name, role, responsibilities, is_active_staff):
        self.__name = name
        self.__role = role
        self.__responsibilities = []
        self.__is_active_staff = True


    #Getters and setters..

    #GETTERS
    def get_name(self):
        return self.__name

    def get_role(self):
        return self.__role

    def get_responsibilities(self):
        return self.__responsibilities

    def get_is_active_staff(self):
        return self.__is_active_staff

    #SETTERS
    def set_name(self, name):
        if name is not None:
            self.__name = name

    def set_role(self, role):
        if role is not None:
            self.__role = role

    def set_responsibilities(self, responsibilities):
        if responsibilities is not None:
            self.__responsibilities = responsibilities

    def set_is_active_staff(self, is_active_staff):
        self.__is_active_staff = is_active_staff

    #Properties

    name = property(get_name, set_name)
    role = property(get_role, set_role)
    responsibilities = property(get_responsibilities, set_responsibilities)
    is_active_staff = property(get_is_active_staff, set_is_active_staff)


    #Class methods...
    def feed_animals(self):
        pass
        for responsibility in self.__responsibilities:
            responsibility.feed_animals()

    def clean_enclsoures(self):
        pass
        for responsibility in self.__responsibilities:
            responsibility.clean_enclosures()

    def health_check(self):
        pass

    def assign_to_enclosure(self, enclosure):
        pass






