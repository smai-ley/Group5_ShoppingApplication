# user.py

import psycopg2

class User:
    def __init__(self):
         self.conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="postgres",
            user="postgres",
            password="matchaluvr")
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
            self.cursor.execute("SELECT product_id, price FROM product")
            products = self.cursor.fetchall()
            if not products:
                print("No products available.")
            else:
                print("\nAvailable Products:")
                for product_id, price in products:
                    print(f"- ID: {product_id} - Price: ${price:.2f}")
        except Exception as e:
            print(f"Error fetching products: {e}")
