import os
import sys

lab4_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(lab4_root)


from Classes.ASCIIart_generator import ArtGenerator
from Classes.art_operations import ArtOperations

def main():
    while True:
        print("Welcome to the ASCII Art Generator!")
        print("1. Create ASCII Art")
        print("2. Exit")
        user_choice = input("Select an option (1 or 2): ").strip()

        if user_choice == '1':
            art_ops = ArtOperations()

            art_ops.text = input("Enter the text to convert to ASCII art: ")
            art_ops.width = int(input("Enter the width (default 10): ") or 10)
            art_ops.height = int(input("Enter the height (default 10): ") or 10)

            art_ops.choose_alignment()
            art_ops.choose_color()

            generator = ArtGenerator(art_ops.char_set, art_ops.width, art_ops.height, art_ops.text)
            ascii_art = generator.generate_art()

            art_ops.display_art(ascii_art)

            print("Do you want to save the ASCII art to a file?")
            print("1. Yes")
            print("2. No")
            save_choice = input("Choose an option (1 or 2): ").strip()

            if save_choice == '1':
                art_ops.save_art_to_file(ascii_art)
            elif save_choice == '2':
                print("ASCII art not saved.")
            else:
                print("Invalid choice. ASCII art not saved.")

        elif user_choice == '2':
            print("Thank you for using the program!")
            break
        else:
            print("Invalid option. Please try again.")