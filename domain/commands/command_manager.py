import re
from domain.utils import Singleton
from enum import Enum
from .commands import *


class CommandManager(metaclass=Singleton):
    """Class that manages all available commands
    """
    class CommandNotFound(Exception):
        """Raised when an invalid command is found
        """
        ...

    def __init__(self):

        self.commands = []
        self.initialize_commands()

    def initialize_commands(self):
        """Adds all available commands to inventory
        """
        self.commands = [command() for command in BaseCommand.__subclasses__()]

    def get_command_from_text(self, text: str):
        """Returns an available command for the provided text

        :param text: command text
        :type text: str
        :raises CommandNotFound: if no appropriate command found
        :return: Command type Enum, Command data
        :rtype: tuple(enum, dict)
        """
        cleaned_text = text.strip()

        for command in self.commands:
            command_data = command.check_if_match(cleaned_text)
            if command_data is not None:
                return(command.command_type, command_data)

        raise self.CommandNotFound(cleaned_text)
