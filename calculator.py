import math

def add(x, y):    # Addition
    return x + y

def subtract(x, y):    # Substraction
    return x - y

def multiply(x, y):    # Multiplication
    return x * y

def divide(x, y):    # Division
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

if __name__ == "__main__":
    # Sample usage
    num1 = 10
    num2 = 5

    print("Addition:", add(num1, num2))
    print("Subtraction:", subtract(num1, num2))
    print("Multiplication:", multiply(num1, num2))
    print("Division:", divide(num1, num2))
