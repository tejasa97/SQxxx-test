# import re
# from commands.command_manager import BaseCommand
# from commands.command_manager import Commands


# class CreateParkingLot(BaseCommand):

#     keys = ['number']
#     regex_pattern = re.compile(r'^Create_parking_lot\s(\d+)$')


# class ParkCar(BaseCommand):

#     command_type = Commands.PARK_CAR_WITH_REG_NO
#     keys = ['registration_number', 'driver_age']
#     regex_pattern = re.compile(r'^Park\s([-\w]{13})\sdriver_age\s(\d+)$')


# class GetSlotsForDriverAge(BaseCommand):

#     keys = ['driver_age']
#     regex_pattern = re.compile(r'^Slot_numbers_for_driver_of_age\s(\d+)$')


# class GetSlotForRegnNumber(BaseCommand):

#     keys = ['registration_number']
#     regex_pattern = re.compile(r'^Slot_number_for_car_with_number\s([-\w]{13})$')


# class VacateSlot(BaseCommand):

#     keys = ['slot_number']
#     regex_pattern = re.compile(r'^Leave\s(\d+)$')


# class GetRegnNumbersForDriverAge(BaseCommand):

#     keys = ['driver_age']
#     regex_pattern = re.compile(r'^Vehicle_registration_number_for_driver_of_age\s(\d+)$')
