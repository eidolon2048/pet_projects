class Calculator:

    def __init__(self):
        self.colour = "black"
        self.weight= 230
        self.manufacturer = "CASIO"
        self.model = "FX-85GT CW"
        self.country_of_origin = "Japan"

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    
    def power(self, a, b):
        return a ** b
    
    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot take square root of negative number.")
        return a ** 0.5

def main():
    calculator = Calculator()

    num1 = int(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /, ^, sqrt ): ")
    num2 = int(input("Enter second number: "))

    if operator == "+":
        result = calculator.add(num1, num2)
    elif operator == "-":
        result = calculator.subtract(num1, num2)
    elif operator == "*":
        result = calculator.multiply(num1, num2)
    elif operator == "/":
        result = calculator.divide(num1, num2)
    elif operator == "^":
        result = calculator.power(num1, num2)
    elif operator == "sqrt":
        result = calculator.square_root(num1)
    else:
        print("Invalid operator")
    return print(f"Answer: {result}")
    
if __name__ == "__main__":
    main()