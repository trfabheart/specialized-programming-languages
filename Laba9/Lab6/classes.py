import math
from variables import memory, history, decimal_point

class Memory:
    def __init__(self):
        self.__memory = memory

    def set_memory(self, value):
        self.__memory = value

    def get_memory(self):
        return self.__memory

    def clear_memory(self):
        self.__memory = 0

class History:
    def __init__(self):
        self.__history = history

    def add_to_history(self, expression, result):
        self.__history.append(f"{expression} = {result}")

    def show_history(self):
        if self.__history:
            print("Calculation History:")
            for entry in self.__history:
                print(entry)
        else:
            print("No history available.")

class DecimalPoint:
    def __init__(self):
        self.__decimal_point = decimal_point

    def set_decimal_point(self):
        point = input("Enter number of symbols after decimal point: ")
        if not point.isdigit() or int(point) < 0:
            raise ValueError("Please enter a non-negative integer.")
        self.__decimal_point = int(point)
        print(f"Number of symbols after decimal point: {self.__decimal_point}")

    def get_decimal_point(self):
        return self.__decimal_point

class BaseCalculator:
    def __init__(self):
        self.memory = Memory()
        self.history = History()
        self.decimal_point = DecimalPoint()

    def check_operator(self, operator):
        return operator in {'+', '-', '*', '/', '^', '√', '%'}

    def get_operator(self):
        while True:
            operator = input("Choose an operator (+, -, *, /, ^, √, %): ")
            if self.check_operator(operator):
                return operator
            print("Incorrect operator! Please try again.")

    def get_input(self):
        try:
            num1_input = input("Enter first number or 'm' to use memory: ")
            num1 = self.memory.get_memory() if num1_input.lower() == 'm' else float(num1_input)
            
            operator = self.get_operator()
            
            num2 = None
            if operator != '√':
                num2_input = input("Enter second number or 'm' to use memory: ")
                num2 = self.memory.get_memory() if num2_input.lower() == 'm' else float(num2_input)
            
            return num1, operator, num2
        except ValueError:
            print("Invalid input. Try again.")
            return self.get_input()

    def get_yes_no_input(self, prompt):
        while True:
            choice = input(prompt).lower()
            if choice in {'y', 'n'}:
                return choice
            else:
                print("Invalid input! Please enter 'y' or 'n'.")

class Calculator(BaseCalculator):
    def calculate(self, num1, operator, num2):
        decimal_point = self.decimal_point.get_decimal_point()
        
        match operator:
            case '+':
                return round(num1 + num2, decimal_point)
            case '-':
                return round(num1 - num2, decimal_point)
            case '*':
                return round(num1 * num2, decimal_point)
            case '/':
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                return round(num1 / num2, decimal_point)
            case '^':
                return round(math.pow(num1, num2), decimal_point)
            case '√':
                if num1 < 0:
                    raise ValueError("Cannot take square root of a negative number.")
                return round(math.sqrt(num1), decimal_point)
            case '%':
                if num2 == 0:
                    raise ZeroDivisionError("Cannot take percentage with zero.")
                return round(num1 % num2, decimal_point)

    def run(self):
        while True:
            num1, operator, num2 = self.get_input()
            result = self.calculate(num1, operator, num2)
            print(f"Result: {result}")
            self.history.add_to_history(f"{num1} {operator} {num2 if num2 is not None else ''}", result)
            
            if self.get_yes_no_input("Save result? (y/n): ") == 'y':
                self.memory.set_memory(result)
                print(f"Result {result} saved to memory.")
            
            if self.get_yes_no_input("New calculation? (y/n): ") == 'n':
                break