# customer.py

from itertools import product
from math import prod
from userPackage.user import User

class Customer(User):
    # adds, deletes, and modifies product and price to products
    # adds stock to warehouse

    def __init__(self, cust_id):
        self.cust_id = cust_id
        super().__init__()

    def show_products(self):
        """
        Browse products in the products table
        @param none
        @return none
        @except error e if unsuccessful
        """
        try:
            self.cursor.execute("SELECT product_id, type, brand, price FROM product")
            products = self.cursor.fetchall()
            if not products:
                print("No products available.")
            else:
                print("\nAvailable Products:")
                for product_id, type, brand, price in products:
                    print(f"- ID: {product_id} - Type: {type} - Brand: {brand} - Price: ${price:.2f}")
        except Exception as e:
            print(f"Error fetching products: {e}")
            self.conn.rollback()  # Reset connection after failure

    #Good
    def view_cards(self, cust_id): 
        """
        Views all cards associated with user 
        @return None
        """
        try:
            self.cursor.execute("""
                SELECT (card_name, card_number) FROM customercreditcard 
                WHERE customer_id = %s
            """, (cust_id))
            cards = self.cursor.fetchall()
            if not cards:
                print(f"No cards found for customer ID '{cust_id}'.")
            else:
                print(f"Cards for customer ID '{cust_id}':")
                for card in cards:
                    print(card)    
        except Exception as e:
            print(f"Error viewing cards: {e}")
            self.conn.rollback()  # Reset connection after failure
            return None

    #Good
    def add_card(self, card_name, card_number, cust_id, address="123 Main Str., New York City, New York, 12345"): 
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
                INSERT INTO customercreditcard (cust_id, card_name, card_number, payment_address)
                VALUES (%s, %s, %s, %s)
            """, (cust_id, card_name, card_number, address))
        
            print(f"{card_name} + {card_number} successfully added to table.")
            self.conn.commit()  # commit transaction
        except Exception as e:
            print(f"Error adding card: {e}")
            self.conn.rollback()  # Reset connection after failure
            return None
    
    #Good 
    def modify_card(self, card_name, new_card_number): # Needs adjustment to support multiple cards
        """
        Modify card number in customer info
        @param cust_id: str or int, the customer ID whose card will be modified
        @param new_cardnumber: int or str, the new card number
        @return: None if unsuccessful
        """
        try:
            self.cursor.execute("""
                UPDATE customercreditcard
                SET card_number = %s
                SET card_name = %s
                WHERE card_name = %s
                """, (new_card_number, card_name, card_name))
            print(new_card_number + "successfully modified in table.") 
            self.conn.commit() # commit transaction
        except: 
            self.conn.rollback()  # Reset connection after failure
            return None
        
    def delete_card(self, card_name):
        """
        Delete card from customer info
        @param cardnumber: int, the card to be deleted
        @return: none if unsuccessful
        """
        try:
            self.cursor.execute("""
                         DELETE FROM customercreditcard (card_name)
                         VALUES (%s)
                         WHERE card_name = %s
                         """, (card_name))
            print(card_name + "successfully removed from table.")
            self.conn.commit() # commit transaction
        except:
            self.conn.rollback()  # Reset connection after failure
            return None

    ### Modify Addresses
        
    def add_address(self, address): # address should be a csv string, THIS FUNCTION IS 85% CORRECT
        """
        Adds new address to customer info
        @param address: string, the address to be added
        @return: none if unsuccessful
        """
        try:
            self.cursor.execute("""
                         INSERT INTO customer (address)
                         VALUES (%s)
                         """, (address))
            print(address + "successfully added to table.")
            self.conn.commit() # commit transaction
        except:
            self.conn.rollback()  # Reset connection after failure
            return None
        
    def delete_address(self, address): # address should be a csv, THIS FUNCTION IS 95% CORRECT
        """
        Delete address from customer info
        @param address: string, the address to be deleted
        @return: none if unsuccessful
        """
        try:
            self.cursor.execute("""
                         DELETE FROM customer (address)
                         VALUES (%s)
                         """, (address))
            print(address + "successfully removed from table.")
            self.conn.commit() # commit transaction
        except:
            self.conn.rollback()  # Reset connection after failure
            return None
    
    def modify_address(self, address):
        """
        Modify address in customer info
        @param address: str, the address to be changed
        @return: none if unsuccessful
        """
        try:
            self.cursor.execute("""
                         UPDATE customer
                         SET address = %s
                         WHERE customer_id = %s
                         """, (address))
            print(address + "successfully modified in table.") 
            self.conn.commit() # commit transaction
        except: 
            self.conn.rollback()  # Reset connection after failure
            return None

    def view_balance(self):
        """
        Show customer balance
        @param none
        @return none
        @except error e if unsuccessful
        """
        try:
            self.cursor.execute("SELECT customer_id, balance FROM customer")
            products = self.cursor.fetchall()
            if not products:
                print("No balance available.")
            else:
                print("\Customer Balance:")
                for customer_id, balance in products:
                    print(f"- Customer ID: {customer_id} - Balance: ${balance}")
        except Exception as e:
            self.conn.rollback()  # Reset connection after failure
            print(f"Error fetching Stock: {e}")

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
                                    WHERE id = %s""", (prodNo))
            products = self.cursor.fetchall()
            print("\Customer Balance:")
            for product_id, type, brand, description, price in products:
                  print(f"- Product ID: {product_id} - Balance: ${balance}")
        except Exception as e:
            self.conn.rollback()  # Reset connection after failure
            print(f"Error fetching Stock: {e}")