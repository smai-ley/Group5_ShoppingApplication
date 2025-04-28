# customer.py

from userPackage.user import User

class Customer(User):
    # adds, deletes, and modifies product and price to products
    # adds stock to warehouse

    def __init__(self):
        super().__init__("CUSTOMER")

    def show_products(self):
        return super().show_products()

    #Good
    def view_cards(self, cust_id = "cust_1"): 
        """
        Views all cards associated with user (cust_1)
        @return None
        """
        try:
            self.execute("""
                SELECT * FROM customercreditcard
                WHERE cust_id = %s
            """, (cust_id,))
            cards = self.fetchall()
            if not cards:
                print(f"No cards found for customer ID '{cust_id}'.")
            else:
                print(f"Cards for customer ID '{cust_id}':")
                for card in cards:
                    print(card)    
        except Exception as e:
            print(f"Error viewing cards: {e}")
            return None

    #Good
    def add_card(self, card_name, card_number, cust_id = "cust_1", address="123 Main Str., New York City, New York, 12345"): 
        """
        Adds new card to customer info
        @param cust_id: str, customer ID
        @param card_name: str, name of card
        @param cardnumber: int or str, card number
        @param address: str, payment address
        @return: None if unsuccessful
        """
        try:
            self.execute("""
                INSERT INTO customercreditcard (cust_id, card_name, card_number, payment_address)
                VALUES (%s, %s, %s, %s)
            """, (cust_id, card_name, card_number, address))
        
            print(f"{card_name} + {card_number} successfully added to table.")
            self.commit()  # commit transaction
        except Exception as e:
            print(f"Error adding card: {e}")
            return None
    
    #Good 
    def modify_card(self, card_name, new_card_number, cust_id ="cust_1"): # Needs adjustment to support multiple cards
        """
        Modify card number in customer info
        @param cust_id: str or int, the customer ID whose card will be modified
        @param new_cardnumber: int or str, the new card number
        @return: None if unsuccessful
        """
        try:
            self.execute("""
                UPDATE customercreditcard
                SET card_number = %s
                WHERE card_name = %s
                """, (new_card_number))
            print(new_card_number + "successfully modified in table.") 
            self.commit() # commit transaction
        except: 
            return None
        
    def delete_card(self, cardnumber):
        """
        Delete card from customer info
        @param cardnumber: int, the card to be deleted
        @return: none if unsuccessful
        """
        try:
            self.execute("""
                         DELETE FROM customers (creditcard)
                         VALUES (%s)
                         """, (cardnumber))
            print(cardnumber + "successfully removed from table.")
            self.commit() # commit transaction
        except:
            return None

    ### Modify Addresses
        
    def add_address(self, address): # address should be a csv string, THIS FUNCTION IS 85% CORRECT
        """
        Adds new address to customer info
        @param address: string, the address to be added
        @return: none if unsuccessful
        """
        try:
            self.execute("""
                         INSERT INTO customers (creditcard)
                         VALUES (%s)
                         """, (address))
            print(address + "successfully added to table.")
            self.commit() # commit transaction
        except:
            return None
        
    def delete_address(self, address): # address should be a csv, THIS FUNCTION IS 95% CORRECT
        """
        Delete address from customer info
        @param address: string, the address to be deleted
        @return: none if unsuccessful
        """
        try:
            self.execute("""
                         DELETE FROM customers (address)
                         VALUES (%s)
                         """, (address))
            print(address + "successfully removed from table.")
            self.commit() # commit transaction
        except:
            return None
    
    def modify_address(self, address):
        """
        Modify card in customer info
        @param cardnumber: int, the card to be changed
        @return: none if unsuccessful
        """
        try:
            self.execute("""
                         UPDATE customers
                         SET creditcard = %s
                         WHERE id = %s
                         """, (address))
            print(address + "successfully modified in table.") 
            self.commit() # commit transaction
        except: 
            return None
