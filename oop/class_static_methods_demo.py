# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method
    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    # Class method
    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers and print the calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
