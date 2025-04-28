# shoppingCart.py

class ShoppingCart:
    def __init__(self):
        self.items = {}  # key: product_id, value: quantity

    def add_item(self, product_id, quantity=1):
        if product_id in self.items:
            self.items[product_id] += quantity
        else:
            self.items[product_id] = quantity
        print(f"Added {quantity} x {product_id} to cart.")

    def remove_item(self, product_id):
        if product_id in self.items:
            del self.items[product_id]
            print(f"Removed {product_id} from cart.")
        else:
            print("Item not in cart.")

    def change_quantity(self, product_id, quantity):
        if product_id in self.items:
            self.items[product_id] = quantity
            print(f"Updated {product_id} quantity to {quantity}.")
        else:
            print("Item not in cart.")

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            print("\nShopping Cart:")
            for product_id, quantity in self.items.items():
                print(f"- {product_id}: {quantity}")

    def checkout(self):
        if not self.items:
            print("Cart is empty.")
            return
        total_items = sum(self.items.values())
        print(f"Checked out {total_items} items.")
        self.items.clear()  # Empty cart after checkout
