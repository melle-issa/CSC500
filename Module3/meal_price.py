# Module 3 CTA Part 1: 
# Write a program that calculates the total amount of a meal purchased at a restaurant.
# The program should ask the user to enter the charge for the food and then calculate the
# amounts with an 18 percent tip and 7 percent sales tax. Display each of these amounts and the total price.
#
# By: Melissa Hidalgo 352865

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

sub_charge_str = input('Enter the cost of your meal: ')

valid = is_float(sub_charge_str) or sub_charge_str.isdigit()
# Make sure entry is valid
while not valid:
    sub_charge_str = input('Invalid entry. Please enter the cost of your meal: ')
    valid = is_float(sub_charge_str) or sub_charge_str.isdigit()

sub_charge = float(sub_charge_str)

tip = sub_charge * 0.18
sales_tax = sub_charge * 0.07
total = sub_charge + tip + sales_tax

print('\n')
print('Price of meal: $', end = '')
print('{:.2f}'.format(sub_charge))
print('18% tip: $', end = '')
print('{:.2f}'.format(tip))
print('7% sales tax: $', end = '')
print('{:.2f}'.format(sales_tax))
print('Total cost: $', end = '')
print('{:.2f}'.format(total))