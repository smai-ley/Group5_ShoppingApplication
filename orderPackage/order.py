# order.py

from userPackage.user import User

class Order(User):        
        
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.balance = 0.0
        self.order_id = None
        self.cart = {}
        self.delivery_type = "Standard"
        self.delivery_price = 5
        self.card_name = ""

    def generate_id(self, user_id):
        try:
            # GENERATE NEW ORDER NUMBER BASED ON EXISTING ORDER IDS
            self.cursor.execute("""
                                SELECT order_id 
                                FROM ordertable
                                """)
            existing_orders = self.cursor.fetchall()

            max_num = 0
            for (oid,) in existing_orders:
                if oid.startswith("ord_"):
                    try:
                        num = int(oid.split("_")[1])  # Get the number part after "ord_"
                        max_num = max(max_num, num)  # Get the highest order number
                    except ValueError:
                        continue

            new_order_id = f"ord_{max_num + 1}"
            self.order_id = new_order_id
            self.cursor.execute("""
                                INSERT INTO orders (order_id, balance, status)
                                VALUES (%s, %s, %s)
                                """, (self.order_id, self.balance, 'pending'))

            self.cursor.execute("""
                                INSERT INTO ordertable (order_id, customer_id)
                                VALUES (%s, %s)
                                """, (self.order_id, self.user_id))
            self.conn.commit()
            print(f"New order created: {self.order_id}")

        except Exception as e:
            self.conn.rollback()
            print(f"Error initializing order: {e}")
        
    def show_order(self):
        print(f"""
             _______________________________________________________
            /\                                                      \
        (O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)
            \/''''''''''''''''''''''''''''''''''''''''''''''''''''''/
            (                                                      (
             )     Order Id: {self.order_id}                        )
            (                                                       (
             )     User Id: {self.user_id}                          )
                   
            (      Delivery Plan:  {self.delivery_type}             (
             )                                                      )
            (      Card Used:   {self.card_name}                    (
             )                                                      )
                   Total: {self.balance}
            (                                                      (
             )     Thank you! :)                                    )
            (                                                      (
            /\''''''''''''''''''''''''''''''''''''''''''''''''''''''\    
        (O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)
            \/______________________________________________________/

            """)


    def modify_row(self, order_id, user_id, balance, status = "issued"):
        """
        Modifies an existing order row in the orders table.
        @param order_id: str, the ID of the order to update
        @param user_id: str or int, the customer/user ID
        @param balance: float, the total balance to update
        @param status: str, the new status of the order
        @return: None if unsuccessful
        """
        try:
            self.cursor.execute("""
                UPDATE orders
                SET customer_id = %s,
                    balance = %s,
                    status = %s
                WHERE order_id = %s
            """, (user_id, balance, status, order_id))
            self.conn.commit()
            print(f"Order {order_id} placed.")
        except Exception as e:
            self.conn.rollback()
            print(f"Error updating order: {e}")
            return None
    
    def add_credit_card_to_order(self, card_name):
        """
        Looks up a credit card by name for the user and adds it to the current order.
        @param card_name: str, the nickname or identifier of the credit card (e.g., 'Visa1', 'MyCard')
        @return: None if unsuccessful, prints status
        """
        try:
            self.cursor.execute("""
                SELECT card_number 
                FROM customercreditcard 
                WHERE customer_id = %s AND card_name = %s
            """, (self.user_id, card_name))
            self.card_name = card_name
            result = self.cursor.fetchone()
            if not result:
                print("No matching card found.")
                return
            card_number = result[0]
            self.cursor.execute("""
                UPDATE orders
                SET credit_card_info = %s
                WHERE order_id = %s
            """, (card_number, self.order_id))
        
            self.conn.commit()
            print(f"Card ending in {card_number[-4:]} added to order {self.order_id}.")

        except Exception as e:
            self.conn.rollback()
            print(f"Error adding credit card to order: {e}")
            return None

    def set_delivery_plan(self):
        """
        Prompts user to select a delivery type and updates the delivery plan for order Standard = 5, Express = 10
        @return: None if unsuccessful, prints confirmation or error
        """
        try:
            choice = input("Choose delivery type: 1 for Standard ($5), 2 for Express ($10): ")
            if choice == "1":
                delivery_type = "Standard"
                price = 5
            elif choice == "2":
                delivery_type = "Express"
                price = 10
            else:
                print("Invalid input. Please choose 1 or 2.")
                return
            self.cursor.execute("""
                UPDATE deliveryplan
                SET delivery_type = %s, price = %s
                WHERE order_id = %s
            """, (delivery_type, price, self.order_id))
            self.conn.commit()
            print(f"Delivery plan set to {delivery_type} for Order {self.order_id}.")
        except Exception as e:
            self.conn.rollback()
            print(f"Error updating delivery plan: {e}")
            return None

    def finalize_order_products(self, cart, order_id):
        """
        Inserts all items from the cart into the order_product table.
        @param order_id: str
        @return: None
        """
        try:
            for product_id, quantity in self.cart.items():
                self.cursor.execute("""
                    INSERT INTO orderproduct (order_id, product_id, quantity)
                    VALUES (%s, %s, %s)
                """, (self.order_id, product_id, quantity))
            self.conn.commit()
            print("Order items successfully recorded in order_product table.")
        except Exception as e:
            self.conn.rollback()
            print(f"Error inserting order products: {e}")
            return None