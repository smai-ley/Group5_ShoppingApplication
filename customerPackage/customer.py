# customer.py

from additionalPackage.icon import Icon
from userPackage.user import User

class Customer(User):
    # adds, deletes, and modifies product and price to products
    # adds stock to warehouse

    def __init__(self, cust_id):
        self.cust_id = cust_id
        self.printer = Icon()
        super().__init__()

    def show_products(self):
        """
        Browse products in the products table
        @param none
        @return none
        @except error e if unsuccessful
        """
        try:
            self.cursor.execute("SELECT product_id, type, price FROM product")
            products = self.cursor.fetchall()
            if not products:
                print("No products available.")
            else:
                print("\n ⁺˚⋆｡°✩₊ Products Available: ⁺˚⋆｡°✩₊\n")
                for product_id, type, price in products:
                    print(f"⋆ ID: {product_id} ⋆ Category: {type} ⋆ Price: ${price:.2f}")
        except Exception as e:
            print(f"Error fetching products: {e}")
            self.conn.rollback()  # Reset connection after failure

    def view_cards(self, cust_id): 
        """
        Views all cards associated with user 
        @return None
        """
        try:
            self.cursor.execute("""
                SELECT card_name, card_number FROM customercreditcard 
                WHERE customer_id = %s
            """, (cust_id,))
            cards = self.cursor.fetchall()
            if not cards:
                print(f"No cards found for customer ID '{cust_id}'.")
            else:
                print(f"\n{cust_id}'s Cards:")
                for card_name, card_number in cards:
                    print(f"* Nickname: {card_name}\n* Card Number: {card_number}")
                print("\n")
        except Exception as e:
            print(f"Error viewing cards: {e}")
            self.conn.rollback()  # Reset connection after failure
            return None

    def add_card(self, card_name, card_number, cust_id, address="123 Main Str., New York City"): 
        """
        Adds new card to customer info
        @param cust_id: str, customer ID
        @param card_name: str, name of card
        @param cardnumber: int or str, card number
        @param address: str, payment address
        @return: None if unsuccessful
        """
        try:
            self.cursor.execute("""
                INSERT INTO customercreditcard (customer_id, card_name, card_number, payment_address)
                VALUES (%s, %s, %s, %s)
            """, (cust_id, card_name, card_number, address))
        
            print(f"{card_name} + {card_number} successfully added to table.")
            self.conn.commit()  # commit transaction
        except Exception as e:
            print(f"Error adding card: {e}")
            self.conn.rollback()  # Reset connection after failure
            return None
   
    def modify_card(self, card_name, new_card_name, new_card_number):
        """
        Modify card info in customercreditcard table
        @param card_name: str, the existing card name to look for
        @param new_card_name: str, the new name to set
        @param new_card_number: str or int, the new card number to set
        @return: None if unsuccessful
        """
        try:
            self.cursor.execute("""
                UPDATE customercreditcard
                SET card_number = %s,
                    card_name = %s
                WHERE card_name = %s
            """, (new_card_number, new_card_name, card_name))
            self.conn.commit()
            print(f"Card '{card_name}' updated to '{new_card_name}' with number {new_card_number}.")
        except Exception as e:
            self.conn.rollback()
            print("Error modifying card:", e)
            return None
        
    def delete_card(self, card_name):
        """
        Delete card from customer info
        @param cardnumber: int, the card to be deleted
        @return: none if unsuccessful
        """
        try:
            self.cursor.execute("""
                         DELETE FROM customercreditcard
                        WHERE card_name = %s
                         """, (card_name,))
            print(card_name + " successfully removed from table.")
            self.conn.commit() # commit transaction
        except:
            self.conn.rollback()  # Reset connection after failure
            return None

    ### Modify Addresses
        
    def add_address(self, address_id, address_text, del_add, pay_add, user_id): 
        """
        Adds a new address to the customer info table. If delivery or payment flag is set to True, it resets those flags for other addresses of the same user.
        @param address_id: string or int, the new address ID
        @param address_text: string, the address text
        @param del_add: any type (will be cast to boolean), True if delivery address
        @param pay_add: any type (will be cast to boolean), True if payment address
        @param user_id: string or int, the customer ID
        @return: None if unsuccessful
        """
        try:
            del_add = bool(del_add)
            pay_add = bool(pay_add)
            if del_add:
                self.cursor.execute("""
                    UPDATE address
                    SET delivery_address = FALSE
                    WHERE customer_id = %s
                """, (user_id,))
            if pay_add:
                self.cursor.execute("""
                    UPDATE address
                    SET payment_address = FALSE
                    WHERE customer_id = %s
                """, (user_id,))
            self.cursor.execute("""
                INSERT INTO address (address_id, address_text, delivery_address, payment_address, customer_id)
                VALUES (%s, %s, %s, %s, %s)
            """, (address_id, address_text, del_add, pay_add, user_id))
            print(address_id + " successfully added to table.")
            self.conn.commit()  # commit transaction
        except Exception as e:
            self.conn.rollback()  # Reset connection after failure
            print(f"Error adding address: {e}")
            return None
     
    def modify_address(self, address_id, address_text, del_add, pay_add, user_id): 
        """
        Modifies an existing address in the customer info table.
        If delivery or payment flag is set to True, it resets those flags for other addresses of the same user.

        @param address_id: string or int, the ID of the address to modify
        @param address_text: string, the new address text
        @param del_add: any type (cast to bool), True if delivery address
        @param pay_add: any type (cast to bool), True if payment address
        @param user_id: string or int, the customer ID linked to this address
        @return: None if unsuccessful
        """
        try: 
            del_add = bool(del_add)
            pay_add = bool(pay_add)
            if del_add:
                self.cursor.execute("""
                    UPDATE address
                    SET delivery_address = FALSE
                    WHERE customer_id = %s AND address_id != %s
                """, (user_id, address_id))
            if pay_add:
                self.cursor.execute("""
                    UPDATE address
                    SET payment_address = FALSE
                    WHERE customer_id = %s AND address_id != %s
                """, (user_id, address_id))
            self.cursor.execute("""
                UPDATE address
                SET address_text = %s,
                    delivery_address = %s,
                    payment_address = %s,
                    customer_id = %s
                WHERE address_id = %s
            """, (address_text, del_add, pay_add, user_id, address_id))
            print(address_id + " successfully modified in table.")
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(f"Error modifying address: {e}")
            return None

    def delete_address(self, address_id, user_id):
        """
        Delete address from customer info
        @param address: string, the address to be deleted
        @return: None if unsuccessful
        """
        try:
            self.cursor.execute("""
                DELETE FROM address
                WHERE address_id = %s
                    AND customer_id = %s                
            """, (address_id, user_id))
            self.conn.commit()
            print(address_id + " successfully removed from table.")
        except Exception as e:
            self.conn.rollback()
            print("Error deleting address:", e)
            return None

    def view_address(self, user_id):
        """
        Show customer addresses
        @param none
        @return none
        @except error e if unsuccessful
        """
        try:
            self.cursor.execute("""SELECT  address_id, address_text, delivery_address, payment_address 
                                FROM address 
                                WHERE customer_id = %s""", (user_id,))
            addresses = self.cursor.fetchall()
            if not addresses:
                print("No address available.")
            else:
                for address_id, address_text, delivery_address, payment_address in addresses:
                    print(f"\nAddresses for {user_id}:\n Address ID: {address_id}\n Address Line: {address_text}\n Delivery Address: {delivery_address}\n Payment_Address: {payment_address}\n")
        except Exception as e:
            self.conn.rollback()  # Reset connection after failure
            print(f"Error fetching Addresses: {e}")

    def view_balance(self, user_id):
        """
        Show customer balance
        @param none
        @return none
        @except error e if unsuccessful
        """
        try:
            self.cursor.execute("""SELECT customer_id, balance 
                                FROM customer 
                                WHERE customer_id = %s""", 
                                (user_id,))
            balances = self.cursor.fetchall()
            if not balances:
                print("No balance available.")
            else:
                print(f"\n{user_id} Balance:")
                for customer_id, balance in balances:
                    print(f"* Outstanding Payments: ${balance}\n")
        except Exception as e:
            self.conn.rollback()  # Reset connection after failure
            print(f"Error fetching Balance: {e}")

    def view_prodInfo(self, prodNo):
        """
        Shows ascii art for type of product
        @param ProdNo: string
        @return none
        @except error e if unsuccessful
        """
        try:
            self.cursor.execute("""SELECT product_id, type, brand, description, price 
                                    FROM product 
                                    WHERE product_id = %s""", (prodNo,))
            products = self.cursor.fetchall()
            print("\n.˚○ • °  Product Details .˚○ • ° \n")
            for product_id, prodType, brand, description, price in products:
                  print(f"⋆ Product ID: {product_id}\n⋆ Category: {prodType}\n⋆ Description: {brand} {description}\n⋆ Price: ${price}")
            self.printer.print_art(prodType)
        except Exception as e:
            self.conn.rollback()  # Reset connection after failure
            print(f"Error fetching Product Info: {e}")
       