"""
Example Python code demonstrating basic functionality
"""

class Calculator:
    """A simple calculator class"""

    def __init__(self):
        self.history = []

    def add(self, a, b):
        """Add two numbers"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        """Subtract b from a"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        """Multiply two numbers"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        """Divide a by b"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def get_history(self):
        """Return calculation history"""
        return self.history


def main():
    """Main function demonstrating calculator usage"""
    calc = Calculator()

    print("Calculator Demo")
    print("-" * 40)

    # Perform some calculations
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 * 5 = {calc.multiply(10, 5)}")
    print(f"10 / 5 = {calc.divide(10, 5)}")

    print("\nCalculation History:")
    print("-" * 40)
    for entry in calc.get_history():
        print(entry)


if __name__ == "__main__":
    main()
