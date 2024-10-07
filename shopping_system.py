class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    # Method to display product information
    def display_product_info(self):
        print(f"Product: {self.product_name}, Price: {self.price}, Stock: {self.quantity_in_stock}")


class ShoppingCart:
    # Class variable to track total carts created
    total_carts = 0

    # Constructor for ShoppingCart class
    def __init__(self):
        self.items = []  # List of tuples (product, quantity)
        ShoppingCart.total_carts += 1

    # Method to add a product to the cart
    def add_to_cart(self, product, quantity):
        if product.quantity_in_stock >= quantity:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity
        else:
            print(f"Not enough stock for {product.product_name}")

    # Method to remove a product from the cart
    def remove_from_cart(self, product):
        self.items = [item for item in self.items if item[0] != product]

    # Method to display cart contents
    def display_cart(self):
        print("Cart contents:")
        for product, quantity in self.items:
            print(f"{product.product_name}: {quantity} units")

    # Method to calculate total price
    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.items)
        return total


# Creating Product objects
product1 = Product("Phone", 1200, 10)
product2 = Product("Headphones", 150, 25)
product3 = Product("Mouse", 50, 50)

# Creating two separate ShoppingCart instances
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Performing a series of operations on cart1
cart1.add_to_cart(product1, 1)
cart1.add_to_cart(product2, 2)
cart1.display_cart()
print(f"Total for cart1: {cart1.calculate_total()}")

# Performing a series of operations on cart2
cart2.add_to_cart(product3, 3)
cart2.remove_from_cart(product3)
cart2.add_to_cart(product2, 1)
cart2.display_cart()
print(f"Total for cart2: {cart2.calculate_total()}")
