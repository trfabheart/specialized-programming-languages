import os
import sys

lab3_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(lab3_root)

from Classes.art_operations import ArtOperations
from Classes.ascii_art import AsciiArtGenerator
from Classes.color_utils import ColorManager
from Classes.file_manager import FileManager
from Classes.fonts import FontManager
from Classes.error_handler import FontError, ColorError, SymbolError

def display_menu():
    print("\n" + "=" * 30)
    print("        ASCII ART Generator")
    print("=" * 30)
    print("1 - Create new ASCII art")
    print("2 - Exit the program")
    print("=" * 30)

def main():
    while True:
        display_menu()

        choice = input("Your choice (1 or 2): ").strip()

        if choice == '1':
            text = input("Enter text to create ASCII art: ")

            try:
                font_manager = FontManager()
                font_choice = font_manager.select_font()

                symbol = input("Enter symbol to create ASCII art: ")
                art_generator = AsciiArtGenerator(text, font_choice, symbol)
                ascii_art = art_generator.generate_art()

                color_manager = ColorManager()
                color_choice = color_manager.select_color()
                ascii_art_colored = color_manager.get_colored_art(ascii_art, color_choice)

                print("\nASCII art with selected symbols:")
                print(ascii_art_colored)

                art_operations = ArtOperations(ascii_art)
                art_operations.change_symbol(color_choice, color_manager)

                resize_option = input("Do you want to resize the ASCII art? (yes/no): ").strip().lower()
                if resize_option in ['yes']:
                    resized_art = art_generator.resize_art()
                    ascii_art_colored = color_manager.get_colored_art(resized_art, color_choice)
                    print("\nASCII art with new size:")
                    print(ascii_art_colored)

                save_option = input("Save ASCII art to file? (yes/no): ").strip().lower()
                if save_option in ['yes']:
                    FileManager.save_to_file(ascii_art)

            except (FontError, ColorError, SymbolError) as e:
                print(e)
            except ValueError as e:
                print(e)

        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1 or 2.")
