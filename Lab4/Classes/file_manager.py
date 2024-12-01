import os

class FileManager:
    @staticmethod
    def save_art_to_file(ascii_art):
        directory = 'C:/Users/User/Desktop/nulp-3/Спеціалізовані мови програмування/data'
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_name = input("Enter the filename to save the ASCII art (e.g., art.txt): ")
        full_path = os.path.join(directory, file_name)

        with open(full_path, 'w') as file:
            file.writelines(line + '\n' for line in ascii_art)

        print(f"ASCII art saved to {full_path}")