from Classes.ascii_art_service import AsciiArtService
from Classes.cylinder import Cylinder
from Classes.sphere import Sphere

def user_interface():
    ascii_art_service = AsciiArtService()

    while True:
        ascii_art_service.display_ascii_art()

        print("\n=== Main Menu ===")
        print("1. Select shape: cube, cylinder or sphere.")
        print("2. Set size.")
        print("3. Set height (for cylinder only).")
        print("4. Rotate shape.")
        print("5. Save ASCII art to file.")
        print("6. Set color.")
        print("7. Exit.")
        choice = input("Choose an option: ").strip()

        match choice:
            case '1':
                shape_type = input("Enter shape type (cube, cylinder, sphere): ").strip().lower()
                size = int(input("Enter size of the shape: "))
                height = int(input("Enter height (for cylinder): ")) if shape_type == "cylinder" else None
                
                ascii_art_service.set_shape(shape_type, size, height)
            case '2':
                if ascii_art_service.shape:
                    size = int(input("Enter new size for the shape: "))
                    ascii_art_service.shape.size = size
                else:
                    print("Shape is not selected. Please select a shape first.")
            case '3':
                if isinstance(ascii_art_service.shape, Cylinder):
                    height = int(input("Enter new height for the cylinder: "))
                    ascii_art_service.shape.height = height
                else:
                    print("Height adjustment is only available for cylinders.")
            case '4':
                if ascii_art_service.shape:
                    angle_x = float(input("Enter rotation angle around X-axis (degrees): "))
                    angle_y = float(input("Enter rotation angle around Y-axis (degrees): "))
                    angle_z = float(input("Enter rotation angle around Z-axis (degrees): "))
                    ascii_art_service.rotate_shape(angle_x, angle_y, angle_z)
                else:
                    print("Shape is not selected. Please select a shape first.")
            case '5':
                filename = input("Enter the filename to save (with .txt extension): ")
                ascii_art_service.save_to_file(filename)
            case '6':
                print("Available colors:", ", ".join(ascii_art_service.color_service.list_colors()))
                color_name = input("Choose a color: ").strip()
                ascii_art_service.set_color(color_name)
            case '7':
                print("Exiting!")
                break
            case _:
                print("Invalid option. Please try again.")