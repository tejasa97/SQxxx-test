import abc
import re
from enum import Enum


class Commands(Enum):
    """Stores all available commands
    """
    CREATE_NEW_PARKING_LOT = "creates a new parking lot"
    PARK_CAR_WITH_REG_NO = "parks a car with a registration number and drivers age"
    GET_SLOTS_FOR_DRIVER_AGE = "returns all slots of cars having drivers of certain age"
    RETURN_SLOT_WITH_REG_NO = "return slot number for the car with registration number"
    VACATE_SLOT_NO = "vacate slot number"
    GET_REG_NOS_FOR_DRIVER_AGE = " get registration number of all cars for driver age"


class BaseCommand(abc.ABC):
    """Base Class for all Commands
    """
    @abc.abstractclassmethod
    def command_type(self):
        raise NotImplementedError()

    @abc.abstractclassmethod
    def keys(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def regex_pattern(self):
        raise NotImplementedError()

    def __init__(self):
        ...

    def check_if_match(self, text: str):
        """Checks if Command is a match for the provided text

        :param text: command text
        :type text: str
        :return: matched groups(data) of text
        :rtype: dict
        """

        try:
            matches = list(self.regex_pattern.match(text).groups())
        except AttributeError:
            return None

        return self.get_matched_groups(matches)

    def get_matched_groups(self, matched_elements: tuple):
        """Returns the matched data of the command

        :param matched_elements: regex matching groups
        :type matched_elements: tuple
        :return: matched data (keys and values)
        :rtype: dict
        """

        return dict(zip(self.keys, matched_elements))


class CreateParkingLot(BaseCommand):

    command_type = Commands.CREATE_NEW_PARKING_LOT
    keys = ['number']
    regex_pattern = re.compile(r'^Create_parking_lot\s(\d+)$')


class ParkCar(BaseCommand):

    command_type = Commands.PARK_CAR_WITH_REG_NO
    keys = ['registration_number', 'driver_age']
    regex_pattern = re.compile(r'^Park\s([-\w]{13})\sdriver_age\s(\d+)$')


class GetSlotsForDriverAge(BaseCommand):

    command_type = Commands.GET_SLOTS_FOR_DRIVER_AGE
    keys = ['driver_age']
    regex_pattern = re.compile(r'^Slot_numbers_for_driver_of_age\s(\d+)$')


class GetSlotForRegnNumber(BaseCommand):

    command_type = Commands.RETURN_SLOT_WITH_REG_NO
    keys = ['registration_number']
    regex_pattern = re.compile(r'^Slot_number_for_car_with_number\s([-\w]{13})$')


class VacateSlot(BaseCommand):

    command_type = Commands.VACATE_SLOT_NO
    keys = ['slot_number']
    regex_pattern = re.compile(r'^Leave\s(\d+)$')


class GetRegnNumbersForDriverAge(BaseCommand):

    command_type = Commands.GET_REG_NOS_FOR_DRIVER_AGE
    keys = ['driver_age']
    regex_pattern = re.compile(r'^Vehicle_registration_number_for_driver_of_age\s(\d+)$')
