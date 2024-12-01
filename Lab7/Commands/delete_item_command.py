from Commands.command import Command
from Core.user_interface import UserInterface
from colorama import Fore

class DeleteItemCommand(Command):
    def __init__(self, user_interface, history, local_data, data_type="posts"):
        self.user_interface = user_interface
        self.history = history
        self.local_data = local_data
        self.data_type = data_type

    def execute(self):
        try:
            delete_id = int(input(f"Enter ID {self.data_type[:-1]} to delete: "))
            item_to_delete = next((item for item in self.local_data if item["id"] == delete_id), None)
            if item_to_delete:
                self.local_data.remove(item_to_delete)
                self.history.log_request(f"DELETE /{self.data_type}", item_to_delete)
                self.user_interface.display_message(f"{self.data_type[:-1].capitalize()} with ID {delete_id} deleted.", color=Fore.GREEN)
            else:
                self.user_interface.display_message(f"{self.data_type[:-1].capitalize()} with ID {delete_id} not found or cannot be deleted. Please, try again!", color=Fore.RED)
        except ValueError:
            self.user_interface.display_message("Error: Please, try again!", color=Fore.RED)
