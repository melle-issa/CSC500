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

# Create a list for all the costs to demonstrate knowledge of Python lists
all_costs = []

sub_charge = float(sub_charge_str)
tip = sub_charge * 0.18
sales_tax = sub_charge * 0.07
total = sub_charge + tip + sales_tax

all_costs.append(sub_charge)
all_costs.append(tip)
all_costs.append(sales_tax)
all_costs.append(total)

print('\n')
print('Price of meal: ${:.2f}'.format(all_costs[0]))
print('18% tip: ${:.2f}'.format(all_costs[1]))
print('7% sales tax: ${:.2f}'.format(all_costs[2]))
print('Total cost: ${:.2f}'.format(all_costs[3]))