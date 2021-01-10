class Car():

    def __init__(self, registration_number, driver_age):

        self.__registration_number = registration_number
        self.__driver_age = driver_age

    @property
    def driver_age(self):

        return self.__driver_age

    @property
    def registration_number(self):

        return self.__registration_number
