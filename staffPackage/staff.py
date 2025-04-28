# staff.py

from userPackage.user import User


class Staff(User):
    # adds, deletes, and modifies product and price to products
    # adds stock to warehouse
    
    def __init__(self):
        super().__init__()

    def show_products(self):
        return super().show_products()
    
    def add_product(self, prodNo, price):
        """
        Adds a product and its price into the table products as a new row
        @param prodNo: string, the product to be added
        @param price: float, the price to be added
        @return: none if unsuccessful
        """
        try:
            self.execute("""
                         INSERT INTO products (product_id, price)
                         VALUES (%s, %s)
                         """, (prodNo, price))
            print(prodNo + "successfully added to table.")
            self.commit() # commit transaction
        except:
            return None
        
    def delete_product(self, prodNo): # May need support for removing price according to rubric
        """
        Removes a product from products table 
        @param prodNo: string, the product to be removed
        @return: none if unsuccessful
        """
        try:
            self.execute("""
                         DELETE FROM products
                         WHERE id = %s
                         """, (prodNo,))
            print(prodNo + "successfully removed from table.")
            self.commit() # commit transaction
        except:
            return None
    
    def modify_product(self, prodNo, price):
        """
        Modifies a product and price in the product table
        @param prodNo: string, the product to be changed
        @param price: float
        @return: none if unsuccessful
        """
        try:
            self.execute("""
                         UPDATE products
                         SET product_id = %s, price = %s
                         WHERE id = %s
                         """, (prodNo, price))
            print(prodNo + "successfully modified in table.")
            self.commit() # commit transaction
        except: 
            return None
        
    def add_stock(self, prodNo, qty): # Remove prodNo depending on relational schema
        """
        Adds stock(product) and quantity info to warehouse table
        @param prodNo: string, the product to be added
        @param qty: int, the amount to be added
        @return: none if unsuccessful
        """
        try:
            self.execute("""
                         INSERT INTO warehouse (product_id, quantity)
                         VALUES (%s, %s)
                         """, (prodNo, qty))
            print(qty + " of " + prodNo + "successfully added to table.")
            self.commit() # commit transaction
        except:
            return None

    
    