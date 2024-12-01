class FontError(Exception):
    def __init__(self, font):
        self.message = f"Error: Invalid font choice '{font}'."
        super().__init__(self.message)

class ColorError(Exception):
    def __init__(self, color):
        self.message = f"Error: Invalid color choice '{color}'."
        super().__init__(self.message)

class SymbolError(Exception):
    def __init__(self, symbol):
        self.message = "Error: The symbol cannot be empty."
        super().__init__(self.message)