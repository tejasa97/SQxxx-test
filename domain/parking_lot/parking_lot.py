from .car import Car
from .utils import Heap


class ParkingLotManager():

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

    def initialize_slots(self, num_slots):
        """Initializes the parking lot with a definite number of slots

        :param num_slots: number of slots
        :type num_slots: int
        """

        self.__max_slots = num_slots

        self.__parking_slots = {}
        self.empty_slots_heap = Heap()

    def add_car_to_slot(self, registration_number, driver_age):
        """[summary]

        :param registration_number: [description]
        :type registration_number: [type]
        :param driver_age: [description]
        :type driver_age: [type]
        :raises self.ParkingSlotFull: [description]
        :return: [description]
        :rtype: [type]
        """

        if len(self.__parking_slots) >= self.__max_slots:
            raise self.ParkingSlotFull

        nearest_slot = self.get_nearest_slot()
        new_car = Car(registration_number, driver_age)
        self.__parking_slots[nearest_slot] = new_car

        return nearest_slot

    def vacate_slot(self, slot_number):
        """[summary]

        :param slot_number: [description]
        :type slot_number: [type]
        :raises InvalidSlotNumber: [description]
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
        """[summary]

        :param registration_number: [description]
        :type registration_number: [type]
        :raises self.InvalidRegNumber: [description]
        :return: [description]
        :rtype: [type]
        """

        for slot_num, car in self.__parking_slots.items():
            if car.registration_number == registration_number:
                return slot_num

        raise self.InvalidRegNumber

    def get_all_slots_for_age(self, driver_age):

        slot_numbers = []
        for slot_num, car in self.__parking_slots.items():
            if car.driver_age == driver_age:
                slot_numbers.append(slot_num)

        if len(slot_numbers) == 0:
            raise self.InvalidAge

        return slot_numbers

    def get_all_cars_for_age(self, driver_age):

        registration_numbers = []
        for car in self.__parking_slots.values():
            if car.driver_age == driver_age:
                print("adding")
                registration_numbers.append(car.registration_number)

        if len(registration_numbers) == 0:
            raise self.InvalidAge

        return registration_numbers

    """ Helper functions """

    def get_nearest_slot(self):
        """[summary]
        """

        nearest_slot = self.empty_slots_heap.pop()
        if nearest_slot is None:
            return len(self.__parking_slots) + 1

        return nearest_slot
