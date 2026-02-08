"""
Perform besic mathematical operations on two numbers.
The operations include addition, subtraction, multiplication, and division.
The program should take two numbers as input from the user and then display the results of all four operations.
"""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print()
print()

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
if num2 != 0:              ## Check for division by zero
 division = num1 / num2

 print("Addition:", addition)
 print("Subtraction:", subtraction)
 print("Multiplication:", multiplication)
 print("Division:", round(division,2))      ## Round the division result to 2 decimal places
else:
 print("Division by zero is not allowed.")         ## Handle division by zero case