from classes import Calculator

def get_menu_choice(prompt):
    while True:
        choice = input(prompt)
        if choice.isdigit() and 1 <= int(choice) <= 6:
            return int(choice)
        print("Invalid choice! Please enter a number between 1 and 6.")

def main():
    calc = Calculator()

    while True:
        print("\nCalculator Menu:")
        print("1. Calculate")
        print("2. Show History")
        print("3. Get Memory")
        print("4. Clear Memory")
        print("5. Set Decimal Precision")
        print("6. Exit")

        choice = get_menu_choice("Choose an option: ")

        if choice == 1:
            try:
                calc.run()
            except (ZeroDivisionError, ValueError) as e:
                print(e)
        elif choice == 2:
            calc.history.show_history()
        elif choice == 3:
            print(f"Memory Value: {calc.memory.get_memory()}")
        elif choice == 4:
            calc.memory.clear_memory()
            print("Memory cleared.")
        elif choice == 5:
            try:
                calc.decimal_point.set_decimal_point()
            except (ValueError) as e:
                print(e)
        elif choice == 6:
            print("Exiting calculator.")
            break