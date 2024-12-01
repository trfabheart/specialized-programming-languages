import json

class ColorService:
    def __init__(self):
        self.color_code = ""
        self.colors = self._load_colors()

    def _load_colors(self):
        with open(
            '/Users/admin/Desktop/ДЗ/3 семестр/000/Спеціалізовані мови програмування/Laba9/Lab4/Config/colors.json', 'r', encoding='utf-8',
        ) as file:
            data = json.load(file)
            return data["colors"]

    def choose_color(self):
        print("Choose a color for ASCII art:")
        for color_name in self.colors.keys():
            print(color_name)

        selected_color = input("Enter your choice: ").strip()
        self.color_code = self.colors.get(selected_color, "0")

    def apply_color(self, text):
        return f"\033[{self.color_code}m{text}\033[0m"