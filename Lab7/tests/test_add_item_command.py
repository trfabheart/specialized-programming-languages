import unittest
from unittest.mock import Mock, patch
from Commands.add_item_command import AddItemCommand
from Core.user_interface import UserInterface
from Commands.show_history_command import History

class TestAddItemCommand(unittest.TestCase):
    def setUp(self):
        self.user_interface = Mock(spec=UserInterface)
        self.history = Mock(spec=History)
        self.data = []  # Загальний список елементів
        self.local_data = []  # Локальний список для нових елементів
        self.command = AddItemCommand(self.user_interface, self.history, self.data, self.local_data, "posts")

    @patch('builtins.input', side_effect=["1", "Test", "Testing programm"])
    def test_execute_add_post(self, mock_input):
        # Виконання команди
        self.command.execute()

        # Перевірка, що новий елемент додано до local_data
        self.assertEqual(len(self.local_data), 1)
        self.assertEqual(self.local_data[0]["userId"], 1)
        self.assertEqual(self.local_data[0]["title"], "Test")
        self.assertEqual(self.local_data[0]["body"], "Testing programm")

