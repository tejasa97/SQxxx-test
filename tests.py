import unittest
from domain.commands.command_manager import CommandManager, Commands
from domain.parking_lot.parking_lot import ParkingLotManager

cm = CommandManager()
pm = ParkingLotManager()


class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # cm = CommandManager()
        # pm = ParkingLotManager()
        pass

    def test_add_lot(self):
        """[summary]
        """
        text = "Create_parking_lot 6"

        command_type, command = cm.get_command_from_text(text)
        self.assertEqual(command_type, Commands.CREATE_NEW_PARKING_LOT)

    def test_add_lot(self):
        """[summary]
        """
        text = "Create_parking_lot 6"

        command_type, command = cm.get_command_from_text(text)
        self.assertEqual(command_type, Commands.CREATE_NEW_PARKING_LOT)

    # # Returns True if the string is in upper case.
    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')


if __name__ == "__main__":
    unittest.main()
