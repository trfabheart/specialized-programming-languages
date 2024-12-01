import os

class FileManager:
    @staticmethod
    def save_to_file(filename, projection):
        os.makedirs("/Users/admin/Desktop/ДЗ/3 семестр/000/Спеціалізовані мови програмування/laba9/Lab5/Data", exist_ok=True)

        file_path = os.path.join("/Users/admin/Desktop/ДЗ/3 семестр/000/Спеціалізовані мови програмування/Laba9/Lab5/Data", filename)

        try:
            with open(file_path, 'w') as file:
                for row in projection:
                    file.write("".join(row) + "\n")
            print(f"ASCII-art saved to {file_path}")
        except Exception as e:
            print(f"Error saving: {e}")