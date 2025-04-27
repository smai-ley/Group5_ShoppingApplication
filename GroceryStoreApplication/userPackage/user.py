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
        
