class Car():
    """Class that represents a Car with a driver
    """

    def __init__(self, registration_number: str, driver_age: int):

        self.__registration_number = registration_number
        self.__driver_age = driver_age

    @property
    def driver_age(self):
        """Returns the driver's age

        :return: driver's age
        :rtype: int
        """

        return self.__driver_age

    @property
    def registration_number(self):
        """Returns the car's registration number

        :return: registration number
        :rtype: str
        """

        return self.__registration_number
