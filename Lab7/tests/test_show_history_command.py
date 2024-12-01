from unittest import TestCase
from unittest.mock import MagicMock
from Commands.show_history_command import ShowHistoryCommand
from Core.user_interface import UserInterface


class TestShowHistoryCommand(TestCase):
    def test_execute(self):
        # Мокаємо UserInterface
        mock_ui = MagicMock(UserInterface)
        # Створюємо об'єкт історії з даними
        mock_history = MagicMock()
        mock_history.history = [{'request': 'GET /posts', 'response': [{'id': 1, 'title': 'Test'}]}]

        # Створюємо команду
        command = ShowHistoryCommand(mock_ui, mock_history)

        # Виконуємо команду
        command.execute()

        # Перевіряємо, що метод відображення повідомлення був викликаний
        mock_ui.display_message.assert_called_with("History:")
        mock_history.show_history.assert_called_once()  # Перевіряємо, що викликано show_history()
