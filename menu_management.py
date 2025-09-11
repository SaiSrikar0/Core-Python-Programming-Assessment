'''2. Restaurant Menu Management

Scenario:

You are managing a restaurant's menu. Write a program to update the menu by adding or removing items and allow users to check if a particular item is available.

Requirements:

- Use functions for adding, removing, and checking menu items.

- Handle cases where the item to be removed does not exist.

Input Example:

initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]

add_item = "Tacos"

remove_item = "Salad"

check_item = "Pizza"

Expected Output:

Updated menu: ["Pizza", "Burger", "Pasta", "Tacos"]

Availability: "Pizza is available"'''

def add_item(item, menu):
    if item not in menu:
        menu.append(item)
    return menu
def remove_item(item, menu):
    if item in menu:
        menu.remove(item)
    return menu
def check_item(item, menu):
    if item in menu:
        return f"{item} is available"
    return f"{item} is not available"
if __name__ == "__main__":
    menu = ["Pizza", "Burger", "Pasta", "Salad"]
    menu = add_item("Tacos", menu)
    menu = remove_item("Salad", menu)
    print("Updated menu:", menu)
    print("Availability:", check_item("Pizza", menu))
    print("Availability:", check_item("Sushi", menu))