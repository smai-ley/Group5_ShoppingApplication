# user.py

import psycopg2

class User:
    def __init__(self):
         self.conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="your_database",
            user="your_user",
            password="your_password")
         self.cursor = self.conn.cursor()
   
    def logOut(self):
        self.cursor.close()
        self.conn.close()
     
    def show_products(self):
        """
        Browse products in the products table
        @param none
        @return none
        @except error e if unsuccessful
        """
        try:
            self.execute("SELECT product_id, price FROM products")
            products = self.fetchall()
            if not products:
                print("No products available.")
            else:
                print("\nAvailable Products:")
                for product_id, price in products:
                    print(f"- {product_id}: ${price:.2f}")
        except Exception as e:
            print(f"Error fetching products: {e}")
