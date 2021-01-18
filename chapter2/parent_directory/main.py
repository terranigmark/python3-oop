import ecommerce.products
product = ecommerce.products.Product()

from ecommerce.products import Product
product = Product()

from ecommerce import products
product = products.Product()

class UsefulClass:
    """This class might be useful for other modules"""

    pass

def main():
    """Create a useful class and does something with it for our module"""

    useful = UsefulClass()
    print(useful)


if __name__ == "__main__":
    main()