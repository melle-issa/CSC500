# Module 1 CTA Part 2:
# Write a Python program to find the multiplication and division of two numbers.
# Ask the user to input two numbers (num1 and num2). Given those two numbers, multiply them together to find the output.
# Also, divide num1/num2 to find the output.
#
# By Melissa Hidalgo 352865

print('Welcome to the multiplication and division calculator!\n')

num1 = input('Please input the first number: ')
valid = num1.isdigit()
# Make sure entry 1 is valid
while not valid:
    print('Invalid entry. Please enter an integer\n')
    num1 = input('Please input the first number: ')
    valid = num1.isdigit()

num2 = input('Please input the second number: ')
valid = num2.isdigit()
# Make sure entry 2 is valid
while not valid:
    print('Invalid entry. Please enter an integer\n')
    num2 = input('Please input the second number: ')
    valid = num2.isdigit()

# Convert to int
num1 = int(num1)
num2 = int(num2)

product = num1 * num2
quotient = num1 / num2
print('\nThe product of', num1, 'and', num2, 'is:', product)
print('The quotient between', num1, 'and', num2, 'is:', quotient)