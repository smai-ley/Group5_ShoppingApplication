# staff.py

from userPackage.user import User


class Staff(User):
    # adds, deletes, and modifies product and price to products
    # adds stock to warehouse
    
    def __init__(self):
        super().__init__()

    def show_products(self):
        return super().show_products()
    
    def show_stock(self):
        return super().show_stock()
    
    def add_product(self, prodNo, price):
        """
        Adds a product and its price into the table products as a new row
        @param prodNo: string, the product to be added
        @param price: float, the price to be added
        @return: none if unsuccessful
        """
        try:
            self.cursor.execute("""
                         INSERT INTO product (product_id, price)
                         VALUES (%s, %s)
                         """, (prodNo, price))
            print(prodNo + " successfully added to table.")
            self.conn.commit() # commit transaction
        except:
            self.conn.rollback()  # Reset connection after failure
            return None
        
    def delete_product(self, prodNo):
        """
        Removes a product from the product table 
        @param prodNo: string, the product_id of the product to be removed
        @return: None if unsuccessful
        """
        try:
            self.cursor.execute("""
                DELETE FROM product
                WHERE product_id = %s
            """, (prodNo,))
            self.conn.commit()
            print(prodNo + " successfully removed from table.")
        except Exception as e:
            self.conn.rollback()  # Reset connection after failure
            print("Error deleting product:", e)
            return None
    
    def modify_product(self, prodNo, price):
        """
        Modifies a product's price in the product table
        @param prodNo: string, the product ID to be changed
        @param price: float
        @return: none if unsuccessful
        """
        try:
            self.cursor.execute("""
                UPDATE product
                SET price = %s
                WHERE product_id = %s
            """, (prodNo, price))
            print(prodNo + "costing " + {price} + " successfully modified in table.")
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()  # Reset connection after failure
            print("Error modifying product:", e)
            return None
        
    def add_stock(self, prodNo, qty, warehouse_id = "wh_1"): # Remove prodNo depending on relational schema
        """
        Adds stock(product) and quantity info to warehouse table
        @param prodNo: string, the product to be added
        @param qty: int, the amount to be added
        @return: none if unsuccessful
        """
        try:
            self.cursor.execute("""
                         INSERT INTO stock (product_id, quantity, warehouse_id)
                         VALUES (%s, %s, %s)
                         """, (prodNo, qty, warehouse_id))
            print(qty + " of " + prodNo + " successfully added to table.")
            self.conn.commit() # commit transaction
        except:
            self.conn.rollback()  # Reset connection after failure
            return None

    
    