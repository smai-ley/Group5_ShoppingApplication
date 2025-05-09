﻿# shoppingCart.py

global_cart = {}

from customerPackage.customer import Customer
from orderPackage.order import Order

class ShoppingCart:
    def __init__(self, user_id):
        self.user_id = user_id
        self.order = Order(user_id)
        self.custMember = Customer(user_id)
        # Use global cart for this session
        self.items = global_cart.get(self.user_id, {})  # Retrieve user-specific cart from global cart

    def add_item(self, product_id, quantity):
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
            
    def update_customer_balance(self):
        """
        Updates the customer's balance with the balance of the finished order.
        @return: None
        """
        try:
            if self.order.balance > 0:
                # Update the balance for the customer in the customer table
                self.custMember.cursor.execute("""
                    UPDATE customer
                    SET balance = balance + %s
                    WHERE customer_id = %s
                """, (self.order.balance, self.user_id))
            
                self.custMember.conn.commit()  # Commit the transaction
                print(f"Customer {self.user_id}'s balance updated by ${self.order.balance:.2f}.")
            else:
                print("No balance to update. Order balance is zero.")
        except Exception as e:
            self.custMember.conn.rollback()  # Rollback transaction if error occurs
            print(f"Error updating customer balance: {e}")

    def view_cart(self):
        """
        Displays the contents of the cart with prices and subtotal per item.
        Looks up product prices from the product table using the cursor.
        @return: None
        """
        if not self.items:
            print("Cart is empty. Time to go shopping!")
        else:
            print("\nShopping Cart:")
            total = 0
            for product_id, quantity in self.items.items():
                try:
                    # Ensure quantity is an integer
                    quantity = int(quantity)
                
                    self.order.cursor.execute("""
                        SELECT price FROM product WHERE product_id = %s
                    """, (product_id,))
                    result = self.order.cursor.fetchone()
                
                    if result:
                        # Ensure price is a float
                        price = float(result[0]) if result[0] else 0  # Safe conversion to float
                        subtotal = price * quantity  # Multiply price by quantity
                        total += subtotal
                        print(f"- {product_id}: {quantity} × ${price:.2f} = ${subtotal:.2f}")
                    else:
                        print(f"- {product_id}: {quantity} (Price not found)")
                except Exception as e:
                    print(f"Error retrieving price for product {product_id}: {e}")
            print(f"Total: ${total:.2f}")

global_cart = {}

from customerPackage.customer import Customer
from orderPackage.order import Order

class ShoppingCart:
    def __init__(self, user_id):
        self.user_id = user_id
        self.order = Order(user_id)
        self.custMember = Customer(user_id)
        
        # Use global cart for this session
        self.items = global_cart.get(self.user_id, {})  # Retrieve user-specific cart from global cart

    def add_item(self, product_id, quantity):
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
        
        # Update the global cart with the modified items
        global_cart[self.user_id] = self.items

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
        
        # Update the global cart with the modified items
        global_cart[self.user_id] = self.items

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
        
        # Update the global cart with the modified items
        global_cart[self.user_id] = self.items
            
    def update_customer_balance(self):
        """
        Updates the customer's balance with the balance of the finished order.
        @return: None
        """
        try:
            if self.order.balance > 0:
                # Update the balance for the customer in the customer table
                self.custMember.cursor.execute("""
                    UPDATE customer
                    SET balance = balance + %s
                    WHERE customer_id = %s
                """, (self.order.balance, self.user_id))
            
                self.custMember.conn.commit()  # Commit the transaction
                print(f"Customer {self.user_id}'s balance updated by ${self.order.balance:.2f}.")
            else:
                print("No balance to update. Order balance is zero.")
        except Exception as e:
            self.custMember.conn.rollback()  # Rollback transaction if error occurs
            print(f"Error updating customer balance: {e}")

    def view_cart(self):
        """
        Displays the contents of the cart with prices and subtotal per item.
        Looks up product prices from the product table using the cursor.
        @return: None
        """
        if not self.items:
            print("Cart is empty. Time to go shopping!")
        else:
            print("\nShopping Cart:")
            total = 0
            for product_id, quantity in self.items.items():
                try:
                    # Ensure quantity is an integer
                    quantity = int(quantity)
                
                    self.order.cursor.execute("""
                        SELECT price FROM product WHERE product_id = %s
                    """, (product_id,))
                    result = self.order.cursor.fetchone()
                
                    if result:
                        # Ensure price is a float
                        price = float(result[0]) if result[0] else 0  # Safe conversion to float
                        subtotal = price * quantity  # Multiply price by quantity
                        total += subtotal
                        print(f"- {product_id}: {quantity} × ${price:.2f} = ${subtotal:.2f}")
                    else:
                        print(f"- {product_id}: {quantity} (Price not found)")
                except Exception as e:
                    print(f"Error retrieving price for product {product_id}: {e}")
            print(f"Total: ${total:.2f}")

    def checkout(self):
        """
        Finalizes the shopping cart.
        @return: None
        """
        if not self.items:
            print("Cart is empty.")
            return
        else:
            try:
                confirm_checkout = input("Do you want to check out? (y/n): ").strip().lower()
                if confirm_checkout != 'y':
                    print("Checkout cancelled.")
                    return
            
                self.order.generate_id(self.user_id)

                # Ensure quantities are integers and sum them up
                total_items = sum(int(quantity) for quantity in self.items.values())  # Convert all quantities to integers

                self.order.balance = total_items
                self.order.cart = self.items

                self.view_cart()  # Display the current cart items
                self.custMember.view_cards(self.user_id)

                card_name = input("Enter the EXACT nickname of the card you wish to use: ")
                self.order.add_credit_card_to_order(card_name)

                self.order.set_delivery_plan()

                confirm_purchase = input("Do you wish to confirm your purchase? (y/n): ").strip().lower()
                if confirm_purchase != 'y':
                    print("Purchase cancelled.")
                    return

                # Finalize order and update the database
                self.order.finalize_order_products(self.items, self.order.order_id)
                self.order.modify_row(self.order.order_id, self.user_id, self.order.balance, 'issued')
                self.update_customer_balance()
                self.order.show_order()

                # Save the updated cart to the global cart (to preserve across sessions)
                global_cart[self.user_id] = self.items

                # Clear the cart after successful checkout
                self.items.clear()
                print("Cart has been cleared.")

            except Exception as e:
                print(f"Checkout failed: {e}")
                return None