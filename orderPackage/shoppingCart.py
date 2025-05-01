# shoppingCart.py

from customerPackage.customer import Customer
from orderPackage.order import Order

class ShoppingCart():

    def __init__(self, user_id):
        self.user_id = user_id
        self.order = Order(user_id)
        self.custMember = Customer(user_id)
        self.items = {}  # key: product_id, value: quantity

    def add_item(self, product_id, quantity=1):
        """
        Adds an item to the cart or increases its quantity if it already exists.

        @param product_id: str or int, the ID of the product to add
        @param quantity: int, number of items to add (default is 1)
        @return: None
        """
        if product_id in self.items:
            self.items[product_id] += quantity
        else:
            self.items[product_id] = quantity
        print(f"Added {quantity} x {product_id} to cart.")

    def remove_item(self, product_id):
        """
        Removes an item from the cart.

        @param product_id: str or int, the ID of the product to remove
        @return: None
        """
        if product_id in self.items:
            del self.items[product_id]
            print(f"Removed {product_id} from cart.")
        else:
            print("Item not in cart.")

    def change_quantity(self, product_id, quantity):
        """
        Changes the quantity of an existing item in the cart.
        @param product_id: str or int, the ID of the product
        @param quantity: int, the new quantity for the product
        @return: None
        """
        if product_id in self.items:
            self.items[product_id] = quantity
            print(f"Updated {product_id} quantity to {quantity}.")
        else:
            print("Item not in cart.")

    def view_cart(self):
        """
        Displays the contents of the cart with prices and subtotal per item
        Looks up product prices from the product table using the cursor
        @return: None
        """
        if not self.items:
            print("Cart is empty. Time to go shopping! ⋆｡˚")
        else:
            print("\nShopping Cart:")
            total = 0
            for product_id, quantity in self.items.items():
                try:
                    # Ensure quantity is iterable and sum its values if necessary
                    if isinstance(quantity, (list, tuple)):  # If quantity is multi-valued (list or tuple)
                        quantity = sum(quantity)  # Sum up all values
                    else:
                        quantity = int(quantity)  # Ensure quantity is an integer
                
                    self.order.cursor.execute("""
                                            SELECT price 
                                            FROM product
                                            WHERE product_id = %s
                                            """, 
                                            (product_id,))
                    result = self.order.cursor.fetchone()
                    if result:
                        # Ensure price is converted to a float (if it isn't already)
                        price = float(result[0]) if result[0] else 0  # Safe conversion to float
                        subtotal = price * quantity
                        total += subtotal
                        print(f"- {product_id}: {quantity} × ${price:.2f} = ${subtotal:.2f}")
                    else:
                        print(f"- {product_id}: {quantity} (Price not found)")
                except Exception as e:
                    print(f"Error retrieving price for product {product_id}: {e}")
            print(f"Total: ${total:.2f}")

    def checkout(self):
        """
        Finalizes the shopping cart 
        @return: None
        """
        if not self.items:
            print("Cart is empty.")
            return
        
        try:
            confirm_checkout = input("Do you want to check out? (y/n): ").strip().lower()
            if confirm_checkout != 'y':
                print("Checkout cancelled.")
                return
            self.order.generate_id(self.user_id)
            total_items = sum(self.items.values())
            self.order.balance = total_items
            self.order.cart = self.items

            self.view_cart()
            self.custMember.view_cards()

            card_name = input("Enter the EXACT nickname of the card you wish to use: ")
            self.order.add_credit_card_to_order(card_name)

            self.order.set_delivery_plan()

            confirm_purchase = input("Do you wish to confirm your purchase? (y/n): ").strip().lower()
            if confirm_purchase != 'y':
                print("Purchase cancelled.")
                return

            self.order.finalize_order_products(self.items, self.order.order_id)
            self.order.modify_row(self.order.order_id, self.user_id, self.order.balance, 'issued')
            self.order.show_order()
            self.items.clear()


        except Exception as e:
            print(f"Checkout failed: {e}")
            return None
                