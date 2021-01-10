# class BaseCommand():

#     keys = []
#     regex_pattern = r''

#     def __init__(self):

#         pass


# class NewCommand(BaseCommand):

#     keys = ['driver']
from domain.commands.command_manager import CommandManager
from domain.parking_lot.parking_lot import ParkingLotManager

pm = ParkingLotManager()
cm = CommandManager()
cm.initialize_commands()

cm.get_command_from_text("Create_parking_lot 6")
cm.get_command_from_text("Park KA-01-HH-1234 driver_age 21")
cm.get_command_from_text("Park PB-01-HH-1234 driver_age 21")
cm.get_command_from_text("Slot_numbers_for_driver_of_age 21")
cm.get_command_from_text("Park PB-01-TG-2341 driver_age 40")
cm.get_command_from_text("Slot_number_for_car_with_number PB-01-HH-1234")
cm.get_command_from_text("Leave 2")
cm.get_command_from_text("Park HR-29-TG-3098 driver_age 39")
cm.get_command_from_text("Vehicle_registration_number_for_driver_of_age 18")
