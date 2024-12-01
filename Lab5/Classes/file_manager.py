import os

class FileManager:
    @staticmethod
    def save_to_file(filename, projection):
        os.makedirs("C:/Users/User/Desktop/nulp-3/Спеціалізовані мови програмування/Lab5/Data", exist_ok=True)

        file_path = os.path.join("C:/Users/User/Desktop/nulp-3/Спеціалізовані мови програмування/Lab5/Data", filename)

        try:
            with open(file_path, 'w') as file:
                for row in projection:
                    file.write("".join(row) + "\n")
            print(f"ASCII-art saved to {file_path}")
        except Exception as e:
            print(f"Error saving: {e}")