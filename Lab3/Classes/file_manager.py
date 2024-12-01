from pathlib import Path

class FileManager:
    @staticmethod
    def save_to_file(ascii_art):
        data_dir = Path('C:/Users/User/Desktop/nulp-3/Спеціалізовані мови програмування/data')
        data_dir.mkdir(parents=True, exist_ok=True)

        filename = input("Enter the file name for saving (without extension): ") + '.txt'
        file_path = data_dir / filename

        with file_path.open('w') as f:
            f.write(ascii_art)

        print(f"ASCII art saved to file {file_path}")