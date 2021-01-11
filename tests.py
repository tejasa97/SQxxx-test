import unittest
from domain.commands.command_manager import CommandManager, Commands
from domain.parking_lot.parking_lot import ParkingLotManager


class TestStringMethods(unittest.TestCase):

    def setUp(self):

        self.cm = CommandManager()
        self.pm = ParkingLotManager()

    def tearDown(self):

        del self.cm
        del self.pm

    def test_add_lot(self):
        """Test adding a new parking lot
        """
        text = "Create_parking_lot 6"

        command_type, command = self.cm.get_command_from_text(text)

        self.assertEqual(6, int(command['number']))
        self.assertEqual(command_type, Commands.CREATE_NEW_PARKING_LOT)

        self.pm.initialize_slots(num_slots=int(command['number']))

    def test_add_car_to_lot(self):
        """Test parking a car in the lot
        """
        self.test_add_lot()

        text = "Park KA-01-HH-1234 driver_age 21"

        command_type, command = self.cm.get_command_from_text(text)
        self.assertEqual(command_type, Commands.PARK_CAR_WITH_REG_NO)

        self.assertEqual("KA-01-HH-1234", command['registration_number'])
        self.assertEqual(21, int(command['driver_age']))

        slot_num = self.pm.add_car_to_slot(
            registration_number=command['registration_number'], driver_age=int(command['driver_age']))

        self.assertTrue(slot_num, 1)

    def test_vacate_car_from_lot(self):
        """Test parking a car in the lot
        """
        self.test_add_car_to_lot()

        text = "Leave 1"
        command_type, command = self.cm.get_command_from_text(text)

        self.assertEqual(command_type, Commands.VACATE_SLOT_NO)
        self.assertEqual(1, int(command['slot_number']))


if __name__ == "__main__":
    unittest.TestLoader.sortTestMethodsUsing = None
    unittest.main()
