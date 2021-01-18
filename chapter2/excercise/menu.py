import sys
from products import Catalog

class Menu:
    """Display a menu and respond to choices when run."""

    def __init__(self):
        self.catalog = Catalog()
        self.choices = {
            "1": self.show_items,
            "2": self.search_items,
            "3": self.add_item,
            "4": self.modify_item,
            "5": self.quit,
        }

    def display_menu(self):
        print("""
        Notebook Menu

        1. Show all items
        2. Search items
        3. Add item
        4. Modify item
        5. Quit

        """)

    def run(self):
        """Display the menu and respond to choices."""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)

            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")

    def show_items(self, items=None):
        if not items:
            items = self.catalog.items

        for item in items:
            print(f"{item.id}: {item.tags}\n{item.product_name}")

    def search_items(self):
        filter = input("Search for: ")
        items = self.catalog.search(filter)
        self.show_items(items)

    def add_item(self):
        name = input("Enter a name: ")
        description = input("Enter a product description: ")
        tag = input("Enter a product tag: ")
        self.catalog.new_product(name, description, tag)

        print(f"{name} has ben added to the catalog.")

    def modify_item(self):
        id = input("Enter an item ID: ")
        name = input("Enter a name: ")
        description = input("Enter a product description: ")
        tag = input("Enter a product tag: ")

        if name:
            self.catalog.modify_name(id, name)
        if description:
            self.catalog.modify_description(id, description)
        if tag:
            self.catalog.modify_tags(id, tag)

    def quit(self):
        print("Thank you for using your Catalog today.")

if __name__ == "__main__":
    Menu().run()