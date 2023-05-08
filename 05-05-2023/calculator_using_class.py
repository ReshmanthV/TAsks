"""This code is for a basic calculator using classes."""


class Calculator:
    """This class contains methods for operations."""

    def __init__(self, operand1, operand2):
        self.operand_1 = operand1
        self.operand_2 = operand2

    def addition(self):
        """This method returns addition of two numbers"""
        return self.operand_1 + self.operand_2

    def subtraction(self):
        """This method returns subtraction of two numbers"""
        return self.operand_1 - self.operand_2

    def multiplication(self):
        """"This method returns multiplication of two numbers"""
        return self.operand_1 * self.operand_2

    def division(self):
        """This method returns division of two numbers"""
        try:
            res = self.operand_1 / self.operand_2
        except ZeroDivisionError:
            print(ZeroDivisionError)
            exit(0)
        return res


try:
    input1 = float(input("Enter operand_1 : "))
    input2 = float(input("Enter operand2 : "))
except ValueError:
    print(ValueError)
    exit(0)
print()
print("For Addition -- '+'")
print("For Subtraction -- '-'")
print("For Multiplication -- '*'")
print("For Division -- '/'")
print()
operation = input("Select Operation : ")
calculator = Calculator(input1, input2)

if operation == '+':
    print("Result : ", calculator.addition())
elif operation == '-':
    print("Result : ", calculator.subtraction())
elif operation == '*':
    print("Result : ", calculator.multiplication())
elif operation == '/':
    print("Result : ", calculator.division())
