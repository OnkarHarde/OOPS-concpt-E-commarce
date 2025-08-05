# Product class
class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

# Cart class
class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product):
        self.items.append(product)
        print(f"{product.name} added to cart.")

    def show_cart(self):
        if not self.items:
            print("Cart is empty.")
            return
        print("\nYour Cart:")
        total = 0
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ₹{item.price}")
            total += item.price
        print(f"Total: ₹{total}")

# Store class
class Store:
    def __init__(self):
        self.products = [
            Product(1, "T-shirt", 500),
            Product(2, "Shoes", 1200),
            Product(3, "Watch", 800),
        ]
        self.cart = Cart()

    def show_products(self):
        print("\nAvailable Products:")
        for p in self.products:
            print(f"{p.pid}. {p.name} - ₹{p.price}")

    def buy(self):
        while True:
            self.show_products()
            choice = input("Enter product ID to add to cart (or 'q' to quit): ")
            if choice == 'q':
                break
            for p in self.products:
                if str(p.pid) == choice:
                    self.cart.add_to_cart(p)
                    break
            else:
                print("Invalid product ID.")
        self.cart.show_cart()


store = Store()
store.buy()
