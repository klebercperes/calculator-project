#!/usr/bin/env python3
"""
Advanced Calculator - Performs all basic math operations
Supports: +, -, *, /, **, sqrt, %, factorial, trigonometric functions
"""

import math
import sys

class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Addition: a + b"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtraction: a - b"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiplication: a * b"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Division: a / b"""
        if b == 0:
            return "Error: Division by zero!"
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, a, b):
        """Power: a ** b"""
        result = a ** b
        self.history.append(f"{a} ** {b} = {result}")
        return result
    
    def square_root(self, a):
        """Square root: √a"""
        if a < 0:
            return "Error: Cannot calculate square root of negative number!"
        result = math.sqrt(a)
        self.history.append(f"√{a} = {result}")
        return result
    
    def modulo(self, a, b):
        """Modulo: a % b"""
        if b == 0:
            return "Error: Modulo by zero!"
        result = a % b
        self.history.append(f"{a} % {b} = {result}")
        return result
    
    def factorial(self, a):
        """Factorial: a!"""
        if a < 0:
            return "Error: Factorial of negative number!"
        if not isinstance(a, int) or a != int(a):
            return "Error: Factorial only for integers!"
        if a > 170:  # Prevent overflow
            return "Error: Number too large for factorial!"
        result = math.factorial(int(a))
        self.history.append(f"{int(a)}! = {result}")
        return result
    
    def sine(self, a):
        """Sine: sin(a) in radians"""
        result = math.sin(a)
        self.history.append(f"sin({a}) = {result}")
        return result
    
    def cosine(self, a):
        """Cosine: cos(a) in radians"""
        result = math.cos(a)
        self.history.append(f"cos({a}) = {result}")
        return result
    
    def tangent(self, a):
        """Tangent: tan(a) in radians"""
        result = math.tan(a)
        self.history.append(f"tan({a}) = {result}")
        return result
    
    def logarithm(self, a, base=10):
        """Logarithm: log_base(a)"""
        if a <= 0:
            return "Error: Logarithm of non-positive number!"
        if base <= 0 or base == 1:
            return "Error: Invalid logarithm base!"
        result = math.log(a, base)
        self.history.append(f"log_{base}({a}) = {result}")
        return result
    
    def natural_log(self, a):
        """Natural logarithm: ln(a)"""
        if a <= 0:
            return "Error: Natural logarithm of non-positive number!"
        result = math.log(a)
        self.history.append(f"ln({a}) = {result}")
        return result
    
    def absolute(self, a):
        """Absolute value: |a|"""
        result = abs(a)
        self.history.append(f"|{a}| = {result}")
        return result
    
    def show_history(self):
        """Display calculation history"""
        if not self.history:
            print("No calculations in history.")
            return
        print("\n--- Calculation History ---")
        for i, calc in enumerate(self.history, 1):
            print(f"{i}. {calc}")
    
    def clear_history(self):
        """Clear calculation history"""
        self.history.clear()
        print("History cleared!")

def get_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_integer(prompt):
    """Get a valid integer from user input"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*50)
    print("           ADVANCED CALCULATOR")
    print("="*50)
    print("1.  Addition (+)")
    print("2.  Subtraction (-)")
    print("3.  Multiplication (*)")
    print("4.  Division (/)")
    print("5.  Power (**)")
    print("6.  Square Root (√)")
    print("7.  Modulo (%)")
    print("8.  Factorial (!)")
    print("9.  Sine (sin)")
    print("10. Cosine (cos)")
    print("11. Tangent (tan)")
    print("12. Logarithm (log)")
    print("13. Natural Logarithm (ln)")
    print("14. Absolute Value (|x|)")
    print("15. Show History")
    print("16. Clear History")
    print("0.  Exit")
    print("="*50)

def main():
    """Main calculator function"""
    calc = Calculator()
    
    print("Welcome to the Advanced Calculator!")
    print("This calculator supports all basic and advanced math operations.")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (0-16): ").strip()
            
            if choice == "0":
                print("Thank you for using the calculator! Goodbye!")
                break
            
            elif choice == "1":  # Addition
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.add(a, b)
                print(f"Result: {result}")
            
            elif choice == "2":  # Subtraction
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.subtract(a, b)
                print(f"Result: {result}")
            
            elif choice == "3":  # Multiplication
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.multiply(a, b)
                print(f"Result: {result}")
            
            elif choice == "4":  # Division
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.divide(a, b)
                print(f"Result: {result}")
            
            elif choice == "5":  # Power
                a = get_number("Enter base: ")
                b = get_number("Enter exponent: ")
                result = calc.power(a, b)
                print(f"Result: {result}")
            
            elif choice == "6":  # Square Root
                a = get_number("Enter number: ")
                result = calc.square_root(a)
                print(f"Result: {result}")
            
            elif choice == "7":  # Modulo
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.modulo(a, b)
                print(f"Result: {result}")
            
            elif choice == "8":  # Factorial
                a = get_integer("Enter integer: ")
                result = calc.factorial(a)
                print(f"Result: {result}")
            
            elif choice == "9":  # Sine
                a = get_number("Enter angle in radians: ")
                result = calc.sine(a)
                print(f"Result: {result}")
            
            elif choice == "10":  # Cosine
                a = get_number("Enter angle in radians: ")
                result = calc.cosine(a)
                print(f"Result: {result}")
            
            elif choice == "11":  # Tangent
                a = get_number("Enter angle in radians: ")
                result = calc.tangent(a)
                print(f"Result: {result}")
            
            elif choice == "12":  # Logarithm
                a = get_number("Enter number: ")
                base = get_number("Enter base (default 10): ")
                result = calc.logarithm(a, base)
                print(f"Result: {result}")
            
            elif choice == "13":  # Natural Logarithm
                a = get_number("Enter number: ")
                result = calc.natural_log(a)
                print(f"Result: {result}")
            
            elif choice == "14":  # Absolute Value
                a = get_number("Enter number: ")
                result = calc.absolute(a)
                print(f"Result: {result}")
            
            elif choice == "15":  # Show History
                calc.show_history()
            
            elif choice == "16":  # Clear History
                calc.clear_history()
            
            else:
                print("Invalid choice! Please enter a number between 0-16.")
        
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()