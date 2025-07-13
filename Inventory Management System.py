class Product:
    # Class-level variable to track total products created
    total_products = 0

    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        Product.total_products += 1

    def update_quantity(self, amount):
        """
        Update the product quantity.
        Positive amount adds stock, negative removes stock.
        Raises ValueError if resulting quantity is negative.
        """
        if self.quantity + amount < 0:
            raise ValueError(f"Cannot remove {abs(amount)} items from '{self.name}'. Not enough stock.")
        self.quantity += amount

    def display(self):
        """
        Print product details.
        """
        print(f"Name: {self.name}")
        print(f"Price: ₹{self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Category: {self.category}")

def categorize_products(products):
    """
    Categorize products by category using dict comprehension.
    Returns a dictionary: {category: [products]}
    """
    categories = set(p.category for p in products)
    return {cat: [p for p in products if p.category == cat] for cat in categories}

def filter_in_stock(products):
    """
    Returns a list of products with quantity > 0 using list comprehension.
    """
    return [p for p in products if p.quantity > 0]

# Example usage
if __name__ == "__main__":
    # Create some products
    p1 = Product("Apple", 0.5, 100, "Fruit")
    p2 = Product("Milk", 1.2, 50, "Dairy")
    p3 = Product("Banana", 0.3, 0, "Fruit")


    products = [p1, p2, p3]

    # Update quantity with exception handling
    try:
        p1.update_quantity(-150)  # Trying to remove more than in stock
    except ValueError as e:
        print("Exception:", e)

    p1.update_quantity(+20)  # Add 20 to apple
    p2.update_quantity(-10)  # Remove 10 from milk

    # Display all products
    print("\nAll Products:")
    for p in products:
        p.display()
        print("-" * 20)

    # Categorize products
    categorized = categorize_products(products)
    print("\nCategorized Products:")
    for category, items in categorized.items():
        print(f"{category}: {[p.name for p in items]}")

    # Filter out products with zero quantity
    #in_stock = filter_in_stock(products)
   # print("\nProducts In Stock:")
    #for p in in_stock:
        #print(f"{p.name} ({p.quantity} in stock)")

    filtered_products = [prod.name for prod in products if prod.quantity > 0]
    print(f"Filtered products (quantity > 0): {filtered_products}")

    # Show total products created
    print(f"\nTotal products created: {Product.total_products}")
    