
from argparse import ArgumentParser
import os.path

from domain.commands.command_manager import CommandManager, Commands
from domain.parking_lot.parking_lot import ParkingLotManager
import pdb


def is_valid_file(parser, arg):
    """Checks if provided filename is valid
    """

    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)

    return arg


if __name__ == '__main__':
    parser = ArgumentParser(description="command input file")
    parser.add_argument("-i", dest="filename", required=True,
                        help="input file with commands", metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))
    args = parser.parse_args()
    file_pointer = open(args.filename, 'r')

    cm = CommandManager()
    pm = ParkingLotManager()

    while True:
        line = file_pointer.readline()
        if not line:
            break

        try:
            command_type, command = cm.get_command_from_text(line)
        except CommandManager.CommandNotFound:
            print("***Error: Invalid command found! Skipping ...")

        # Check commands
        if command_type == Commands.CREATE_NEW_PARKING_LOT:
            pm.initialize_slots(num_slots=int(command['number']))
            print(
                f"""Created parking of {command['number']} slots"""
            )

        elif command_type == Commands.PARK_CAR_WITH_REG_NO:
            try:
                slot_num = pm.add_car_to_slot(
                    registration_number=command['registration_number'], driver_age=int(command['driver_age']))
                print(
                    f"""Car with vehicle registration number "{command['registration_number']}" has been parked at slot number {slot_num}"""
                )

            except ParkingLotManager.ParkingSlotFull:
                print("***Error: Sorry, it appears the parking lot is full!")

        elif command_type == Commands.GET_SLOTS_FOR_DRIVER_AGE:
            try:
                slot_numbers = pm.get_all_slots_for_age(driver_age=int(command['driver_age']))
                print(
                    f"""{','.join(map(str, slot_numbers))}"""
                )
            except ParkingLotManager.InvalidAge:
                print(f"null")

        elif command_type == Commands.RETURN_SLOT_WITH_REG_NO:
            try:
                slot_number = pm.get_slot_for_registration_number(
                    registration_number=command['registration_number'])
                print(
                    f"""{slot_number}"""
                )

            except ParkingLotManager.InvalidRegNumber:
                print("***Error: Sorry, invalid registration number provided!")

        elif command_type == Commands.VACATE_SLOT_NO:
            try:
                registration_number, driver_age = pm.vacate_slot(
                    slot_number=int(command['slot_number']))
                print(
                    f"""Slot number {2} vacated, the car with vehicle registration number "{registration_number}" left the space, the driver of the car was of age {driver_age}"""
                )

            except ParkingLotManager.InvalidSlotNumber:
                print("***Error: Sorry, it appears you are requesting an invalid slot number!")
            except ParkingLotManager.SlotEmpty:
                print("Slot already vacant")

        elif command_type == Commands.GET_REG_NOS_FOR_DRIVER_AGE:
            try:
                registration_numbers = pm.get_all_cars_for_age(
                    driver_age=int(command['driver_age']))
                print(
                    f"""{','.join(registration_numbers)}"""
                )

            except ParkingLotManager.InvalidAge:
                print(f"""null""")
