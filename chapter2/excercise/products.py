import datetime

# Store the next available id for all new products
last_id = 0

class Product:
    """
    Represents a product in the catalog.
    Match against a string in searches and store tags for each product.
    """

    def __init__(self, product_name, description, tags=""):
        """Initialize a product with name, description and optional space-separated tags.
        Automatically set the product's creation date and a unique ID."""

        self.product_name = product_name
        self.description = description
        self.tags = tags
        self.creation_date = datetime.date.today()

        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """Determine if this product matches the filter text.
        Return True if it matches, False otherwise.

        Search is case sensitive and matches both name, description and tags."""

        return filter in self.product_name or filter in self.description or filter in self.tags


class Catalog:
    """Represents a collection of products that can be named, described, modified or tagged."""

    def __init__(self):
        """Initialize a catalog with an empty list."""
        self.items = []

    def new_product(self, product_name, description, tags=""):
        """Creates a new item to add it to the list."""
        self.items.append(Product(product_name, description, tags))

    def _find_product(self, product_id):
        """Locate the item with the given id."""
        for item in self.items:
            if str(item.id) == str(product_id):
                return item

        return None

    def modify_name(self, product_id, product_name):
        """Find the item with given id and changes its name."""
        product = self._find_product(product_id)

        if product:
            product.product_name = product_name
            return True

        return False

    def modify_description(self, product_id, description):
        """Find the item with given id and changes its description."""
        product = self._find_product(product_id)

        if product:
            product.description = description
            return True

        return False

    def modify_tags(self, product_id, tags):
        """Find the item with given id and changes its tags."""
        product = self._find_product(product_id)

        if product:
            product.tags = tags
            return True

        return None

    def search(self, filter):
        """Find all items that match the given filter string."""
        return [product for product in self.items if product.match(filter)]