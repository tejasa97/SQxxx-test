import unittest
from domain.commands.command_manager import CommandManager, Commands
from domain.parking_lot.parking_lot import ParkingLotManager


class Tests(unittest.TestCase):

    def setUp(self):
        """Initialize a new CM and PM for every test
        """
        self.cm = CommandManager()
        self.pm = ParkingLotManager()

    def tearDown(self):
        """Delete the CM and PM instances after every test
        """
        del self.cm
        del self.pm

    def create_parking_lot(self, slot_size=6):
        """Utility to create a parking lot with a size

        :param slot_size: slot size, defaults to 6
        :type slot_size: int, optional
        """

        self.pm = ParkingLotManager()
        self.pm.initialize_slots(num_slots=slot_size)

    def test_add_lot(self):
        """Test adding a new parking lot
        """

        # Test adding a parking lot with valid number
        text = "Create_parking_lot 6"
        command_type, command = self.cm.get_command_from_text(text)

        self.assertEqual(6, int(command['number']))
        self.assertEqual(command_type, Commands.CREATE_NEW_PARKING_LOT)

        self.pm.initialize_slots(num_slots=int(command['number']))

    def test_add_car_to_lot(self):
        """Test parking a car in the lot
        """
        self.create_parking_lot(1)

        # Park when slots available
        text = "Park KA-01-HH-1234 driver_age 21"
        command_type, command = self.cm.get_command_from_text(text)

        self.assertEqual(command_type, Commands.PARK_CAR_WITH_REG_NO)
        self.assertEqual("KA-01-HH-1234", command['registration_number'])
        self.assertEqual(21, int(command['driver_age']))

        slot_num = self.pm.add_car_to_slot(
            registration_number=command['registration_number'], driver_age=int(command['driver_age']))
        self.assertTrue(slot_num, 1)

        # try adding when parking lot is full (INVALID)
        self.assertRaises(
            ParkingLotManager.ParkingSlotFull,
            self.pm.add_car_to_slot,
            registration_number=command['registration_number'], driver_age=int(
                command['driver_age'])
        )

    def test_vacate_car_from_lot(self):
        """Test parking a car in the lot
        """
        self.test_add_car_to_lot()

        # Try vacating INVALID empty slot 2
        self.assertRaises(ParkingLotManager.InvalidSlotNumber, self.pm.vacate_slot, 2)

        # Try vacating VALID slot 1
        text = "Leave 1"
        command_type, command = self.cm.get_command_from_text(text)

        self.assertEqual(command_type, Commands.VACATE_SLOT_NO)
        self.assertEqual(1, int(command['slot_number']))

        registration_number, driver_age = self.pm.vacate_slot(
            slot_number=int(command['slot_number']))
        self.assertEqual(registration_number, "KA-01-HH-1234")
        self.assertEqual(driver_age, 21)

        # Try vacating an INVALID already empty slot (1)
        self.assertRaises(
            ParkingLotManager.SlotEmpty,
            self.pm.vacate_slot,
            slot_number=1
        )

    def test_get_slot_num_for_regn_number(self):
        """Test getting slot number for registration number
        """

        self.test_add_car_to_lot()

        # Try getting slot number for invalid registration number
        self.assertRaises(
            ParkingLotManager.InvalidRegNumber,
            self.pm.get_slot_for_registration_number,
            "KA-0X-XX-XXXX"
        )

        # Try getting slot number for valid registration number
        text = "Slot_number_for_car_with_number KA-01-HH-1234"
        command_type, command = self.cm.get_command_from_text(text)

        self.assertEqual(command_type, Commands.RETURN_SLOT_WITH_REG_NO)
        self.assertEqual("KA-01-HH-1234", command['registration_number'])

    def test_get_slots_for_age(self):
        """Test getting slot numbers for a driver's age
        """

        self.test_add_car_to_lot()

        # Try getting slot numbers for invalid drivers age
        self.assertRaises(
            ParkingLotManager.InvalidAge,
            self.pm.get_all_slots_for_age,
            18
        )

        # Try getting slot number for valid driver's age
        text = "Slot_numbers_for_driver_of_age 21"
        command_type, command = self.cm.get_command_from_text(text)

        self.assertEqual(command_type, Commands.GET_SLOTS_FOR_DRIVER_AGE)
        self.assertEqual(21, int(command['driver_age']))

        slot_numbers = self.pm.get_all_slots_for_age(driver_age=int(command['driver_age']))
        self.assertEqual([1], slot_numbers)

    def test_get_all_cars_for_age(self):
        """Test getting all registration numbers for a driver's age
        """

        self.test_add_car_to_lot()

        # Try getting slot numbers for invalid drivers age
        self.assertRaises(
            ParkingLotManager.InvalidAge,
            self.pm.get_all_cars_for_age,
            18
        )

        # Try getting slot number for valid driver's age
        text = "Vehicle_registration_number_for_driver_of_age 21"
        command_type, command = self.cm.get_command_from_text(text)

        self.assertEqual(command_type, Commands.GET_REG_NOS_FOR_DRIVER_AGE)
        self.assertEqual(21, int(command['driver_age']))

        registration_numbers = self.pm.get_all_cars_for_age(driver_age=int(command['driver_age']))
        self.assertEqual(["KA-01-HH-1234"], registration_numbers)


if __name__ == "__main__":
    unittest.TestLoader.sortTestMethodsUsing = None
    unittest.main()
