# Module 4 Milestone: 
# Step 1: Build the ItemToPurchase class with the following specifications:
# Attributes
# item_name (string)
# item_price (float)
# item_quantity (int)
# Default constructor
# Initializes item's name = "none", item's price = 0, item's quantity = 0
# Method
# print_item_cost()
#
# Step 2: In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.
# 
# Step 3: Add the costs of the two items together and output the total cost.
# By: Melissa Hidalgo 352865

class ItemToPurchase:

    # Default constructor
    def __init__(self, item_name = 'none', item_price = 0.0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
    
    # Print method
    def print_item_cost(self):
        cost = self.item_price * self.item_quantity
        print('{} {} @ ${:.2f} = ${:.2f}'.format(self.item_name, self.item_quantity, self.item_price, cost))
        return cost

def validate_input(input, input_type):
    if input_type == 'float':
        try:
            float(input)
            return True
        except ValueError:
            return False
    elif input_type == 'int':
        return input.isdigit()

# We'll use a dictionary for the shopping cart
shopping_cart = {}
item_1 = ItemToPurchase()
item_2 = ItemToPurchase()

print('Hello, I\'m going to prompt you to add two items to your shopping cart. Let\'s start with item 1')

item_1.item_name = input('Enter the item name: ')

price_str = input('Enter the item price: ')
while not validate_input(price_str, 'float'):
    price_str = input('Please enter a valid price: ')
item_1.item_price = float(price_str)

quant_str = input('Enter the item quantity: ')
while not validate_input(quant_str, 'int'):
    quant_str = input('Please enter a valid integer: ')
item_1.item_quantity = int(quant_str)

shopping_cart[0] = item_1

print()
print('Let\'s move onto the second item')
item_2.item_name = input('Enter the item name: ')

price_str = input('Enter the item price: ')
while not validate_input(price_str, 'float'):
    price_str = input('Please enter a valid price: ')
item_2.item_price = float(price_str)

quant_str = input('Enter the item quantity: ')
while not validate_input(quant_str, 'int'):
    quant_str = input('Please enter a valid integer: ')
item_2.item_quantity = int(quant_str)

shopping_cart[1] = item_2

print()
print('TOTAL COST')
total = 0
for i in range(0, 2):
    total += shopping_cart[i].print_item_cost()

print('Total: ${:.2f}'.format(total))