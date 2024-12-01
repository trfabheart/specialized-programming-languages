from Commands.load_data_command import LoadDataCommand
from Commands.display_data_command import DisplayDataCommand
from Commands.add_item_command import AddItemCommand
from Commands.delete_item_command import DeleteItemCommand
from Commands.save_data_command import SaveDataCommand
from Commands.show_history_command import ShowHistoryCommand, History
from Core.user_interface import UserInterface
from Core.data_saver import DataSaver

def main():
    user_interface = UserInterface()
    history = History()
    data_saver = DataSaver()

    posts = []
    local_posts = []
    albums = []
    local_albums = []

    while True:
        print("\nMain menu:")
        print("1. Download data.")
        print("2. Show posts.")
        print("3. Add new post.")
        print("4. Delete post.")
        print("5. Show albums.")
        print("6. Add new album.")
        print("7. Delete album.")
        print("8. Save posts in file.")
        print("9. Save albums in file.")
        print("10. Show history")
        print("0. Exit.")

        choice = input("Select option: ").strip()

        match choice:
            case "1":
                LoadDataCommand(user_interface, history, posts, albums).execute()
            case "2":
                DisplayDataCommand(user_interface, posts + local_posts, "posts").execute()
            case "3":
                AddItemCommand(user_interface, history, posts, local_posts, "posts").execute()
            case "4":
                DeleteItemCommand(user_interface, history, local_posts, "posts").execute()
            case "5":
                DisplayDataCommand(user_interface, albums + local_albums, "albums").execute()
            case "6":
                AddItemCommand(user_interface, history, albums, local_albums, "albums").execute()
            case "7":
                DeleteItemCommand(user_interface, history, local_albums, "albums").execute()
            case "8":
                SaveDataCommand(user_interface, data_saver, posts + local_posts, "posts").execute()
            case "9":
                SaveDataCommand(user_interface, data_saver, albums + local_albums, "albums").execute()
            case "10":
                ShowHistoryCommand(user_interface, history).execute()
            case "0":
                print("Exit from programm!")
                break
            case _:
                print("Error: Incorrect option. Please, try again!")



