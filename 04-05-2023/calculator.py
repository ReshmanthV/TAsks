"""
    This code is for a basic calculator.
"""


def addition(operand_1, operand_2):
    """This function returns addition of two numbers"""
    return operand_1 + operand_2


def subtraction(operand_1, operand_2):
    """This function returns subtraction of two numbers"""
    return operand_1 - operand_2


def multiplication(operand_1, operand_2):
    """"This function returns multiplication of two numbers"""
    return operand_1 * operand_2


def division(operand_1, operand_2):
    """This function returns division of two numbers"""
    return operand_1 / operand_2


operand1 = float(input("Enter operand_1 : "))
operand2 = float(input("Enter operand2 : "))
print()
print("For Addition -- '+'")
print("For Subtraction -- '-'")
print("For Multiplication -- '*'")
print("For Division -- '/'")
print()
operation = input("Select Operation : ")

if operation == '+':
    print("Result : ", addition(operand1, operand2))
elif operation == '-':
    print("Result : ", subtraction(operand1, operand2))
elif operation == '*':
    print("Result : ", multiplication(operand1, operand2))
elif operation == '/':
    print("Result : ", division(operand1, operand2))
