
# Basic Calculator Program

# Ask the user to enter two numbers
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Ask the user to enter a math operation
op = input("Enter +, -, * or / : ")

# Convert the numbers to integers
num1 = int(num1)
num2 = int(num2)

# Do the calculation based on the operation
if op == "+":
    print(num1, "+", num2, "=", num1 + num2)
elif op == "-":
    print(num1, "-", num2, "=", num1 - num2)
elif op == "*":
    print(num1, "*", num2, "=", num1 * num2)
elif op == "/":
    print(num1, "/", num2, "=", num1 / num2)
else:
    print("Invalid operation.")
