# Problem Statement: Write a Python program that does the following:
# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
# o	Addition
# o	Subtraction
# o	Multiplication
# o	Division
# 3.  Displays the results of each operation on the screen.


number1 = input("Enter the first number: ")
number1 = int(number1)
number2 = input("Enter the second number: ")
number2 = int(number2)

Addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2

print("Addition: ", Addition)
print("Subtraction: ", subtraction)
print("Multiplication: ", multiplication)
print("Division: ", division)
