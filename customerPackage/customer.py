# customer.py

from userPackage.user import User


class Customer(User):
    # adds, deletes, and modifies product and price to products
    # adds stock to warehouse

    def __init__(self):
        super().__init__("CUSTOMER")

    ### Modify Cards
    
    def addCard(self, cardnumber):
        """
        Adds new card to customer info
        @param cardnumber: int, the card to be added
        @return: none if unsuccessful
        """
        try:
            self.execute("""
                         INSERT INTO customers (creditcard)
                         VALUES (%s)
                         """, (cardnumber))
            print(cardnumber + "successfully added to table.")
            self.commit() # commit transaction
        except:
            return None
        
    def deleteCard(self, cardnumber):
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
    
    def modifyCard(self, cardnumber): # Needs adjustment to support multiple cards
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
                         """, (cardnumber))
            print(cardnumber + "successfully modified in table.") 
            self.commit() # commit transaction
        except: 
            return None

    ### Modify Addresses
        
    def addAddress(self, address): # address should be a csv string, THIS FUNCTION IS 85% CORRECT
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
        
    def deleteAddress(self, address): # address should be a csv, THIS FUNCTION IS 95% CORRECT
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
    
    def modifyCard(self, address):
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