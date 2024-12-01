class AlignmentManager:

    def __init__(self):
        self.alignment = "center"

    def choose_alignment(self):
        print("Select text alignment:")
        print("1. Left")
        print("2. Center")
        print("3. Right")

        option = input("Choose an option (1, 2, or 3): ").strip()
        if option == '1':
            self.alignment = "left"
        elif option == '2':
            self.alignment = "center"
        elif option == '3':
            self.alignment = "right"
        else:
            print("Invalid choice. Defaulting to center alignment.")
            self.alignment = "center"

    def _align_line(self, line, width):
        if self.alignment == 'left':
            return line.ljust(width)
        elif self.alignment == 'center':
            return line.center(width)
        elif self.alignment == 'right':
            return line.rjust(width)
        return line