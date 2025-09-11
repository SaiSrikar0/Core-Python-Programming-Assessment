'''1. E-Commerce Cart System** 

Scenario:

You are designing the logic for an e-commerce website. Write a program to calculate the total price of items in a user's cart. If the cart contains more than 5 items, apply 10% discount.

Requirements:

- Use a function to calculate the total price.

- Handle cases where the cart is empty.

Input Example:

cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}

Expected Output:

Total Price: 54000'''

def calculate(cart_items):
    if not cart_items:
        return 0
    total = sum(cart_items.values())
    if len(cart_items) > 5:
        total *= 0.9
    return total
if __name__ == "__main__":
    cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
    print(calculate(cart_items))