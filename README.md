# PLP-CALCULATOR

A simple Python calculator program.

## Usage

This calculator program allows you to perform basic arithmetic operations.

### How to Run
1. Save the code below in a file named `calculator.py`.
2. Run the program with `python calculator.py`.

```python
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter +, -, * or / : ")

    if op == "+":
        print(num1, "+", num2, "=", num1 + num2)
    elif op == "-":
        print(num1, "-", num2, "=", num1 - num2)
    elif op == "*":
        print(num1, "*", num2, "=", num1 * num2)
    elif op == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(num1, "/", num2, "=", num1 / num2)
    else:
        print("Invalid operation.")
except ValueError:
    print("Please enter valid numbers.")
```

## Features
- Addition, subtraction, multiplication, and division
- Handles invalid input
- Checks for division by zero

## License
MIT License
