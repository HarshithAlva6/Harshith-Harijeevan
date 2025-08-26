class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: Division by zero"

    def calculate(self, operation):
        operation = operation.lower()
        if operation == "add":
            return self.add()
        elif operation == "subtract":
            return self.subtract()
        elif operation == "multiply":
            return self.multiply()
        elif operation == "divide":
            return self.divide()
        else:
            return "Invalid operation, Try again!"

if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter operation \n(add, subtract, multiply, divide): ")

    c = Calculator(a, b)
    result = c.calculate(operation)
    print(f"Result: {result}")
