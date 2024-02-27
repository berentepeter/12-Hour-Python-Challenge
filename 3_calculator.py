# Write a function that takes two numbers and a mathematical 
# operation (add, subtract, multiply, divide) as parameters 
# and returns the result of that operation.

def calculator(num1: float, num2: float, operation: str) -> float:
    if operation not in ('+', '-', '*', '/'):
        print('Invalid operation! Please use the following operations: +, -, *, /');
        return None;
    elif operation == '/' and num2 == 0:
        print('Invalid operation! Cannot divide by zero.');
        return None;
    if operation == '+':
        return num1 + num2;
    elif operation == '-':
        return num1 - num2;
    elif operation == '*':
        return num1 * num2;
    elif operation == '/':
        return num1 / num2;
