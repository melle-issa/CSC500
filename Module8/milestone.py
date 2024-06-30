# Module 8 Milestone
#
# This is an extension of the first and second milestone projects we did implementing a shopping cart
#
# By: Melissa Hidalgo 352865

def validate_input(input, input_type):
    if input_type == 'float':
        try:
            float(input)
            return True
        except ValueError:
            return False
    elif input_type == 'int':
        return input.isdigit()

class ItemToPurchase:
    # Default constructor
    def __init__(self, item_name = 'none', item_price = 0.0, item_quantity = 0, item_desc = 'none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_desc
    
    # Print cost method
    def print_item_cost(self):
        cost = self.item_price * self.item_quantity
        print('{} {} @ ${:.2f} = ${:.2f}'.format(self.item_name, self.item_quantity, self.item_price, cost))
        return cost
    
    # Print description method
    def print_item_description(self):
        print('{}: {}'.format(self.item_name, self.item_description))
    
class ShoppingCart:
    # Default constructor
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2020', cart_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
    
    # Add item
    def add_item(self, new_item):
        self.cart_items.append(new_item)
    
    # Remove item
    def remove_item(self, item_to_remove):
        item_pos = -1
        for pos, item in enumerate(self.cart_items):
            if item.item_name == item_to_remove:
                item_pos = pos
                break
        
        if item_pos != -1:
            del self.cart_items[pos]
        else:
            print('Item not found in cart. Nothing removed.')
    
    # Modify item
    def modify_item(self, item_to_modify):
        item_pos = -1
        for pos, item in enumerate(self.cart_items):
            if item.item_name == item_to_modify:
                item_pos = pos
                break
        
        if item_pos != -1:
            cart_item = self.cart_items[item_pos]
            if cart_item.item_name != 'none' and cart_item.item_price != 0.0 and cart_item.item_quantity != 0:
                new_quant = input('How much of {} would you like to buy? '.format(item_to_modify))
                while not validate_input(new_quant, 'int'):
                    new_quant = input('Please enter a valid integer for the new quantity ')
                cart_item.item_quantity = int(new_quant)
                self.cart_items[item_pos] = cart_item
                print('Item modified')
            else:
                print('Cannot modify item')
        else:
            print('Item not found in cart. Nothing modified.')

    # Number of items in cart
    def get_num_items_in_cart(self):
        total = 0
        for item in self.cart_items:
            total = total + item.item_quantity
        return total

    # Total price of cart
    def get_cost_of_cart(self):
        total = 0.0
        for item in self.cart_items:
            total = total + (item.item_quantity * item.item_price)
        return total

    # Print total cost
    def print_total(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('Number of Items: {}'.format(self.get_num_items_in_cart()))
            for item in self.cart_items:
                item.print_item_cost()
            print('Total: ${}'.format(self.get_cost_of_cart()))
    
    # Print descriptions
    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('Item Descriptions')
            for item in self.cart_items:
                item.print_item_description()

def print_menu(cart):
    choice = 'x'
    while choice != 'q':
        print()
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print('i - Output items\' descriptions')
        print('o - Output shopping cart')
        print('q - Quit')
    
        choice = input('Choose an option: ')
        print()

        valid_choices = ['a', 'r', 'c', 'i', 'o', 'q']
        while choice not in valid_choices:
            choice = input('Please enter a valid choice: ')

        if choice == 'a':
            print('ADD ITEM TO CART')
            name = input('Enter the item name: ')
            description = input('Enter the item description: ')
            price = input('Enter the item price: ')
            while not validate_input(price, 'float'):
                price = input('Invalid entry. Please enter a decimal: ')

            quantity = input('Enter the item quantity: ')
            while not validate_input(quantity, 'int'):
                quantity = input('Please enter a valid integer: ')

            new_item = ItemToPurchase(name, float(price), int(quantity), description)
            cart.add_item(new_item)
        elif choice == 'r':
            print('REMOVE ITEM')
            name = input('Enter the name of the item to be removed: ')
            cart.remove_item(name)
        elif choice == 'c':
            print('CHANGE ITEM QUANTITY')
            name = input('Enter the name of the item to change quantity of purchase: ')
            cart.modify_item(name)
        elif choice == 'i':
            print('\nOUTPUT ITEMS\' DESCRIPTIONS')
            cart.print_descriptions()
        elif choice == 'o':
            print('\nOUTPUT SHOPPING CART')
            cart.print_total()
        elif choice == 'q':
            break

        print()

print('Hello, welcome to our store!')

customer_name = input('Enter customer\'s name: ')
curr_date = input('Enter today\'s date: ')

print('Customer name: {}'.format(customer_name))
print('Today\'s date: {}'.format(curr_date))

cart = ShoppingCart(customer_name, curr_date)

print_menu(cart)
print('Thanks for shopping with us!')