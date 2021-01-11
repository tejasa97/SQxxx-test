from .car import Car
from .utils import Heap
from domain.utils import Singleton


class ParkingLotManager(metaclass=Singleton):

    class ParkingSlotFull(Exception):
        ...

    class InvalidSlotNumber(Exception):
        ...

    class DoesNotExist(Exception):
        ...

    class SlotEmpty(Exception):
        ...

    class InvalidRegNumber(Exception):
        ...

    class InvalidAge(Exception):
        ...

    __max_slots = 0

    def initialize_slots(self, num_slots: int):
        """Initializes the parking lot with a definite number of slots

        :param num_slots: number of slots
        :type num_slots: int
        """

        self.__max_slots = num_slots

        self.__parking_slots = {}
        self.empty_slots_heap = Heap()

    def add_car_to_slot(self, registration_number: str, driver_age: int):
        """Parks a car in the parking lot

        :param registration_number: car's registration_number
        :type registration_number: str
        :param driver_age: car driver's age
        :type driver_age: int
        :raises self.ParkingSlotFull: if no parking slot available
        :return: assigned slot number
        :rtype: int
        """

        if len(self.__parking_slots) >= self.__max_slots:
            raise self.ParkingSlotFull

        nearest_slot = self.get_nearest_slot()
        new_car = Car(registration_number, driver_age)
        self.__parking_slots[nearest_slot] = new_car

        return nearest_slot

    def vacate_slot(self, slot_number):
        """Removes a car from the parking lot (by it's `slot number`)

        :param slot_number: slot number
        :type slot_number: int
        :raises InvalidSlotNumber: if invalid slot number provided
        """

        if slot_number > self.__max_slots:
            raise self.InvalidSlotNumber

        try:
            vacating_car = self.__parking_slots[slot_number]
        except KeyError:
            raise self.SlotEmpty

        registration_number, driver_age = vacating_car.registration_number, vacating_car.driver_age

        del self.__parking_slots[slot_number]
        self.empty_slots_heap.add(slot_number)

        return registration_number, driver_age

    def get_slot_for_registration_number(self, registration_number):
        """Returns the slot number of the car with `registration number` provided

        :param registration_number: car's registration number
        :type registration_number: str
        :raises self.InvalidRegNumber: if invalid registration number provided
        :return: slot number
        :rtype: int
        """

        for slot_num, car in self.__parking_slots.items():
            if car.registration_number == registration_number:
                return slot_num

        raise self.InvalidRegNumber

    def get_all_slots_for_age(self, driver_age: int):
        """Returns all the slots used by car's having drivers with a particular age

        :param driver_age: car driver's age
        :type driver_age: int
        :raises self.InvalidAge: if no such cars found
        :return: slot numbers
        :rtype: List[int]
        """
        slot_numbers = []
        for slot_num, car in self.__parking_slots.items():
            if car.driver_age == driver_age:
                slot_numbers.append(slot_num)

        if len(slot_numbers) == 0:
            raise self.InvalidAge

        return slot_numbers

    def get_all_cars_for_age(self, driver_age: int):
        """Returns all car's having a particular driver's age

        :param driver_age: car driver's age
        :type driver_age: int
        :raises self.InvalidAge: if no such cars found
        :return: registration numbers
        :rtype: List[str]
        """
        registration_numbers = []
        for car in self.__parking_slots.values():
            if car.driver_age == driver_age:
                registration_numbers.append(car.registration_number)

        if len(registration_numbers) == 0:
            raise self.InvalidAge

        return registration_numbers

    """ Helper functions """

    def get_nearest_slot(self):
        """Returns the nearest slot available currently

        :return: nearest slot
        :rtype: int
        """

        nearest_slot = self.empty_slots_heap.pop()
        if nearest_slot is None:
            return len(self.__parking_slots) + 1

        return nearest_slot
