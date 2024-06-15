# Module 6 Milestone
#
# This is an extension of the first milestone project we did implementing a shopping cart
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
                print('We can modify {} for you!'.format(item_to_modify))
                to_modify = input('What would you like to modify? Enter \'Description\', \'Price\', or \'Quantity\' ')
                if to_modify == 'Description':
                    new_desc = input('What would you like the new description for {} to be? '.format(item_to_modify))
                    cart_item.item_description = new_desc
                elif to_modify == 'Price':
                    new_price = input('What would you like the new price for {} to be? '.format(item_to_modify))
                    while not validate_input(new_price, 'float'):
                        new_price = input('Please enter a valid entry for the new price ')
                    cart_item.item_price = float(new_price)
                elif to_modify == 'Quantity':
                    new_quant = input('How much of {} would you like to buy? '.format(item_to_modify))
                    while not validate_input(new_quant, 'int'):
                        new_quant = input('Please enter a valid integer for the new quantity ')
                    cart_item.item_quantity = new_quant
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

        valid_choices = ['a', 'r', 'c', 'i', 'o', 'q']
        while choice not in valid_choices:
            choice = input('Please enter a valid choice: ')

        if choice == 'a':
            # place holder until module 8
            continue
        elif choice == 'r':
            # place holder until module 8
            continue
        elif choice == 'c':
            # place holder until module 8
            continue
        elif choice == 'i':
            print()
            cart.print_descriptions()
        elif choice == 'o':
            print()
            cart.print_total()
        elif choice == 'q':
            break

cart = ShoppingCart()

print('Hello, welcome to our store!')

item1 = ItemToPurchase()
item2 = ItemToPurchase()
item3 = ItemToPurchase()

item1.item_name = 'Nike Romaleos'
item1.item_quantity = 2
item1.item_price = 189.00
item1.item_description = 'Volt color, Weightlifting shoes'

item2.item_name = 'Powerbeats 2 Headphones'
item2.item_quantity = 1
item2.item_price = 128.00
item2.item_description = 'Bluetooth headphones'

item3.item_name = 'Chocolate Chips'
item3.item_quantity = 5
item3.item_price = 3.00
item3.item_description = 'Semi-sweet'

cart.add_item(item1)
cart.add_item(item3)
cart.add_item(item2)

print_menu(cart)